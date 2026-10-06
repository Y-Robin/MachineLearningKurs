# Set 15 – Modelle speichern, laden und anwenden

Drei kurze Beispiele zur PDF `ML_Set_04_01.pdf` (Bereitstellung von ML-Modellen). Schwerpunkt sind lokale Modelldateien und Inference; alle Beispiele starten einen neuen Python-Prozess und vergleichen dessen Vorhersagen mit dem trainierten Modell.

| Notebook | Inhalt |
|---|---|
| `01_sklearn_pipeline_speichern_und_laden.ipynb` | Iris, StandardScaler + LogisticRegression, joblib, Feature-Struktur, JSON-Konfiguration und Versionsangaben |
| `02_sklearn_eigener_transformer_und_modellpaket.ipynb` | Eigener Transformer im importierbaren Python-Modul, Modellpaket und Laden außerhalb der Notebook-Sitzung |
| `03_pytorch_gewichte_speichern_und_laden_cpu.ipynb` | Kleine Ziffernerkennung, state_dict, Architektur/Preprocessing, CPU-Laden, eval und inference_mode |

18 Übungsfragen stehen in `uebungen/01_fragen_modelle_speichern_und_laden.ipynb`. Die lokalen Musterantworten befinden sich wie bisher in `uebungen/loesungen`.

## Installation und Ausführung

Die ersten beiden Beispiele verwenden die normalen Kursabhängigkeiten. Für das PyTorch-Beispiel zusätzlich die CPU-Abhängigkeiten aus NN2 installieren:

```powershell
.venv\Scripts\python.exe -m pip install -r requirements.txt
.venv\Scripts\python.exe -m pip install -r requirements-cpu.txt
```

Jedes Beispiel ist unabhängig ausführbar, trainiert ein kleines Modell selbst und speichert Dateien unter `artefakte/`. Es benötigt weder Daten- noch Gewichtsdownloads. Die Notebooks enthalten gespeicherte Ausgaben. Der Inference-Unterprozess verwendet dasselbe Python wie der Notebook-Kernel.

Die Artefakte bleiben lokal und werden nicht von Git erfasst; durch erneutes Ausführen werden sie reproduziert. `predict.py` zeigt die Anwendung ohne Training. Zum Weitergeben gehören die betreffenden Artefakte **und** `predict.py`, `deployment_tools.py` sowie bei Bedarf `custom_transformer.py` bzw. `model_code.py` zusammen. Die JSON-Versionsdatei dokumentiert die tatsächlich verwendeten Bibliotheken; sie installiert oder erzwingt deren Versionen nicht automatisch.

Die Joblib-Beispiele laden ausschließlich selbst erzeugte Dateien. Versionsübergreifendes Laden in scikit-learn wird nicht unterstützt. Bei PyTorch werden CPU-Wheels, `weights_only=True`, `map_location="cpu"` und `strict=True` verwendet.

## Bezug zur Vorlage und Quellen

PDF: Grundlagen/Preprocessing auf Seiten 3–6, eigener Code und Umgebung auf Seiten 7–8, PyTorch auf Seite 9, Inference/Anwendung auf Seiten 12–15. ONNX, APIs, Container und Edge-Optimierung werden im Fragenkatalog aufgegriffen; dafür werden keine zusätzlichen Bibliotheken oder Server benötigt.

- [scikit-learn: Model persistence](https://scikit-learn.org/stable/model_persistence.html)
- [PyTorch: Saving and Loading Models](https://docs.pytorch.org/tutorials/beginner/saving_loading_models.html)
- Die Zifferndaten entsprechen der kleinen scikit-learn-Auswahl aus NN2; Herkunft und Lizenz sind in `../set14-neuronale-netze-nn2/daten/README.md` dokumentiert. Iris wird direkt mit `sklearn.datasets.load_iris` geladen.
