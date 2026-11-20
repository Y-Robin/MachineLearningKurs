# Set 12: Zeitreihen

## Einfach anfangen: Beispiel 00, Übung 00, Lösung 00

Wenn ARMA und ARIMA noch neu sind, mit diesen Materialien beginnen:

1. [Beispiel 00: ARMA und ARIMA ganz einfach](00_arma_arima_ganz_einfach.ipynb)
   erklärt eine ruhige Sinuswelle, einen Anstieg sowie Anstieg plus Sinus und Rauschen.
   Die Modelle sagen jeweils 40 Tage vorher.
2. [Übung 00](uebungen/00_uebung_arma_arima_einfach.ipynb)
   enthält sechs Aufgaben mit vorgegebenen Daten und Modellparametern.
3. [Lösung 00](uebungen/loesungen/00_loesung_arma_arima_einfach.ipynb)
   enthält vollständigen Code, Diagramme und Antworten.
4. [Fragenkatalog](uebungen/03_fragen_zeitreihen.ipynb)
   enthält 25 einfache Fragen mit Schwerpunkt ARMA und ARIMA.
   [Musterantworten](uebungen/loesungen/03_loesungen_fragen_zeitreihen.ipynb).

Als Ergänzung zu Beispiel 00 zeigt
[Beispiel 00_b: ARMA mit externen Merkmalen](00_b_arma_mit_externen_merkmalen.ipynb),
wie ein bekannter Produktionsplan die Verbrauchsprognose verbessert.
Es vergleicht dieselben 40 Tage ohne und mit `exog` und erklärt,
welche Merkmale beim Fitten und für die Zukunft übergeben werden müssen.

[Beispiel 00_c: Schrittweise ARMA und lineare Regression](00_c_schrittweise_arma_und_regression.ipynb)
führt die ersten zwei Tagesprognosen einzeln vor und wiederholt den Ablauf anschließend
in einer Schleife: vorhersagen, echten Wert beobachten, Zustand mit `append(..., refit=False)`
aktualisieren. Eine feste 40-Tage-Prognose und eine lineare Regression mit demselben
Produktionsplan dienen als Vergleich. Ein vergrößerter Plot zeigt die kleinen Schwankungen.

Die neuen Notebooks funktionieren eigenständig. Jeweils einen Python-Kernel
starten und die Zellen von oben nach unten ausführen. Die Übung enthält bewusst
noch auszufüllende Codezellen. Beispiel und Lösung enthalten gespeicherte Ausgaben.
Benötigt werden NumPy, pandas, matplotlib, IPython und statsmodels aus der Kursumgebung.

Der neue Einstieg verwendet die Modellklasse `statsmodels.tsa.arima.model.ARIMA`
direkt. ARMA wird mit `d=0` geschätzt. Bei der steigenden Reihe erlaubt `trend="t"`
zusammen mit `d=1` einen gelernten mittleren Anstieg. Alle Prognosen entstehen
am Ende des Trainings, ohne spätere Messwerte nachzureichen.

## Danach vertiefen

- **01:** Zeitachse, Ausschnitte, Glättung und Resampling.
- **02:** Trend, Saisonalität, ACF/PACF und Differenzierung.
- **03b:** AR-, MA- und ARMA-Mechanismen genauer verstehen.
- **03:** Zeitliche Aufteilung und Backtesting.
- **04:** ARIMA, Prognosehorizont und Unsicherheit.
- **05:** Mehrere Modelle auf unterschiedlichen künstlichen Daten vergleichen.

Die bisherigen Übungen 01 und 02 sind weiterführend. Für den ersten Einstieg
reichen Beispiel 00 und Übung 00 aus.
