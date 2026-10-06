from pathlib import Path
import json, platform, subprocess, sys
from importlib.metadata import version
import numpy as np
import pandas as pd
ROOT=Path(__file__).resolve().parent
ARTEFAKTE=ROOT/'artefakte'
ARTEFAKTE.mkdir(exist_ok=True)

def umgebung(pakete):
    return {'python':platform.python_version(), **{p:version(p) for p in pakete}}

def json_speichern(path,inhalt):
    Path(path).write_text(json.dumps(inhalt,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

def eingaben_pruefen(frame,namen):
    if not frame.columns.is_unique or set(frame.columns)!=set(namen):
        raise ValueError('Feature-Namen passen nicht: fehlende oder zusätzliche Spalten.')
    result=frame.loc[:,namen].copy()  # Gleiche Namen in anderer Reihenfolge werden geordnet.
    if not all(pd.api.types.is_numeric_dtype(t) for t in result.dtypes):
        raise ValueError('Alle Features müssen numerisch sein.')
    if not np.isfinite(result.to_numpy()).all():
        raise ValueError('Eingaben enthalten NaN oder unendliche Werte.')
    return result

def neuer_prozess(art,ordner,eingaben):
    input_path=ordner/'eingaben.json';output_path=ordner/'vorhersagen_neuer_prozess.json'
    json_speichern(input_path,eingaben)
    result=subprocess.run([sys.executable,str(ROOT/'predict.py'),art,str(ordner),str(input_path),str(output_path)],
                          cwd=ROOT,capture_output=True,text=True,timeout=180)
    if result.returncode:
        raise RuntimeError(result.stderr)
    print('Neuer Python-Prozess:',result.stdout.strip())
    return json.loads(output_path.read_text(encoding='utf-8'))
