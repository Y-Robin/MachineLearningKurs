"""CPU-Werkzeuge für NN2: Daten, Training und eingefrorener MobileNet-Backbone."""
from pathlib import Path
import copy
import hashlib
import json
import numpy as np
import pandas as pd
import torch
from torch import nn
from torch.utils.data import DataLoader, TensorDataset
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

ROOT=Path(__file__).resolve().parent
DEVICE=torch.device('cpu')


def cpu_setup(seed=42):
    if torch.version.cuda is not None:
        raise RuntimeError('Bitte die CPU-Builds aus requirements-cpu.txt installieren.')
    torch.manual_seed(seed)
    np.random.seed(seed)
    torch.set_num_threads(2)
    plt.rcParams.update({'figure.figsize':(10,4),'figure.dpi':105,
                         'axes.spines.top':False,'axes.spines.right':False,
                         'axes.grid':True,'grid.alpha':0.2,'legend.frameon':False})
    return DEVICE


def ziffern_split(seed=42):
    daten=load_digits()
    bilder=torch.tensor(daten.images/16.0,dtype=torch.float32).unsqueeze(1)
    labels=torch.tensor(daten.target,dtype=torch.long)
    ids=np.arange(len(labels))
    train,rest=train_test_split(ids,test_size=0.4,random_state=seed,stratify=daten.target)
    val,test=train_test_split(rest,test_size=0.5,random_state=seed,stratify=daten.target[rest])
    return bilder,labels,{'train':train,'val':val,'test':test}


def loader(x,y,batch_size=64,shuffle=False,seed=42):
    return DataLoader(TensorDataset(x,y),batch_size=batch_size,shuffle=shuffle,
                      generator=torch.Generator().manual_seed(seed),num_workers=0)


@torch.inference_mode()
def auswerten(modell,daten_loader):
    modell.eval()
    verlust=nn.CrossEntropyLoss(reduction='sum')
    loss=0.0; probs=[]; labels=[]
    for x,y in daten_loader:
        logits=modell(x.to(DEVICE))
        loss+=float(verlust(logits,y.to(DEVICE)))
        probs.append(logits.softmax(dim=1).cpu()); labels.append(y.cpu())
    p=torch.cat(probs); y=torch.cat(labels)
    return {'loss':loss/len(y),'accuracy':float((p.argmax(1)==y).float().mean())},p,y


def trainiere(modell,train_loader,val_loader,epochen=20,lr=0.003):
    modell.to(DEVICE)
    optimizer=torch.optim.Adam((p for p in modell.parameters() if p.requires_grad),lr=lr)
    loss_fn=nn.CrossEntropyLoss()
    best_loss=float('inf'); best_state=None; zeilen=[]
    for epoche in range(1,epochen+1):
        modell.train()
        loss_sum=0.0; richtig=0; anzahl=0
        for x,y in train_loader:
            x,y=x.to(DEVICE),y.to(DEVICE)
            optimizer.zero_grad(set_to_none=True)
            logits=modell(x)
            loss=loss_fn(logits,y)
            loss.backward()
            optimizer.step()
            loss_sum+=float(loss.detach())*len(y)
            richtig+=int((logits.argmax(1)==y).sum()); anzahl+=len(y)
        val,_,_=auswerten(modell,val_loader)
        zeilen.append({'epoche':epoche,'train_loss':loss_sum/anzahl,'val_loss':val['loss'],
                       'train_accuracy':richtig/anzahl,'val_accuracy':val['accuracy']})
        if val['loss']<best_loss:
            best_loss=val['loss']; best_state=copy.deepcopy(modell.state_dict())
    modell.load_state_dict(best_state)
    return pd.DataFrame(zeilen).set_index('epoche')


def lernkurven(historie):
    fig,axes=plt.subplots(1,2,figsize=(11,4))
    historie[['train_loss','val_loss']].plot(ax=axes[0]); axes[0].set(ylabel='Cross-Entropy',title='Loss über Epochen')
    historie[['train_accuracy','val_accuracy']].plot(ax=axes[1]); axes[1].set(ylabel='Accuracy',title='Training vs. Validierung',ylim=(0,1.03))
    plt.tight_layout(); plt.show()


