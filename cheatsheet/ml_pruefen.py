"""Führt die Rezepte mit der Kursumgebung aus und speichert echte Ausgaben."""
from pathlib import Path
import argparse, contextlib, io, json, traceback, time
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from ml_inhalte import PAGES, COMMON

parser = argparse.ArgumentParser()
parser.add_argument('--output', required=True)
args = parser.parse_args()
out = Path(args.output)
out.mkdir(parents=True, exist_ok=True)
ns = {'__name__': '__main__'}
exec(COMMON, ns)
plt.rcParams.update({'font.size': 9, 'axes.spines.top': False,
                     'axes.spines.right': False, 'figure.dpi': 150})
plt.show = lambda *a, **k: None
results = {}
for n, page in enumerate(PAGES, 1):
    if not page['code'] or not page['run']:
        continue
    buf = io.StringIO()
    start = time.time()
    try:
        with contextlib.redirect_stdout(buf):
            exec(page['setup'], ns)
            exec(compile(page['code'], f'CheatSheet Seite {n}', 'exec'), ns)
        figures = []
        for i, fnum in enumerate(plt.get_fignums()):
            path = out / f'figure-{n:02}-{i}.png'
            plt.figure(fnum).savefig(path, dpi=160, bbox_inches='tight')
            figures.append(str(path))
        results[str(n)] = {'text': buf.getvalue(), 'figures': figures}
        print(f'{n:02} OK {time.time()-start:.1f}s {page["title"]}', flush=True)
    except Exception:
        results[str(n)] = {'text': buf.getvalue(), 'error': traceback.format_exc()}
        print(results[str(n)]['error'], flush=True)
        (out/'results.json').write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding='utf-8')
        raise
    finally:
        plt.close('all')
    (out/'results.json').write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding='utf-8')
import sklearn, numpy, pandas
versions = {'scikit-learn': sklearn.__version__, 'numpy': numpy.__version__,
            'pandas': pandas.__version__}
(out/'versions.json').write_text(json.dumps(versions, indent=2), encoding='utf-8')
print('Alle ausführbaren Rezepte erfolgreich geprüft.', flush=True)
