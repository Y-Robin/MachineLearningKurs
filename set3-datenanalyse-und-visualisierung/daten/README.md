# Datenquellen und Lizenzen

Die CSV-Dateien liegen lokal vor, damit die Notebooks offline funktionieren.

## Palmer Penguins

- Datei: palmer_penguins.csv
- Quelle: Allison Horst, Alison Hill und Kristen Gorman
- Projekt: https://github.com/allisonhorst/palmerpenguins
- Lizenz: CC0 1.0; kommerzielle Nutzung erlaubt

## Wine Quality - Red Wine

- Datei: wine_quality_red.csv
- Quelle: Cortez, Cerdeira, Almeida, Matos und Reis; UCI Machine Learning Repository
- DOI: https://doi.org/10.24432/C56S3T
- Lizenz: CC BY 4.0; kommerzielle Nutzung mit Quellenangabe erlaubt

## AI4I 2020 Predictive Maintenance

- Datei: ai4i_predictive_maintenance.csv
- Quelle: Stephan Matzka; UCI Machine Learning Repository
- DOI: https://doi.org/10.24432/C5HS5C
- Lizenz: CC BY 4.0; kommerzielle Nutzung mit Quellenangabe erlaubt

Eine offene Lizenz garantiert weder Datenqualität noch Eignung für einen bestimmten Zweck.

## CWRU Bearing Data Center – echte Vibrationssignale

Für die Notebooks 05 und 06 werden vier Originalaufnahmen direkt von der Case Western Reserve University geladen. Die MATLAB-Dateien werden lokal in `cwru/` gecacht und nicht im Repository verteilt. Der erste Lauf braucht Internet, weitere Läufe funktionieren offline. Die Abhängigkeiten NumPy, pandas, SciPy, Matplotlib und scikit-learn sind bereits in `requirements.txt` enthalten.

- Originalquelle und Übersicht: https://engineering.case.edu/bearingdatacenter/welcome
- Versuchsaufbau: https://engineering.case.edu/bearingdatacenter/apparatus-and-procedures
- Dateiformat/Kanäle: https://engineering.case.edu/bearingdatacenter/download-data-file
- Gesunde Referenz: https://engineering.case.edu/bearingdatacenter/normal-baseline-data
- Fehleraufnahmen: https://engineering.case.edu/bearingdatacenter/48k-drive-end-bearing-fault-data
- Abruf der Quellseiten geprüft am 06.10.2026.

| Datei | Zustand | Kanal / Abtastrate | Last | Schaden |
|---|---|---|---|---|
| 97.mat | gesund | DE / 48 kHz | 0 HP | keiner |
| 109.mat | Innenring | DE / 48 kHz | 0 HP | 0,007 Zoll |
| 122.mat | Kugel | DE / 48 kHz | 0 HP | 0,007 Zoll |
| 135.mat | Außenring | DE / 48 kHz | 0 HP | 0,007 Zoll, 6-Uhr-Position |

Direktlinks folgen dem Schema `https://engineering.case.edu/sites/default/files/97.mat` (Dateinummer ersetzen). Bei einem Downloadfehler nennt die Hilfsdatei den konkreten Link und den lokalen Zielpfad für den manuellen Download. Dateien werden vor dem Speichern auf einen lesbaren DE-Kanal geprüft. Die beim Laden erzeugte Metadatentabelle enthält URL, Samplezahl, Drehzahl und SHA-256 des tatsächlich verwendeten Originals. Die gesunde DE-Referenz 97 wird mit 48 kHz ausgewertet; andere Kanäle oder Datenserien dürfen nicht ohne Prüfung mit derselben Abtastrate interpretiert werden.

Die Beschleunigungssignale wurden real gemessen, die Lagerfehler im Labor per EDM künstlich erzeugt. Die Drehzahl liegt ungefähr bei 1797 U/min; wo vorhanden wird der RPM-Wert aus der Datei genutzt, sonst der Tabellenwert. Es gibt keine markierten Produktionszyklen: Umdrehungsfenster sind aus der mittleren Drehzahl geschätzt und nicht phasensynchron. Die FFT-Features werden aus längeren, nicht überlappenden 8192-Sample-Fenstern gebildet. Je Aufnahme werden für die EDA gleich viele Fenster verwendet.

**Nutzung/Quellenangabe:** In den verlinkten CWRU-Quellseiten ist keine ausdrückliche offene Datenlizenz angegeben. Deshalb wird hier keine CC-Lizenz behauptet. Als Ursprung nennen: Case Western Reserve University Bearing Data Center, mit Link auf die Originalquelle. Ein öffentlich verfügbarer Download ist keine dokumentierte pauschale Weiterverteilungserlaubnis; im Repository verbleiben nur Downloadcode und Quellenangaben.

**Didaktische Grenze:** Nur eine Aufnahme je Zustand. Fenster derselben Aufnahme sind abhängig. Diese Auswahl illustriert Feature Engineering und PCA, nicht eine belastbare Modellbewertung auf unbekannten Lagern. Bei späterem Modelltraining nach Aufnahme/Lager trennen und Skalierer/PCA nur auf Training fitten.
