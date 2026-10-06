# Machine-Learning-Kurs – Codebeispiele

Dieses Repository entsteht Schritt für Schritt zusammen mit dem Kurs. Die Inhalte sind in **Sets** gegliedert. Jedes Thema wird als Jupyter Notebook erklärt und enthält ausführbare Beispiele sowie kleine Übungen.

## Aktueller Inhalt

```text
.
├── README.md
├── requirements.txt
├── requirements-cpu.txt
├── set1-python-grundlagen/
│   ├── 01_python_setup_und_bibliotheken.ipynb
│   ├── 02_python_und_numpy_basics.ipynb
│   └── uebungen/
│       ├── 01_uebungen_python_setup.ipynb
│       ├── 02_uebungen_python_numpy.ipynb
│       └── loesungen/
├── set2-ml-grundlagen/
│   └── uebungen/
│       ├── 01_fragenkatalog_ml_grundlagen.ipynb
│       ├── 02_fallstudien_methodenwahl.ipynb
│       └── loesungen/
├── set3-datenanalyse-und-visualisierung/
│   ├── 01_pandas_basics.ipynb
│   ├── 02_eda_palmer_penguins.ipynb
│   ├── 03_eda_wine_quality.ipynb
│   ├── 04_eda_predictive_maintenance.ipynb
│   ├── 05_sensor_signale_fft_features.ipynb
│   ├── 06_pca_sensor_features.ipynb
│   ├── sensor_features.py
│   ├── daten/
│   │   ├── palmer_penguins.csv
│   │   ├── wine_quality_red.csv
│   │   ├── ai4i_predictive_maintenance.csv
│   │   └── README.md
│   └── uebungen/
│       ├── 01_uebungen_pandas.ipynb
│       ├── 02_fragen_datenanalyse_visualisierung.ipynb
│       ├── 03_programmieruebungen_eda.ipynb
│       └── loesungen/
├── set4-machine-learning-mit-scikit-learn/
│   ├── 01_daten_verstehen_und_visualisieren.ipynb
│   ├── 02_sklearn_transformer_basics.ipynb
│   ├── 03_preprocessing_mit_pipeline.ipynb
│   └── uebungen/
│       ├── 01_uebungen_datenanalyse.ipynb
│       ├── 02_fragen_preprocessing_pipeline.ipynb
│       ├── 03_programmieruebungen_preprocessing.ipynb
│       └── loesungen/
├── set5-lineare-und-logistische-regression/
│   ├── 01_lineare_regression.ipynb
│   ├── 02_m_und_b_interaktiv.ipynb
│   ├── 03_logistische_regression.ipynb
│   ├── 04_pipeline_palmer_penguins.ipynb
│   ├── 05_xai_koeffizienten.ipynb
│   ├── daten/
│   │   └── README.md
│   └── uebungen/
│       ├── 01_uebungen_lineare_regression.ipynb
│       ├── 02_uebungen_logistische_regression.ipynb
│       ├── 03_uebungen_breast_cancer_xai.ipynb
│       ├── 04_fragen_regression_klassifikation.ipynb
│       └── loesungen/
├── set6-bias-varianz-und-regularisierung/
│   ├── 01_bias_varianz_polynom_interaktiv.ipynb
│   ├── 02_regularisierung_l1_l2.ipynb
│   ├── 03_hyperparameter_tuning_regression.ipynb
│   └── uebungen/
│       ├── 01_projekt_optimale_regression.ipynb
│       ├── 02_fragen_bias_varianz_regularisierung.ipynb
│       └── loesungen/
├── set7-naive-bayes-und-textklassifikation/
│   ├── 01_gaussian_naive_bayes.ipynb
│   ├── 02_naive_bayes_vs_logistische_regression.ipynb
│   ├── 03_textmerkmale_multinomial_naive_bayes.ipynb
│   ├── daten/
│   │   ├── SMSSpamCollection
│   │   └── README.md
│   └── uebungen/
│       ├── 01_projekt_sms_spamklassifikation.ipynb
│       ├── 02_fragen_naive_bayes_textklassifikation.ipynb
│       └── loesungen/
├── set8-entscheidungsbaeume-und-ensembles/
│   ├── 01_entscheidungsbaum_klassifikation.ipynb
│   ├── 02_entscheidungsbaum_regression.ipynb
│   ├── 03_random_forest.ipynb
│   ├── 04_gradient_boosting_und_modellvergleich.ipynb
│   ├── daten/
│   │   ├── banknote_authentication.csv
│   │   └── README.md
│   └── uebungen/
│       ├── 01_entscheidungsbaum_banknoten.ipynb
│       ├── 02_random_forest_banknoten.ipynb
│       ├── 03_gradient_boosting_banknoten.ipynb
│       ├── 04_vergleich_und_fragen.ipynb
│       └── loesungen/
├── set9-knn-und-dimensionen/
│   ├── 01_knn_pipeline_klassifikation.ipynb
│   ├── 02_curse_of_dimensionality.ipynb
│   ├── 03_distanzen_gewichtung_und_regression.ipynb
│   ├── daten/
│   │   ├── wdbc.csv
│   │   └── README.md
│   └── uebungen/
│       ├── 01_projekt_knn_wdbc.ipynb
│       ├── 02_fragen_knn.ipynb
│       └── loesungen/
├── exkurs-conditional-random-fields/
│   ├── 01_crf_score_forward_viterbi.ipynb
│   └── uebungen/
│       ├── 01_miniuebung_crf.ipynb
│       └── loesungen/
├── set10-support-vector-machines/
│   ├── 01_svm_klassifikation.ipynb
│   ├── 02_svm_regression.ipynb
│   └── uebungen/
│       ├── 01_uebung_svm_klassifikation.ipynb
│       ├── 02_uebung_svm_regression.ipynb
│       ├── 03_fragen_svm.ipynb
│       └── loesungen/
├── set11-unueberwachtes-lernen/
│   ├── 01_pca_und_merkmalsreduktion.ipynb
│   ├── 02_nmf_und_tsne.ipynb
│   ├── 03_kmeans_und_clusterbewertung.ipynb
│   ├── 04_hierarchisch_dbscan_und_gmm.ipynb
│   ├── 05_anomalieerkennung_und_thresholds.ipynb
│   └── uebungen/
│       ├── 01_uebung_pca_und_feature_reduction.ipynb
│       ├── 02_uebung_clustering.ipynb
│       ├── 03_uebung_anomalie_threshold.ipynb
│       ├── 04_fragen_unueberwachtes_lernen.ipynb
│       └── loesungen/
├── set12-zeitreihenanalyse/
│   ├── 01_zeitreihen_darstellen_und_fenster_interaktiv.ipynb
│   ├── 02_trend_saisonalitaet_und_autokorrelation.ipynb
│   ├── 03_zeitlicher_split_lags_und_backtesting.ipynb
│   ├── 04_arima_prognosehorizont_und_unsicherheit.ipynb
│   ├── 05_echte_daten_bike_sharing_prognose.ipynb
│   ├── zeitreihen_tools.py
│   ├── README.md
│   ├── daten/
│   │   ├── bike_day.csv
│   │   ├── energie_sensoren.csv
│   │   ├── download_daten.py
│   │   ├── quellen_manifest.json
│   │   └── README.md
│   └── uebungen/
│       ├── 01_uebung_fenster_und_backtesting.ipynb
│       ├── 02_uebung_echte_energie_sensoren.ipynb
│       ├── 03_fragen_zeitreihen.ipynb
│       └── loesungen/
├── set13-neuronale-netze-nn1/
│   ├── 01_mlp_regression.ipynb
│   ├── 02_mlp_klassifikation.ipynb
│   ├── README.md
│   └── uebungen/
│       ├── 01_uebung_mlp_regression.ipynb
│       ├── 02_uebung_mlp_klassifikation.ipynb
│       ├── 03_fragen_neuronale_netze.ipynb
│       └── loesungen/
├── set14-neuronale-netze-nn2/
│   ├── 01_pytorch_ziffern_und_pixel.ipynb
│   ├── 02_cnn_filter_pooling_und_feature_maps.ipynb
│   ├── 03_transfer_learning_nur_der_kopf.ipynb
│   ├── cv_tools.py
│   ├── README.md
│   ├── daten/
│   │   └── README.md
│   └── uebungen/
│       ├── 01_uebung_kleines_cnn.ipynb
│       ├── 02_uebung_transfer_zwei_ziffern.ipynb
│       ├── 03_fragen_computer_vision.ipynb
│       └── loesungen/
└── set15-modelle-speichern-und-laden/
    ├── 01_sklearn_pipeline_speichern_und_laden.ipynb
    ├── 02_sklearn_eigener_transformer_und_modellpaket.ipynb
    ├── 03_pytorch_gewichte_speichern_und_laden_cpu.ipynb
    ├── deployment_tools.py
    ├── custom_transformer.py
    ├── model_code.py
    ├── predict.py
    ├── README.md
    └── uebungen/
        ├── 01_fragen_modelle_speichern_und_laden.ipynb
        └── loesungen/
```

