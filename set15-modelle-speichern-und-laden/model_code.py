"""Architektur für den separat gespeicherten PyTorch-state_dict."""
import torch
from torch import nn

class ZiffernNetz(nn.Module):
    def __init__(self,hidden=32,klassen=10):
        super().__init__()
        self.net=nn.Sequential(nn.Flatten(),nn.Linear(64,hidden),nn.ReLU(),nn.Dropout(0.1),nn.Linear(hidden,klassen))
    def forward(self,x):
        return self.net(x)

def bilder_vorbereiten(bilder,divisor=16.0):
    x=torch.as_tensor(bilder,dtype=torch.float32)
    if x.ndim!=3 or tuple(x.shape[1:])!=(8,8) or len(x)==0:
        raise ValueError('Erwartet wird ein nichtleeres Batch N × 8 × 8.')
    if not torch.isfinite(x).all() or x.min()<0 or x.max()>divisor:
        raise ValueError('Pixel müssen endlich und im Bereich 0–16 sein.')
    return (x/divisor).unsqueeze(1)
