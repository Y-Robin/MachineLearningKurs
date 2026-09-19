# Machine-Learning-Kurs – Codebeispiele

Dieses Repository entsteht Schritt für Schritt zusammen mit dem Kurs. Die Inhalte sind in **Sets** gegliedert. Jedes Thema wird als Jupyter Notebook erklärt und enthält ausführbare Beispiele sowie kleine Übungen.

## Aktueller Inhalt

```text
.
├── README.md
├── requirements.txt
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
└── set5-lineare-und-logistische-regression/
    ├── 01_lineare_regression.ipynb
    ├── 02_m_und_b_interaktiv.ipynb
    ├── 03_logistische_regression.ipynb
    ├── 04_pipeline_palmer_penguins.ipynb
    ├── daten/
    │   └── README.md
    └── uebungen/
        ├── 01_uebungen_lineare_regression.ipynb
        ├── 02_uebungen_logistische_regression.ipynb
        ├── 03_uebungen_pipeline_penguins.ipynb
        ├── 04_fragen_regression_klassifikation.ipynb
        └── loesungen/
```

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