## Set 3: echte Sensorsignale und Feature Engineering

Nach der tabellarischen EDA folgen zwei zusammenhängende Beispiele:

- `05_sensor_signale_fft_features.ipynb`: echte Kugellager-Beschleunigungssignale, geschätzte Umdrehungsfenster, FFT und Zeit-/Frequenzmerkmale pro Messfenster.
- `06_pca_sensor_features.ipynb`: Korrelationen, Standardisierung, anschauliche PCA-Achsen, Komponentengewichte und die Berechnung neuer Merkmale.

Beide Notebooks laden beim ersten Start nur vier kleine MATLAB-Aufnahmen direkt vom CWRU Bearing Data Center in `set3-datenanalyse-und-visualisierung/daten/cwru`. Danach nutzen sie den lokalen Cache offline. Internet ist nur beim ersten Download nötig. Die neuen Notebooks enthalten kleine Aufgaben; die Hilfsdatei `sensor_features.py` bündelt Laden und Feature-Berechnung. Quellen und Datenauswahl stehen in `set3-datenanalyse-und-visualisierung/daten/README.md`.

## Set 12: Zeitreihenanalyse

Fünf Beispiele behandeln interaktive Bereichs-/Fensterwahl, Trend/Saisonalität/Autokorrelation, zeitliches Backtesting, ARIMA und einen Test auf echten Fahrrad-Ausleihdaten. Zwei Übungen und ein Fragenkatalog mit 25 Fragen ergänzen das Set. Eine Übung verwendet echte Energie-Sensordaten. Beide Datenauswahlen liegen offline vor und sind unter CC BY 4.0 kommerziell nutzbar mit Quellenangabe.

