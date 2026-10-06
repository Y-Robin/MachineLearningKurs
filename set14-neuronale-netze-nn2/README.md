# Set 14 - NN2: Computer Vision mit PyTorch (CPU)

NN2 ergänzt NN1 / Set 13. Drei überschaubare Beispiele führen von Pixeln zum CNN und zur Übertragung eines vortrainierten Vision-Backbones. Dazu kommen zwei kurze Übungen, lokale Musterlösungen und ein Fragenkatalog mit 20 Fragen.

| Beispiel | Inhalt |
|---|---|
| `01_pytorch_ziffern_und_pixel.ipynb` | Bilder/Tensorformen, kleines MLP, Trainingsschritt, Lernkurven, Confusion Matrix, Ziffern-/Rausch-/Verschiebungsregler |
| `02_cnn_filter_pooling_und_feature_maps.ipynb` | Handgewählte Kantenfilter, Max-/Average-Pooling, kleines CNN, gelernte Filter und interaktive Feature Maps |
| `03_transfer_learning_nur_der_kopf.ipynb` | MobileNetV3 Small, eingefrorener Backbone, offizielles Preprocessing, Feature-Cache und ausschließlich neuer Kopf |

## CPU-Installation

Die Basispakete bleiben im Haupt-`requirements.txt`. PyTorch wird separat vom offiziellen **CPU-Wheel-Index** installiert, damit keine CUDA-Wheels aus einer allgemeinen Installation ausgewählt werden:

```powershell
.venv\Scripts\python.exe -m pip install -r requirements.txt
.venv\Scripts\python.exe -m pip install -r requirements-cpu.txt
```

Die CPU-Datei fixiert die zusammenpassenden getesteten Versionen torch 2.14.1+cpu und torchvision 0.29.1+cpu für Windows/Linux. Alle Beispiele erzwingen `torch.device("cpu")` und prüfen `torch.version.cuda is None`. Es sind keine GPU, kein CUDA-Toolkit und kein torchaudio nötig. Kleine Modelle, zwei CPU-Threads und `DataLoader(num_workers=0)` halten den Einstieg einfach.

## Daten und Laufzeit

Die echten 8×8-Ziffernbilder kommen aus dem bereits installierten scikit-learn-Paket. Wir verwenden diese kleinen Daten statt MNIST, um Download und Trainingszeit niedrig zu halten. Die Bildbeispiele 1/2 laufen offline. MobileNet braucht einmalig etwa 10 MB vortrainierte Gewichte; danach bleiben Gewichte und Features lokal gecacht. Die einmalige Feature-Extraction dauert auf CPU länger als das anschließende Kopftraining.

Die normalen Trainingsbeispiele verwenden getrennte Trainings-/Validierungs-/Testbilder. Der Helfer speichert den Zustand mit dem kleinsten Validierungs-Loss. Der Test ist nicht zur Auswahl von Architektur oder Epoche vorgesehen. Im Transfer-Beispiel werden zusätzlich unveränderte Backbone-Gewichte und BatchNorm-Puffer über einen Hash geprüft.

Alle Notebooks erhalten gespeicherte Outputs. Interaktive Regler benötigen zur Neuberechnung einen laufenden Jupyter-Kernel. Statische Vorschaudiagramme sind auch ohne diesen sichtbar.

## Bezug zur PDF

`ML_Set_03_05.pdf`: Bildfilter und CNN-Bausteine auf Seiten 4–6, Klassifikation vs. Objekterkennung auf Seiten 7–8 und Pretraining/Transfer Learning auf Seite 26. Die Beispiele klassifizieren ausgeschnittene Ziffern; eine Bounding-Box-Detektion ist nicht Teil dieser einfachen Übungen. Die weiteren PDF-Themen NLP, Foundation Models und Generative AI sind hier nicht als zusätzliche Aufgaben eingefügt.

Quellen und Daten-/Gewichtshinweise: `daten/README.md`. Musterlösungen bleiben wie in den anderen Sets lokal in `uebungen/loesungen` und werden nicht von Git erfasst.