def bildgalerie(bilder,labels,probs=None,anzahl=12):
    n=min(anzahl,len(bilder)); cols=6; rows=(n+cols-1)//cols
    fig,axes=plt.subplots(rows,cols,figsize=(11,2.5*rows),squeeze=False)
    for ax in axes.flat: ax.axis('off')
    for i,ax in enumerate(axes.flat):
        if i>=n: break
        ax.imshow(bilder[i,0].cpu(),cmap='gray',vmin=0,vmax=1,interpolation='nearest')
        titel=f'Ist: {int(labels[i])}'
        if probs is not None:
            pred=int(probs[i].argmax()); titel+=f' | Netz: {pred}'
            ax.set_title(titel,color='tab:green' if pred==int(labels[i]) else 'tab:red',fontsize=10)
        else: ax.set_title(titel,fontsize=10)
    plt.tight_layout(); plt.show()


class KleinesCNN(nn.Module):
    def __init__(self,kanaele=8):
        super().__init__()
        self.features=nn.Sequential(nn.Conv2d(1,kanaele,3,padding=1),nn.ReLU(),nn.MaxPool2d(2),
                                    nn.Conv2d(kanaele,16,3,padding=1),nn.ReLU(),nn.MaxPool2d(2))
        self.head=nn.Sequential(nn.Flatten(),nn.Linear(16*2*2,10))
    def forward(self,x):
        return self.head(self.features(x))


class FrozenMobileNet(nn.Module):
    """Alle Backbone-Gewichte und BatchNorm-Puffer bleiben eingefroren."""
    def __init__(self):
        super().__init__()
        from torchvision.models import mobilenet_v3_small,MobileNet_V3_Small_Weights
        torch.hub.set_dir(str(ROOT/'daten/torch_cache'))
        self.weights=MobileNet_V3_Small_Weights.IMAGENET1K_V1
        try:
            original=mobilenet_v3_small(weights=self.weights,progress=False).to(DEVICE)
        except Exception as exc:
            raise RuntimeError('MobileNet-Gewichte nicht verfügbar. Einmaliger Internetzugang für '
                               'https://download.pytorch.org/models/mobilenet_v3_small-047dcff4.pth nötig.') from exc
        self.backbone=nn.Sequential(original.features,original.avgpool,nn.Flatten())
        for p in self.backbone.parameters(): p.requires_grad_(False)
        self.backbone.eval()
        self.head=nn.Linear(576,10)
        self.register_buffer('feature_mean',torch.zeros(576))
        self.register_buffer('feature_std',torch.ones(576))
    def train(self,mode=True):
        super().train(mode)
        self.backbone.eval()  # Auch laufende BatchNorm-Statistiken einfrieren.
        return self
    def forward(self,x):
        with torch.no_grad(): f=self.backbone(x)
        return self.head((f-self.feature_mean)/self.feature_std)


def backbone_hash(modell):
    h=hashlib.sha256()
    for name,tensor in modell.backbone.state_dict().items():
        h.update(name.encode()); h.update(tensor.detach().cpu().contiguous().numpy().tobytes())
    return h.hexdigest()


def mobilenet_bilder(bilder,weights):
    """8x8-Graustufen -> RGB-PIL -> offizielles ImageNet-Preprocessing."""
    from PIL import Image
    transform=weights.transforms()
    result=[]
    for bild in bilder:
        array=(bild[0].numpy()*255).round().astype(np.uint8)
        pil=Image.fromarray(array).convert('RGB')
        result.append(transform(pil))
    return torch.stack(result)


@torch.inference_mode()
def extrahiere_features(modell,bilder,batch_size=16):
    """Einmalige eingefrorene Feature-Extraction; Cache ohne gelernte Zielstatistiken."""
    cache_dir=ROOT/'daten/feature_cache'; cache_dir.mkdir(parents=True,exist_ok=True)
    key=hashlib.sha256(bilder.contiguous().numpy().tobytes()+
                       (str(modell.weights)+repr(modell.weights.transforms())+backbone_hash(modell)).encode()).hexdigest()[:20]
    path=cache_dir/f'digits_mobilenet_{key}.npz'
    if path.exists():
        with np.load(path,allow_pickle=False) as data: features=torch.from_numpy(data['features'].copy())
        if features.shape!=(len(bilder),576) or not torch.isfinite(features).all():
            raise ValueError('Ungültiger Feature-Cache.')
        print('Lokaler Feature-Cache:',path.name)
        return features
    modell.backbone.eval()
    teile=[]
    # Preprocessing erfolgt batchweise, damit nicht alle 224x224-Bilder im RAM liegen.
    for start in range(0,len(bilder),batch_size):
        x=mobilenet_bilder(bilder[start:start+batch_size],modell.weights).to(DEVICE)
        teile.append(modell.backbone(x).cpu())
    features=torch.cat(teile)
    np.savez_compressed(path,features=features.numpy())
    print('Features berechnet und lokal gecacht:',features.shape)
    return features