Die Notebooks enthalten gespeicherte Outputs. Für Änderungen der Slider müssen die Zellen mit laufendem Kernel ausgeführt werden. Überblick und Quellen: `set12-zeitreihenanalyse/README.md`.

## NN1 und NN2: Sets 13 und 14

Die bisherigen neuronalen Netze liegen als NN1 auf Platz 13. Unüberwachtes Lernen und Zeitreihen sind dafür auf Plätze 11 und 12 gerückt. NN2 / Set 14 ergänzt drei CPU-PyTorch-Beispiele: Ziffernerkennung, ein kleines CNN mit sichtbaren Filtern/Feature Maps und Transfer Learning mit vortrainiertem MobileNet-Backbone und ausschließlich neu trainiertem Kopf. Dazu kommen zwei einfache Übungen und 20 Fragen.

PyTorch für NN2 separat als CPU-Build installieren:

```powershell
.venv\Scripts\python.exe -m pip install -r requirements-cpu.txt
```

Vorher die normalen Kursabhängigkeiten aus `requirements.txt` installieren. Die CPU-Datei verwendet den offiziellen CPU-Wheel-Index und fixiert zusammenpassende getestete Versionen. Überblick: `set14-neuronale-netze-nn2/README.md`.

## Set 15: Modelle speichern und laden

Drei kurze Beispiele mit scikit-learn und CPU-PyTorch zeigen gespeicherte Pipelines, eigene Transformer und getrennte Architektur/Gewichte. Alle Modelle werden in einem neuen Python-Prozess geladen und ihre Vorhersagen verglichen. Dazu kommen 18 Übungsfragen und lokale Musterantworten. Einstieg: `set15-modelle-speichern-und-laden/README.md`. PyTorch verwendet dieselbe `requirements-cpu.txt` wie NN2.

## Voraussetzungen

- Python 3.11 oder neuer
- ein Terminal (PowerShell, Terminal oder Bash)
- optional: Git

Prüfe deine Python-Version:

```bash
python --version
```

Unter Windows kann der Befehl stattdessen `py --version` lauten.

## Installation mit virtueller Umgebung

Eine virtuelle Umgebung hält die Pakete dieses Kurses von anderen Python-Projekten getrennt.

### Windows PowerShell

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m jupyter lab
```

Falls PowerShell das Aktivierungsskript blockiert, kann die Umgebung auch ohne Aktivierung verwendet werden:

```powershell
.venv\Scripts\python.exe -m pip install -r requirements.txt
.venv\Scripts\python.exe -m jupyter lab
```

### macOS und Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m jupyter lab
```

Jupyter öffnet sich normalerweise automatisch im Browser. Starte mit dem ersten Notebook in `set1-python-grundlagen` und führe die Zellen der Reihe nach mit `Shift + Enter` aus.

## Empfohlene Arbeitsweise

1. Virtuelle Umgebung aktivieren.
2. JupyterLab starten.
3. Notebook von oben nach unten durcharbeiten.
4. Beispiele verändern und erneut ausführen.
5. Übungen zuerst selbst lösen und danach die Musterlösung ausführen.

Die Aufgaben eines Sets liegen jeweils im Unterordner `uebungen`. Zugehörige Musterlösungen befinden sich lokal in `uebungen/loesungen`. Alle solchen Lösungsordner werden absichtlich nicht von Git erfasst, damit die Lösungen nicht versehentlich zusammen mit den Aufgaben veröffentlicht werden.

## Hinweise zu Jupyter

- Eine **Markdown-Zelle** enthält Erklärtext.
- Eine **Code-Zelle** enthält ausführbaren Python-Code.
- Mit `Shift + Enter` wird eine Zelle ausgeführt.
- Arbeite die Zellen am besten von oben nach unten durch.
- Falls Ergebnisse merkwürdig wirken, starte das Notebook neu und führe alle Zellen noch einmal der Reihe nach aus.

## Lizenz / Nutzung

Die Materialien sind als begleitende Beispiele für den ML-Kurs gedacht und können innerhalb des Kurses angepasst und erweitert werden.

Für externe Beispieldaten gelten die jeweils im Datenordner dokumentierten Lizenzen und Quellenangaben.
