"""Nur laden und vorhersagen: kein Training und kein Zugriff auf Trainingsdaten."""
import json, sys
from pathlib import Path
import numpy as np
import pandas as pd
from deployment_tools import eingaben_pruefen, json_speichern

def main():
    art,ordner,input_path,output_path=sys.argv[1:]
    ordner=Path(ordner)
    daten=json.loads(Path(input_path).read_text(encoding='utf-8'))
    config=json.loads((ordner/'config.json').read_text(encoding='utf-8'))
    if art=='sklearn':
        import joblib
        # Ausschließlich selbst erzeugte, vertrauenswürdige Dateien laden.
        modell=joblib.load(ordner/'pipeline.joblib')
        x=eingaben_pruefen(pd.DataFrame(daten),config['feature_namen'])
        probs=modell.predict_proba(x)
        labels=modell.predict(x)
    elif art=='pytorch':
        import torch
        from model_code import ZiffernNetz,bilder_vorbereiten
        if torch.version.cuda is not None:raise RuntimeError('Bitte CPU-Wheels installieren.')
        torch.set_num_threads(2)
        modell=ZiffernNetz(**config['architektur']).to('cpu')
        weights=torch.load(ordner/'gewichte.pt',map_location='cpu',weights_only=True)
        modell.load_state_dict(weights,strict=True)
        modell.eval()
        x=bilder_vorbereiten(daten,config['pixel_divisor'])
        with torch.inference_mode():probs=modell(x).softmax(1).numpy()
        labels=probs.argmax(1)
    else:raise ValueError('Unbekannte Modellart')
    json_speichern(output_path,{'labels':labels.tolist(),'wahrscheinlichkeiten':probs.tolist()})
    print('Modell geladen; Vorhersagen ohne Training:',len(labels))

if __name__=='__main__':main()
