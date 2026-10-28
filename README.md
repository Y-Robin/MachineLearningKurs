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
│   ├── 07_datenerfassung_und_doe.ipynb
│   ├── 08_kaggle_datensaetze_laden.ipynb
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
│       ├── 04_uebung_datenerfassung_doe.ipynb
│       ├── 05_uebung_datensatz_dokumentation.ipynb
│       └── loesungen/
├── set4-machine-learning-mit-scikit-learn/
│   ├── 01_daten_verstehen_und_visualisieren.ipynb
│   ├── 02_sklearn_transformer_basics.ipynb
│   ├── 03_preprocessing_mit_pipeline.ipynb
│   ├── 04_daten_richtig_aufteilen.ipynb
│   ├── 05_kreuzvalidierung_ohne_data_leakage.ipynb
│   ├── 06_klassenungleichgewicht_und_smote.ipynb
│   └── uebungen/
│       ├── 01_uebungen_datenanalyse.ipynb
│       ├── 02_fragen_preprocessing_pipeline.ipynb
│       ├── 03_programmieruebungen_preprocessing.ipynb
│       ├── 04_uebung_splits_und_kreuzvalidierung.ipynb
│       ├── 05_uebung_klassenungleichgewicht.ipynb
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
│   ├── 03b_ar_ma_und_arma.ipynb
│   ├── 04_arima_prognosehorizont_und_unsicherheit.ipynb
│   ├── 05_synthetische_daten_modellvergleich.ipynb
│   ├── zeitreihen_tools.py
│   ├── zeitreihen_demos.py
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

## Einstieg mit Visual Studio Code

### 1. Python und VS Code installieren

Installiere [Python ab Version 3.11](https://www.python.org/downloads/) und [Visual Studio Code](https://code.visualstudio.com/). Aktiviere bei der Python-Installation unter Windows die Option **Add python.exe to PATH**, falls sie angeboten wird.

Öffne in VS Code die Ansicht **Erweiterungen / Extensions** und installiere diese beiden Erweiterungen von Microsoft:

- [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
- [Jupyter](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter)

### 2. Kursordner öffnen und Pakete installieren

Lade das Repository herunter und entpacke es oder klone es mit Git. Öffne anschließend in VS Code über **Datei → Ordner öffnen** den Kursordner mit der Datei `requirements.txt`.

Öffne über **Terminal → Neues Terminal** das integrierte Terminal. Erstelle dort eine virtuelle Umgebung für die Kurspakete und installiere die Abhängigkeiten:

**Windows (PowerShell)**

```powershell
py -m venv .venv
.venv\Scripts\python.exe -m pip install -r requirements.txt
```

**macOS / Linux**

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
```

Für die PyTorch-Beispiele in Set 14 und 15 installierst du unter Windows/Linux zusätzlich die CPU-Pakete:

```powershell
# Windows
.venv\Scripts\python.exe -m pip install -r requirements-cpu.txt
```

```bash
# Linux
.venv/bin/python -m pip install -r requirements-cpu.txt
```

### 3. Notebook öffnen und Kernel auswählen

1. Öffne `set1-python-grundlagen/01_python_setup_und_bibliotheken.ipynb` im Datei-Explorer von VS Code.
2. Klicke oben rechts auf **Kernel auswählen / Select Kernel**. Wähle bei Bedarf **Anderen Kernel auswählen / Select Another Kernel → Python-Umgebungen / Python Environments** und anschließend die Umgebung `.venv` im Kursordner.
3. Führe die Zellen von oben nach unten mit **Shift + Enter** aus. Codezellen führen Python aus, Markdown-Zellen enthalten Erklärungen.

Beim nächsten Mal öffnest du den Kursordner und das gewünschte Notebook wieder in VS Code und verwendest denselben `.venv`-Kernel. Weitere Hinweise stehen in der [VS-Code-Anleitung für Jupyter-Notebooks](https://code.visualstudio.com/docs/datascience/jupyter-notebooks).

## Mit dem Kurs arbeiten

Arbeite die Sets der Reihe nach durch, probiere die Beispiele aus und verändere einzelne Werte. Löse anschließend die Aufgaben im jeweiligen Ordner `uebungen`. Falls vorhanden, findest du die Musterlösungen lokal unter `uebungen/loesungen`.

Interaktive Regler funktionieren, nachdem du die zugehörigen Zellen ausgeführt hast. Wenn Ergebnisse unerwartet sind, starte den Kernel über die Notebook-Werkzeugleiste neu und führe alle Zellen erneut aus.

## Nutzung und Datenquellen

Die Materialien begleiten den ML-Kurs und können innerhalb des Kurses angepasst und erweitert werden. Quellen und Lizenzen externer Beispieldaten stehen in den jeweiligen Datenordnern.
