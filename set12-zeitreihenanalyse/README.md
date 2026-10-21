# Set 12 - Zeitreihenanalyse

Sechs Notebooks erklären Zeitreihen und Prognosen. Die Prognosebeispiele 03 bis 05 verwenden einfache synthetische Daten; alle Prognosefits verwenden ausschließlich `statsmodels.tsa.arima.model.ARIMA`.

| Reihenfolge | Notebook | Thema |
|---|---|---|
| 1 | `01_zeitreihen_darstellen_und_fenster_interaktiv.ipynb` | Zeitindex, Ausschnitt, Glättungsfenster, Resampling und Lücken |
| 2 | `02_trend_saisonalitaet_und_autokorrelation.ipynb` | Trend, Saison, STL, ACF/PACF und Differenzierung |
| 3 | `03_zeitlicher_split_lags_und_backtesting.ipynb` | Sinus plus Trend, kausale Lags, chronologische Folds und ARIMA-Modellwahl |
| 4 | `03b_ar_ma_und_arma.ipynb` | AR/MA/ARMA ausdrücklich mit ARIMA fitten; Schockwirkung und Sinus-Vergleich |
| 5 | `04_arima_prognosehorizont_und_unsicherheit.ipynb` | Sinus plus Trend, d=0/d=1 und expliziter Trend im Plot, Tagesmerkmale, feste/rollende Prognose und Unsicherheit |
| 6 | `05_synthetische_daten_modellvergleich.ipynb` | Sinus, Sinus plus Trend, Rauschen; vollständige Modell-, Baseline- und Testtag-Tabellen |

## Klar sichtbare Prognosen und Zahlen

`zeitreihen_demos.py` erzeugt reproduzierbare Dummy-Daten: Niveau 50, Sinusamplitude 8, Periode 24 h, optional Trend +0.08 SE/h, Rauschstandardabweichung 0.03, Seed 42. Die geringe Rauschstärke dient der Erklärung. Die Modelle erhalten keine zukünftigen Messwerte.

Ein AR-Modell ist ein ARIMA-Spezialfall mit d=q=0; MA hat p=d=0; ARMA hat d=0. Für die nahezu rauschfreie Sinus-Schwingung wird der stationäre Grenzbereich erlaubt. Sinus/Cosinus-Tagesmerkmale für ARIMA werden nur aus der Uhrzeit gebildet; Amplitude, Drift und Modellparameter werden gefittet.

Training: 01.01.–10.01.2024 (240 Stunden). Validierung: 11.01.–12.01. (48 Stunden). Test: 13.01.–15.01. (72 Stunden). Notebook 05 zeigt alle Modellfamilien und beide Baselines, getrennt nach festen 72 h und rollender 1 h. Positive Prozentwerte in den Tabellen bedeuten weniger MAE als die jeweilige Baseline. Eine Übersicht zeigt das anhand der Validierung gewählte Modell; eine weitere Tabelle zerlegt den Test in einzelne Tage.

Die Ausführung von Notebook 05 schreibt `auswertung_set12.csv` (vollständige Testtabelle mit Zeitgrenzen) und `auswertung_set12_uebersicht.csv` (kompakte Modell-/Baseline-Befunde). Die CSV-Werte entsprechen den im Notebook ausgegebenen Tabellen.

## Prognoseprotokoll und Interaktivität

- Ein fester Ursprung erhält innerhalb seines Zukunftsblocks keine neuen Messwerte. Die Vortags-Baseline wiederholt deshalb den letzten bekannten Zyklus.
- Bei der rollenden Ein-Stunden-Prognose wird erst vorhergesagt und danach die gemessene Stunde übernommen; Modellparameter bleiben fest.
- Die Kandidaten stehen vor dem Vergleich fest; Modellwahl verwendet Training/Validierung. Auch schlechtere Testresultate werden gezeigt.
- Der Horizontregler in 04 verändert nur die Anzeige der bereits erstellten Prognose. Interaktion braucht einen laufenden Jupyter-Kernel; die statischen Ausgaben sind gespeichert.

## Übungen und optionale echte Daten

Zwei Übungen und ein Fragenkatalog ergänzen das Set. Prognosefits sind auch in den Aufgaben als ARIMA vorgesehen. Die Energie-Sensorübung ist eine zusätzliche reale Anwendung. Bike- und Energiedaten bleiben offline unter `daten` verfügbar; Herkunft und Lizenz stehen in `daten/README.md`. Das frühere Bike-Hauptbeispiel 05 wurde durch den kontrollierten synthetischen Vergleich ersetzt.
