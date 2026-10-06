# Set 12 - Zeitreihenanalyse

Fünf Beispiele führen von Darstellung und Fensterwahl zur Prognose auf echten Daten. Danach folgen zwei Übungen und ein Fragenkatalog mit 25 Fragen. Alle Notebooks sind mit Python 3.11+ und den Abhängigkeiten aus dem Haupt-`requirements.txt` ausführbar.

| Reihenfolge | Notebook | Thema |
|---|---|---|
| 1 | `01_zeitreihen_darstellen_und_fenster_interaktiv.ipynb` | Übersicht/Detail, Bereichs- und Fensterregler, kausale vs. zentrierte Glättung, Resampling und Lücken |
| 2 | `02_trend_saisonalitaet_und_autokorrelation.ipynb` | STL, ACF/PACF, Lag-Regler, Differenzierung und ADF-Test |
| 3 | `03_zeitlicher_split_lags_und_backtesting.ipynb` | Prognoseauftrag, kausale Lags, Expanding/Sliding Window, Pipeline, Baselines und finaler Test |
| 4 | `04_arima_prognosehorizont_und_unsicherheit.ipynb` | Kleine ARIMA-Modellwahl, Horizontregler, Prognoseintervalle, fester Ursprung vs. rollende Prognose |
| 5 | `05_echte_daten_bike_sharing_prognose.ipynb` | Tägliche Fahrrad-Ausleihen, chronologische Validierung, Baselines und Testfehler |

Die Beispiele 1-4 verwenden reproduzierbare generierte Sensorreihen; Beispiel 5 verwendet echte Ausleihdaten. Die beiden Übungen behandeln Fenster/Backtesting auf synthetischen Daten und eine stündliche Energieprognose aus echten 10-Minuten-Sensormessungen. Lokale Musterlösungen liegen in `uebungen/loesungen` und bleiben wie in den anderen Sets von Git ausgeschlossen.

## Darstellung und Interaktivität

Die Diagramme verwenden kompakte Datumsachsen, Einheiten, markierte Zeitbereiche und Überblick/Detail. Die Regler ändern Anzeigeausschnitt, Fensterbreite, Zentrierung, Lag und Prognosehorizont. Gespeicherte statische Vorschauen sind sofort lesbar. Für Änderungen an Reglern müssen die Zellen in JupyterLab mit laufendem Kernel ausgeführt werden; gespeicherter Widget-Zustand allein führt keine neue Berechnung durch.

## Methodischer Rahmen

- Vor dem Modellieren sind Ursprung, Horizont und verfügbare Informationen definiert.
- Zeitgrenzen werden vor der Trainingsanalyse festgelegt. Modellwahl nutzt Training/Validierung; Testwerte werden erst zur finalen Bewertung betrachtet.
- Lag-/Rollmerkmale schauen nur zurück. Kalendermerkmale sind vorab bekannt. Gelernte Skalierung bleibt in der Pipeline bzw. im Trainingsfold.
- Rollende Ein-Schritt-Vorhersagen dürfen inzwischen eingetroffene frühere Testmessungen nutzen. Ein Mehr-Schritt-Forecast mit festem Ursprung darf dies nicht.
- Die PDF `ML_Set_01_04.pdf` behandelt allgemeine Datenanalyse und Splits, darunter den chronologischen Split auf Seite 24. Sie liefert das Prinzip für dieses zusätzliche Zeitreihenset; STL/ARIMA sind die hier ergänzten Methoden.

## Echte Daten und Quellen

Die beiden kleinen Datenauswahlen liegen unter `daten` und sind laut UCI unter CC BY 4.0 kommerziell nutzbar mit Quellenangabe. Details, Änderungen, Lizenzlinks und Herkunft stehen in `daten/README.md` und `daten/quellen_manifest.json`. Beide Praxisaufgaben funktionieren offline.
