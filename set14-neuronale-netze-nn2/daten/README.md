# Daten und vortrainierte Gewichte für NN2

## Kleine handgeschriebene Ziffern

- Daten: Optical Recognition of Handwritten Digits, E. Alpaydin und C. Kaynak (1998).
- Originalquelle: https://archive.ics.uci.edu/dataset/80/optical+recognition+of+handwritten+digits
- DOI: https://doi.org/10.24432/C50P49
- Laut UCI: CC BY 4.0, kommerzielle Nutzung mit Quellenangabe möglich.
- Lizenz: https://creativecommons.org/licenses/by/4.0/
- Verwendete Auswahl: `sklearn.datasets.load_digits()`, 1797 Bilder, je 8×8 Graustufenwerte im Bereich 0–16. Laut scikit-learn eine Kopie des Testteils des UCI-Datensatzes; sie ist direkt im installierten Paket verfügbar und braucht keinen Download.
- API: https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_digits.html
- Änderungen: feste Division durch 16, Umformung nach N×1×8×8 und neuer reproduzierbarer stratifizierter Bildsplit 60/20/20. Die Schreibenden-IDs stehen in dieser Auswahl nicht zur Verfügung; deshalb wird kein Test auf unbekannte Personen behauptet.

## MobileNetV3 Small

- Architektur und vortrainierte Gewichte: torchvision, `MobileNet_V3_Small_Weights.IMAGENET1K_V1`.
- Modellreferenz: https://docs.pytorch.org/vision/stable/models/generated/torchvision.models.mobilenet_v3_small.html
- Original-Gewichtsdatei: https://download.pytorch.org/models/mobilenet_v3_small-047dcff4.pth
- Die Gewichte sind auf ImageNet vortrainiert. Sie sind keine Bestandteile des CC-BY-Zifferndatensatzes; dessen Lizenz wird nicht auf Gewichte oder ImageNet übertragen.
- Der erste Aufruf lädt die etwa 10 MB große Datei mit der Hashprüfung von torchvision nach `torch_cache/checkpoints`. Danach laufen die Beispiele mit dem lokalen Cache offline.
- Änderung für den Kurs: ImageNet-Kopf entfernt, Backbone eingefroren, neuer linearer Kopf mit zehn bzw. zwei Outputs. RGB-Umwandlung und das offizielle Gewichts-Preprocessing werden übernommen. Hochskalierung erzeugt keine neue reale Bildinformation.
- Feature-Vektoren werden lokal in `feature_cache` gespeichert. Der Cache-Schlüssel berücksichtigt Bilder, Transformation und Backbone-Zustand. Er enthält Rohfeatures ohne zielgelernte Normalisierung. Ein geänderter Kopf kann dieselben Features weiterverwenden.

Die Cacheordner sind von Git ausgeschlossen. Herkunft und API-Angaben wurden am 06.10.2026 geprüft.
