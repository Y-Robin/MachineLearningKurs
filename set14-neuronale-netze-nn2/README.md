# Set 14 – Kurzes Intro: Bilder, PyTorch und CNNs

**Leitfrage: Wie wird aus einem Bild eine vorhergesagte Ziffer?**
Voraussetzung ist das MLP aus Set 13. Der Kern dauert etwa **35 Minuten**;
mit Miniübung etwa 40–45 Minuten. Zeiten sind Richtwerte für die Erklärung.

## Der Weg durch die Stunde

| Reihenfolge | Notebook | Inhalt | Richtzeit |
|---|---|---|---|
| 1 | [Vom Bild zur Vorhersage](01_pytorch_ziffern_und_pixel.ipynb) | Pixel, Tensorform, MLP, fünf Trainingsschritte, Test | 20 Min. |
| 2 | [Was macht ein CNN anders?](02_cnn_filter_pooling_und_feature_maps.ipynb) | Filter, ReLU, Max-Pooling, kleines CNN, gelernte Antwort | 15 Min. |
| 3 | [Miniübung](uebungen/01_uebung_kleines_cnn.ipynb) | Formen, Pooling von Hand, zwei Filter | 5–10 Min. |

**Hier endet das Intro.** [Notebook 03](03_transfer_learning_nur_der_kopf.ipynb)
ist ein optionaler Ausblick für weitere 10–15 Minuten plus ersten Download.
Es zeigt einen eingefrorenen MobileNet-Backbone und einen neuen Kopf für Ziffer 2 gegen 3.
Die zweite Übung und die letzten zwei Kurzfragen sind ebenfalls optional.

## Aufbau und Durchführung

Jedes Notebook läuft eigenständig von oben nach unten. Daten laden, aufteilen,
Netz definieren, trainieren und auswerten stehen direkt in den Zellen.
Die Trainingsschleife wiederholt sichtbar: Gradienten löschen → Vorhersage →
Loss → Gradienten berechnen → Gewichte ändern.

Es gibt keine Imports aus `cv_tools.py`, keine eigenen Modellklassen und keine
versteckten Trainingsfunktionen. Bekannte Schritte werden bewusst wiederholt.
Die alte Hilfsdatei bleibt für frühere Kopien erhalten; die neuen Materialien
benötigen sie nicht.

Architektur und Epochenzahl sind vorab festgelegt. 80 % der Bilder dienen dem
Training, 20 % dem abschließenden Test. Es findet keine Modellwahl am Test statt.
Für Hyperparametervergleiche sind zusätzliche Validierungsdaten aus dem
Trainingsanteil nötig. Ein Bildsplit belegt keine Generalisierung auf unbekannte
schreibende Personen.

## Installation

Eine vorhandene PyTorch-Installation mit CUDA-Unterstützung kann ebenfalls
verwendet werden. Sie muss nicht durch CPU-Wheels ersetzt werden. Die Beispiele
rechnen weiterhin auf der CPU. Das Colab-Setup übernimmt vorhandenes PyTorch
und torchvision und installiert CPU-Pakete nur, wenn PyTorch fehlt.

Im Hauptordner des Kurses unter Windows:

```powershell
.venv/Scripts/python.exe -m pip install -r requirements.txt
.venv/Scripts/python.exe -m pip install -r requirements-cpu.txt
```

In Jupyter/VS Code diesen Python-Kernel auswählen. Alle Modelle und Tensoren
bleiben auf der CPU. Die ersten beiden Notebooks benötigen kein torchvision
und keinen Download. Die Ziffern sind in scikit-learn enthalten.
Für einen frischen Trainingslauf den Kernel neu starten und alle Zellen ausführen.

Der optionale Ausblick benötigt torchvision und einmalig die MobileNet-Gewichte.
Er wird aus dem Kurs-Hauptordner oder direkt aus dem Set-14-Ordner gestartet.
Gewichte liegen danach in `daten/torch_cache`; Features bleiben nur im Arbeitsspeicher.

## Übungen und Quellen

- Übung 01 vertieft den CNN-Aufbau ohne weiteres Modelltraining.
- Übung 02 fragt optional den sichtbaren Transfer-Ablauf ab.
- Der Fragenkatalog enthält sechs Kernfragen und zwei optionale Fragen.
- Passende Musterlösungen liegen lokal in `uebungen/loesungen` und bleiben von Git ausgeschlossen.
- Daten- und Gewichtsquellen: [daten/README.md](daten/README.md).

Die Beispiele klassifizieren eine bereits ausgeschnittene Ziffer pro Bild.
Objekterkennung mit Bounding Boxes gehört nicht zu diesem Intro.

## Frühere Fragen und Antworten

Die [ursprünglichen 20 Fragen](uebungen/03_fragen_computer_vision_alt.ipynb) und ihre [alten Musterantworten](uebungen/loesungen/03_loesungen_fragen_computer_vision_alt.ipynb) sind zusätzlich verfügbar. Sie beziehen sich auf den früheren, ausführlicheren Ablauf. Die neuen Kurzfragen und Lösungen bleiben unverändert.
