# Echte Zeitreihendaten - Quellen und Nutzung

Die Dateien liegen lokal, damit Set 12 offline funktioniert. Die UCI-Quellseiten wurden am 06.10.2026 geprüft. Beide Datensätze sind dort unter **CC BY 4.0** ausgewiesen. Diese Lizenz erlaubt kommerzielle Nutzung, Bearbeitung und Weitergabe mit geeigneter Quellen-/Urheberangabe, Lizenzlink und Kennzeichnung von Änderungen.

Lizenz: https://creativecommons.org/licenses/by/4.0/

## Bike Sharing

- Urheber/Datensatz: Hadi Fanaee-T (2013), Bike Sharing, UCI Machine Learning Repository.
- DOI: https://doi.org/10.24432/C5W894
- Quelle: https://archive.ics.uci.edu/dataset/275/bike+sharing+dataset
- Lokal: `bike_day.csv`, 731 tägliche Einträge von 01.01.2011 bis 31.12.2012.
- Änderung: Original `day.csv` unverändert übernommen und lediglich umbenannt; keine Zeilen/Spalten verändert.
- Ziel im Beispiel: `cnt`, Anzahl täglicher Ausleihen. `casual` und `registered` sind Zielbestandteile und werden nicht als Features genutzt. Tageswetterwerte werden nicht als vorab bekannte Forecast-Eingaben behandelt.

## Appliances Energy Prediction

- Urheber/Datensatz: Luis Candanedo (2017), Appliances Energy Prediction, UCI Machine Learning Repository.
- DOI: https://doi.org/10.24432/C5VC8G
- Quelle: https://archive.ics.uci.edu/dataset/374/appliances+energy+prediction
- Lokal: `energie_sensoren.csv`, 19.735 Einträge im 10-Minuten-Raster.
- Änderung: Nur `date`, `Appliances`, `T1`, `RH_1` aus `energydata_complete.csv` ausgewählt; alle Zeilen und Originalwerte beibehalten. CSV wurde mit UTF-8 neu geschrieben.
- Messgrößen: Geräteenergie `Appliances` in Wh, Küchentemperatur `T1` in Grad Celsius und relative Luftfeuchte `RH_1` in Prozent. Die vier Spalten stammen aus Messungen; die Wetter- und Zufallsspalten des Originaldatensatzes sind nicht Teil dieser Auswahl.
- In Übung 2 werden rechts geschlossene Stundenintervalle mit Endlabel gebildet: Energie summieren, Temperatur/Feuchte mitteln. Nur Stunden mit sechs 10-Minuten-Einträgen werden verwendet. Diese Aggregation ist eine weitere im Notebook dokumentierte Änderung.

## Reproduzierbarer Bezug

`download_daten.py` bezieht die beiden UCI-Originalarchive, prüft deren dokumentierte SHA-256 und erzeugt die Offline-Dateien erneut. Aufruf vom Repository aus:

```powershell
.venv\Scripts\python.exe set12-zeitreihenanalyse/daten/download_daten.py
```

`quellen_manifest.json` enthält Original-URLs, Lizenz, Archiv- und lokale Dateihashes sowie die Änderungen. Der Bezug braucht Internet; die Notebooks selbst benötigen keines.
