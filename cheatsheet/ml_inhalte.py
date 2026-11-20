"""Inhalte und ausführbare Rezepte des ML-Cheat-Sheets (UTF-8)."""
from textwrap import dedent

PAGES = []
def page(title, intro, principle, source, code='', notes=(), table=(), setup='', run=True):
    PAGES.append(dict(title=title, intro=intro, principle=principle, source=source,
                      code=dedent(code).strip(), notes=list(notes), table=list(table),
                      setup=dedent(setup).strip(), run=run))

COMMON = '''
from pathlib import Path
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline, make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.metrics import (accuracy_score, f1_score,
    mean_absolute_error, mean_squared_error, r2_score)
ROOT = next(p for p in [Path.cwd(), *Path.cwd().parents]
            if (p / "requirements.txt").exists())
'''

page('Methoden im Machine Learning',
     'Vom Rohdatensatz bis zur überprüften Vorhersage. Dieses Nachschlageheft verbindet die Methoden aus Set 3 bis 15 mit kurzen Python-Rezepten und konkreten Kursdateien.',
     'Erst die spätere Anwendung festlegen, dann Daten aufteilen. Alle gelernten Schritte gehören in die Trainings- und Validierungsschleife.',
     'Kursübersicht: README.md',
     notes=[('So benutzt du das Heft', 'Jede Methodenseite enthält Zweck, Code, Ergebnis oder erwartete Ausgabe und einen Verweis auf das Kursnotebook. Die Rezepte sind gekürzte, an den Kurs angelehnte Beispiele; keine wortgetreuen Abschriften.'),
            ('Code ausführen', 'Das begleitende Notebook im Ordner cheatsheet von oben nach unten mit der Kursumgebung ausführen. Die gemeinsame Importzelle gilt für alle Rezepte. Die Modellseiten nennen ihre Datenbasis ausdrücklich.'),
            ('Ergebnisse lesen', 'Neu ausgeführte Beispiele verwenden random_state=42. Zahlen gelten nur für den genannten Split und die jeweilige Datenbasis. Das Heft ersetzt keinen fairen Benchmark auf identischen Daten.')],
     table=[('Seiten', 'Nachschlagen'), ('2–3', 'Imports und Datensätze'), ('4–6', 'Imputation, Skalierung, eigene Merkmale'), ('7–9', 'Splits, Kreuzvalidierung, Ungleichgewicht'), ('10–11', 'Metriken und Visualisierungen'), ('12–18', 'Regression, Klassifikation, CRF'), ('19–21', 'Zeitreihen und Prognosen'), ('22–24', 'MLP, CNN und Transfer Learning'), ('25–28', 'PCA, NMF, t-SNE und Clustering'), ('29–31', 'Anomalien, Speichern und Transformer-Klasse')])

page('Imports und gemeinsame Daten',
     'Die folgenden zwei kleinen Datensätze werden auf den Modellseiten wiederverwendet: Halbmonde für nichtlineare Klassifikation und die simulierten Mietdaten aus Set 5 für Regression.',
     'X enthält Merkmale als 2D-Matrix, y enthält Zielwerte. Xct/Xce stehen für Training/Test der Klassifikation, Xrt/Xre für Regression.',
     'Set 5: 01_lineare_regression.ipynb; Set 10: 01_svm_klassifikation.ipynb',
     '''
     from sklearn.datasets import make_moons
     Xc, yc = make_moons(n_samples=500, noise=.22,
                        random_state=42)
     Xct, Xce, yct, yce = train_test_split(
         Xc, yc, test_size=.25, stratify=yc, random_state=42)

     rng = np.random.default_rng(42)
     flaeche = rng.uniform(25, 130, 120)
     miete = 8.5*flaeche + 320 + rng.normal(0, 85, 120)
     Xr = pd.DataFrame({"flaeche_qm": flaeche.round(1)})
     yr = pd.Series(miete.round(2), name="miete_euro")
     Xrt, Xre, yrt, yre = train_test_split(
         Xr, yr, test_size=.25, random_state=42)
     print("Klassifikation:", Xct.shape, Xce.shape)
     print("Regression:", Xrt.shape, Xre.shape)
     ''', notes=[('Gemeinsame Imports', 'Im Notebook stehen NumPy als np, pandas als pd, Matplotlib als plt, Path, sys, train_test_split, Pipeline, make_pipeline, StandardScaler, SimpleImputer sowie accuracy_score, f1_score, mean_absolute_error, mean_squared_error und r2_score in der ersten Zelle.'),
                 ('Bewertungsregel', 'Die festen Modelle dieses Hefts sind didaktische Einzelrezepte. Bei eigener Modellauswahl zunächst ausschließlich innerhalb der Entwicklungsdaten vergleichen; den Test erst nach der Auswahl auswerten.')])

page('Datensätze passend zur Aufgabe',
     'Für Klassifikation ist y eine Klasse, für Regression eine Zahl. Ob ein Datensatz eine Zufallsaufteilung erlaubt, hängt von Messaufbau, Gruppen und Zeitabhängigkeit ab.',
     'Die Zieldefinition entscheidet über das Verfahren. Dieselbe Tabelle kann mehrere Aufgaben erlauben, benötigt dann aber jeweils eine klare Zielvariable.',
     'Set 3: daten/README.md; Sets 5, 7–9, 12, 14 und 15',
     '''
     from sklearn.datasets import load_iris, load_digits
     iris = load_iris(as_frame=True)
     print("Iris:", iris.data.shape, iris.target.nunique())
     daten = ROOT / "set3-datenanalyse-und-visualisierung/daten"
     penguins = pd.read_csv(daten / "palmer_penguins.csv")
     wein = pd.read_csv(daten / "wine_quality_red.csv", sep=";")
     print("Penguins:", penguins.shape, "Wein:", wein.shape)
     ''', table=[('Daten im Kurs', 'Aufgabe / Besonderheit'),
     ('Iris / WDBC Breast Cancer', 'Art / Diagnose; tabellarische Klassifikation'),
     ('Palmer Penguins', 'species klassifizieren; Körpermaße als Merkmale'),
     ('SMS Spam / Banknoten', 'Spam erkennen / Echtheit klassifizieren'),
     ('AI4I Predictive Maintenance', 'Machine failure; seltene positive Klasse'),
     ('Mietdaten / Sinusdaten', 'Regression; kontrollierte Simulationen'),
     ('Wine Quality', 'quality als Zahl oder explizit definierte Klasse'),
     ('Bike Sharing / Energie', 'cnt / Appliances; chronologische Prognose'),
     ('CWRU / künstliche Spektren', 'Signalmerkmale / additive NMF-Bausteine'),
     ('Digits / make_moons / make_blobs', 'Bilder / Klassifikation / Cluster-Demos'),
     ('Kaggle in Set 3', 'Titanic, House Prices, Credit Card Fraud; manuell laden')],
     notes=[('Zielleckage vermeiden', 'AI4I: Fehleruntertypen können das Ziel direkt verraten. Bike Sharing: casual + registered = cnt, deshalb keine Zielbestandteile als Eingaben verwenden. IDs, spätere Messwerte und diagnostische Hilfsspalten prüfen.'),
            ('Zahlen sind keine garantierten Abstände', 'Wine quality ist eine ordinale Bewertung. Regression behandelt Abstände wie Zahlenabstände; Klassifikation beantwortet eine andere, vorher definierte Frage.')])

page('Imputation und Standardisierung',
     'SimpleImputer ersetzt fehlende Werte, StandardScaler bringt numerische Merkmale auf vergleichbare Skalen. Das ist besonders für kNN, SVM, lineare Regularisierung, PCA und MLP hilfreich.',
     'fit lernt Median, Mittelwert und Streuung ausschließlich am Training. Für neue Daten wird nur transform aufgerufen.',
     'Set 4: 02_sklearn_transformer_basics.ipynb',
     '''
     train = pd.DataFrame({"alter": [20., 40., np.nan],
                           "umsatz": [100., 300., 200.]})
     neu = pd.DataFrame({"alter": [np.nan], "umsatz": [400.]})
     prep = make_pipeline(SimpleImputer(strategy="median"),
                          StandardScaler())
     z_train = prep.fit_transform(train)
     z_neu = prep.transform(neu)
     print("Mediane:", prep[0].statistics_)
     print("Training:\\n", np.round(z_train, 3))
     print("Neu:", np.round(z_neu, 3))
     ''', notes=[('Wie rechnen?', 'z = (x - Mittelwert des Trainings) / Standardabweichung des Trainings. StandardScaler verwendet ddof=0. Neue Daten dürfen Mittelwert und Streuung verändern; sie werden nicht erneut auf Mittelwert 0 angepasst.'),
            ('Alternativen', 'Median ist relativ robust gegen Ausreißer. MinMaxScaler skaliert anhand des Trainingsbereichs; neue Werte können außerhalb von [0,1] liegen. RobustScaler nutzt Median und Quantilabstand. Bäume brauchen normalerweise keine Standardisierung.'),
            ('Fehlende Werte sind Information', 'SimpleImputer(add_indicator=True) ergänzt Indikatoren für Spalten, die im Fit fehlende Werte enthielten. Gründe für fehlende Werte trotzdem prüfen. Zielwerte nicht ohne fachliche Begründung imputieren.')])

page('Gemischte Tabellen als Pipeline',
     'ColumnTransformer verarbeitet Zahlen und Kategorien getrennt. OneHotEncoder erzeugt Indikatorspalten, damit Kategorien keine künstliche numerische Reihenfolge erhalten.',
     'Eine Pipeline verbindet Vorverarbeitung und Modell. Bei jedem CV-Fold werden beide ausschließlich am jeweiligen Training gelernt.',
     'Set 4: 03_preprocessing_mit_pipeline.ipynb; Set 5: 04_pipeline_palmer_penguins.ipynb',
     '''
     from sklearn.compose import ColumnTransformer
     from sklearn.preprocessing import OneHotEncoder
     from sklearn.linear_model import LogisticRegression
     df = penguins.dropna(subset=["species"])
     X = df[["bill_length_mm", "bill_depth_mm", "island", "sex"]]
     y = df["species"]
     Xt, Xe, yt, ye = train_test_split(
         X, y, stratify=y, test_size=.25, random_state=42)
     num = make_pipeline(SimpleImputer(strategy="median"),
                         StandardScaler())
     cat = make_pipeline(SimpleImputer(strategy="most_frequent"),
         OneHotEncoder(handle_unknown="ignore"))
     prep = ColumnTransformer([
         ("num", num, ["bill_length_mm", "bill_depth_mm"]),
         ("cat", cat, ["island", "sex"])])
     penguin_model = Pipeline([("prep", prep),
         ("clf", LogisticRegression(max_iter=2000))])
     penguin_model.fit(Xt, yt)
     print("Accuracy:", round(penguin_model.score(Xe, ye), 3))
     print("Merkmale:", len(prep.get_feature_names_out()))
     ''', notes=[('Unbekannte Kategorien', 'handle_unknown="ignore" verhindert einen Fehler bei neuen Kategorien; die betreffende One-Hot-Gruppe wird null. Prüfen, ob dieses Verhalten für die Anwendung sinnvoll ist.'),
            ('Spalten bewusst wählen', 'Spaltenlisten werden hier fachlich festgelegt. Statistische Feature-Auswahl, Imputation, Skalierung und PCA gehören bei Modellbewertung in die Pipeline. Einfache EDA-Fits auf allen Daten sind keine validierten Modelle.')])

page('Eigene Transformer und Signalmerkmale',
     'Ein eigener Transformer bildet Fachwissen als reproduzierbaren Schritt ab. Im Kurs ergänzen Flächenprodukte die Iris-Merkmale; bei Sensorsignalen werden beispielsweise RMS und Spektralenergie pro Fenster gebildet.',
     'Eine feste Rechenregel braucht kein Training. Sobald der Transformer Schwellen, Frequenzen oder Referenzen aus Daten lernt, geschieht das in fit am Training.',
     'Set 15: 02b_sklearn_eigener_transformer_schritt_fuer_schritt.ipynb; Set 3: sensor_features.py',
     '''
     # Importierbare Kursklasse, damit Speichern/Laden funktioniert.
     sys.path.insert(0, str(ROOT / "set15-modelle-speichern-und-laden"))
     from custom_transformer_einfach import FlaechenMerkmale
     from sklearn.linear_model import LogisticRegression
     it, ie, jt, je = train_test_split(iris.data, iris.target,
         stratify=iris.target, test_size=.25, random_state=42)
     iris_model = make_pipeline(FlaechenMerkmale(),
         SimpleImputer(strategy="median"), StandardScaler(),
         LogisticRegression(max_iter=2000))
     iris_model.fit(it, jt)
     print("Merkmale:", FlaechenMerkmale().fit_transform(it).shape)
     print("Accuracy:", round(iris_model.score(ie, je), 3))

     sys.path.insert(0, str(ROOT / "set3-datenanalyse-und-visualisierung"))
     from sensor_features import signal_merkmale
     fs = 48000
     t = np.arange(8192) / fs
     signal = np.sin(2*np.pi*1000*t)  # kontrolliertes Testsignal
     f = signal_merkmale(signal, fs=fs)
     print("RMS:", round(f["rms"], 3),
           "Peak-Hz:", round(f["peak_frequenz_hz"], 1))
     ''', notes=[('Aufbau der Klasse', 'FlaechenMerkmale erbt von TransformerMixin und BaseEstimator. fit gibt self zurück; transform kopiert X und ergänzt kelch_flaeche sowie blueten_flaeche als Längen-Breiten-Produkte. Vollständiger Klassencode: Seite 31; importierbare Originaldatei: custom_transformer_einfach.py.'),
            ('Fenster und Frequenzen', 'FFT-Frequenzauflösung: fs / Fensterlänge. Set 3 nutzt 8192 Samples, Mittelwertabzug und Hann-Fenster. Fenster derselben Aufnahme sind abhängig; bei Bewertung nach Aufnahme oder Lager trennen. Vier CWRU-Aufnahmen allein tragen keine belastbare Generalisierung auf neue Lager.')])

page('Split nach späterer Anwendung',
     'Zufallssplits passen zu unabhängigen Zeilen. Gruppen müssen zusammenbleiben, wenn das Modell später neue Personen, Maschinen oder Aufnahmen sehen soll; Prognosen benötigen chronologische Splits.',
     'Der Split simuliert die Zukunft der Anwendung. Ein technisch korrekter Zufallssplit kann bei abhängigen Messungen trotzdem die falsche Frage beantworten.',
     'Set 4: 04_daten_richtig_aufteilen.ipynb',
     '''
     from sklearn.model_selection import GroupShuffleSplit
     # 60 % Training, 20 % Validierung, 20 % Test
     ids = np.arange(len(yc))
     dev, test = train_test_split(ids, test_size=.2,
         stratify=yc, random_state=42)
     train, val = train_test_split(dev, test_size=.25,
         stratify=yc[dev], random_state=42)
     print("Train/Val/Test:", len(train), len(val), len(test))

     # Demo: 50 Maschinen mit je 10 aufeinanderfolgenden Zeilen
     gruppen = np.repeat(np.arange(50), 10)
     splitter = GroupShuffleSplit(n_splits=1, test_size=.2,
                                  random_state=42)
     tr, te = next(splitter.split(Xc, yc, groups=gruppen))
     print("Gemeinsame Gruppen:",
           len(set(gruppen[tr]) & set(gruppen[te])))
     # Zeitreihe: erst sortieren, dann ohne Mischen teilen
     reihe = pd.Series(np.arange(100.))
     zeit_train, zeit_test = reihe.iloc[:80], reihe.iloc[80:]
     ''', table=[('Fall', 'Holdout / Kreuzvalidierung'),
     ('Unabhängige Regression', 'Zufallssplit / KFold mit shuffle=True'),
     ('Unabhängige Klassifikation', 'stratify=y / StratifiedKFold'),
     ('Neue Gruppen', 'GroupShuffleSplit / GroupKFold'),
     ('Gruppen und Klassenbalance', 'ggf. StratifiedGroupKFold; Balance prüfen'),
     ('Vorhersage zukünftiger Werte', 'Zeit-Holdout / TimeSeriesSplit mit Lücke')],
     notes=[('Überlappende Zeitfenster', 'Nicht nur Zeilenindizes prüfen: Trainingsziele dürfen nicht in den Validierungszeitraum ragen. Fenster, Forecast-Horizont und zeitliche Verfügbarkeit bestimmen die benötigte Lücke. Gruppen mit Zeitordnung erfordern oft einen eigenen Split.')])

page('Kreuzvalidierung und Tuning',
     'Kreuzvalidierung schätzt die Streuung über mehrere Trainingsaufteilungen. GridSearchCV wählt Hyperparameter ausschließlich innerhalb der Entwicklungsdaten.',
     'Testdaten bleiben bis nach der Auswahl unangetastet. Den besten Such-CV-Wert nicht als unabhängige Schätzung der endgültigen Güte verkaufen.',
     'Set 4: 05_kreuzvalidierung_ohne_data_leakage.ipynb; Set 6: 03_hyperparameter_tuning_regression.ipynb',
     '''
     from sklearn.model_selection import StratifiedKFold, GridSearchCV
     from sklearn.linear_model import LogisticRegression
     dev_x, test_x, dev_y, test_y = train_test_split(
         Xc, yc, test_size=.2, stratify=yc, random_state=42)
     pipe = Pipeline([("scale", StandardScaler()),
                      ("clf", LogisticRegression(max_iter=2000))])
     cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
     suche = GridSearchCV(pipe, {"clf__C": [.01, .1, 1, 10]},
                          cv=cv, scoring="f1", n_jobs=1)
     suche.fit(dev_x, dev_y)
     print("Beste Parameter:", suche.best_params_)
     print("Such-CV F1:", round(suche.best_score_, 3))
     pred = suche.predict(test_x)
     print("Finaler Test-F1:", round(f1_score(test_y, pred), 3))
     ''', notes=[('Regression und Gruppen', 'Für Regression beispielsweise KFold(5, shuffle=True, random_state=42) und scoring="neg_root_mean_squared_error" verwenden. Bei GroupKFold zusätzlich groups an fit bzw. cross_validate übergeben; eine normale KFold-Schleife schützt Gruppen nicht.'),
            ('Negative Fehlerscores', 'scikit-learn maximiert Scores. Bei neg_mean_absolute_error oder neg_root_mean_squared_error das Vorzeichen zur Darstellung als Fehler umdrehen. Größere negative Scores bedeuten kleinere Fehler.'),
            ('Verschachtelte CV', 'Wenn Modellfamilien und Parameter umfangreich verglichen werden und kein separater Test verfügbar ist: äußere CV für die Bewertung, innere CV für die Auswahl. Bei Zeit und Gruppen müssen beide Ebenen die Abhängigkeiten respektieren.')])

page('Seltene Klassen und Schwellen',
     'Bei seltenen Fehlern kann ein Modell mit hoher Accuracy fast alle wichtigen Fälle übersehen. Klassenweights, Sampling und ein passender Entscheidungsschwellenwert beantworten unterschiedliche Probleme.',
     'Sampling ausschließlich im Trainingsfold. Schwellen an Validierungsdaten wählen und anschließend für den finalen Test festhalten.',
     'Set 4: 06_klassenungleichgewicht_und_smote.ipynb',
     '''
     from sklearn.datasets import make_classification
     from sklearn.linear_model import LogisticRegression
     from sklearn.model_selection import cross_validate, StratifiedKFold
     from imblearn.pipeline import Pipeline as SamplingPipeline
     from imblearn.over_sampling import SMOTE
     Xi, yi = make_classification(n_samples=1000, n_features=8,
         n_informative=4, weights=[.95, .05], random_state=42)
     a, b, c, d = train_test_split(Xi, yi, stratify=yi,
                                  test_size=.25, random_state=42)
     balanced = SamplingPipeline([
         ("impute", SimpleImputer(strategy="median")),
         ("scale", StandardScaler()),
         ("sample", SMOTE(random_state=42, k_neighbors=3)),
         ("clf", LogisticRegression(max_iter=2000))])
     cv = StratifiedKFold(5, shuffle=True, random_state=42)
     scores = cross_validate(balanced, a, c, cv=cv,
         scoring=["recall", "precision", "average_precision"])
     print({k: round(v.mean(), 3) for k, v in scores.items()
            if k.startswith("test_")})
     ''', notes=[('Gewichtung als Alternative', 'LogisticRegression(class_weight="balanced") verändert die Gewichtung im Verlust. Es entstehen keine neuen Zeilen. Gewichtung und SMOTE separat innerhalb derselben CV vergleichen; automatisch kombinieren muss nicht besser sein.'),
            ('SMOTE hat Voraussetzungen', 'Es interpoliert zwischen Nachbarn. Kategoriale Werte brauchen beispielsweise SMOTENC; One-Hot-Interpolation kann unsinnige Zwischenwerte erzeugen. Auch genügend Minderheitsbeispiele pro Fold und die Gruppenstruktur beachten.'),
            ('Schwelle und Kalibrierung', 'p >= 0.5 ist nur eine Regel. Auf Validierung etwa einen Mindest-Recall verlangen und dann Precision bzw. Kosten vergleichen. Sampling und Klassenweights können Wahrscheinlichkeiten verschieben; Kalibrierung bei Bedarf separat validieren.')])

page('Regressionsmetriken und Plots',
     'MAE beschreibt den mittleren absoluten Fehler in der Zieleinheit. RMSE gewichtet große Fehler stärker; R² beschreibt die Verbesserung gegenüber einem konstanten Mittelwert auf den ausgewerteten Daten.',
     'Ein kleiner Trainingsfehler ist keine Generalisierung. Auf zurückgehaltenen Daten mit einer einfachen Baseline vergleichen und die Residuen ansehen.',
     'Set 5: 01_lineare_regression.ipynb; Set 10: 02_svm_regression.ipynb',
     '''
     from sklearn.linear_model import LinearRegression
     from sklearn.dummy import DummyRegressor
     reg = LinearRegression().fit(Xrt, yrt)
     pred_r = reg.predict(Xre)
     baseline = DummyRegressor().fit(Xrt, yrt).predict(Xre)
     print("MAE:", round(mean_absolute_error(yre, pred_r), 2))
     print("RMSE:", round(np.sqrt(mean_squared_error(yre, pred_r)), 2))
     print("R2:", round(r2_score(yre, pred_r), 3))
     print("Baseline-MAE:", round(mean_absolute_error(yre, baseline), 2))
     fig, ax = plt.subplots(1, 2, figsize=(9, 2.8))
     ax[0].scatter(yre, pred_r, s=14)
     lo, hi = min(yre.min(), pred_r.min()), max(yre.max(), pred_r.max())
     ax[0].plot([lo, hi], [lo, hi], "k--")
     ax[0].set(xlabel="Ist [Euro]", ylabel="Prognose [Euro]")
     ax[1].scatter(pred_r, yre-pred_r, s=14)
     ax[1].axhline(0, color="black", ls="--")
     ax[1].set(xlabel="Prognose [Euro]", ylabel="Residuum [Euro]")
     fig.tight_layout()
     ''', notes=[('Interpretation', 'R² = 1 ist perfekt, R² = 0 entspricht auf diesen Testdaten dem Testmittelwert, R² < 0 ist schlechter. Der DummyRegressor verwendet dagegen den Trainingsmittelwert. R² ist kein Prozentwert korrekter Vorhersagen.'),
            ('Was im Plot auffällt', 'Eine Kurve in den Residuen deutet auf fehlende Nichtlinearität, eine Trichterform auf veränderliche Streuung. Zeitlich korrelierte Residuen sprechen für noch nicht erfasste Dynamik. MAPE ist bei nullnahen Zielen problematisch.')])

page('Klassifikationsmetriken und Plots',
     'Precision fragt, wie viele positive Meldungen stimmen; Recall, wie viele echte positive Fälle gefunden werden. F1 verbindet beide, während ROC-AUC und Average Precision kontinuierliche Scores auswerten.',
     'Positive Klasse ausdrücklich festlegen. Bei Multiclass macro-F1 für die gleichgewichtete Sicht auf Klassen verwenden und Klassen einzeln prüfen.',
     'Set 5: 03_logistische_regression.ipynb; Set 4: 06_klassenungleichgewicht_und_smote.ipynb',
     '''
     from sklearn.svm import SVC
     from sklearn.metrics import (classification_report,
         ConfusionMatrixDisplay, RocCurveDisplay,
         PrecisionRecallDisplay, roc_auc_score, average_precision_score)
     clf = make_pipeline(StandardScaler(), SVC(C=1, kernel="rbf"))
     clf.fit(Xct, yct)
     pred_c = clf.predict(Xce)
     score_c = clf.decision_function(Xce)  # Klasse 1 ist positiv
     print(classification_report(yce, pred_c, zero_division=0, digits=3))
     print("ROC-AUC:", round(roc_auc_score(yce, score_c), 3),
           "AP:", round(average_precision_score(yce, score_c), 3))
     fig, ax = plt.subplots(1, 3, figsize=(10, 2.8))
     ConfusionMatrixDisplay.from_predictions(yce, pred_c, ax=ax[0],
         colorbar=False, cmap="Oranges")
     RocCurveDisplay.from_predictions(yce, score_c, ax=ax[1])
     PrecisionRecallDisplay.from_predictions(yce, score_c, ax=ax[2])
     fig.tight_layout()
     ''', notes=[('Formeln', 'Precision = TP/(TP+FP), Recall = TP/(TP+FN), F1 = 2PR/(P+R). In der sklearn-Konfusionsmatrix sind Zeilen die echten Klassen und Spalten die Vorhersagen. Balanced Accuracy mittelt den Recall über die Klassen.'),
            ('Seltene Klasse', 'Accuracy kann irreführen. PR-Kurve und AP ergänzen, Prävalenz nennen und die Kosten von FP/FN diskutieren. AP und ROC-AUC sind keine Kennzahlen eines einzelnen Schwellenwerts; AP ist nicht einfach die trapezförmige Fläche unter jedem PR-Plot.'),
            ('Multiclass und Wahrscheinlichkeiten', 'classification_report zeigt Klassen und macro/weighted-Mittel. ROC/PR erfordern z. B. eine One-vs-Rest-Auswertung. Für log_loss oder Kalibrierung echte Wahrscheinlichkeiten verwenden; SVM-Decision-Scores sind keine Wahrscheinlichkeiten.')])

page('Lineare Regression',
     'LinearRegression schätzt einen additiven Zusammenhang zwischen Merkmalen und einer Zahl. Sie liefert eine schnelle Baseline und gut nachvollziehbare Koeffizienten.',
     'Ein Koeffizient beschreibt den geschätzten Zusammenhang bei konstanten anderen Merkmalen. Das ist ohne kausales Studiendesign kein Beweis für eine Ursache.',
     'Set 5: 01_lineare_regression.ipynb; 05_xai_koeffizienten.ipynb',
     '''
     from sklearn.linear_model import LinearRegression
     linear = LinearRegression().fit(Xrt, yrt)
     m, b = linear.coef_[0], linear.intercept_
     neu = pd.DataFrame({"flaeche_qm": [80.]})
     print(f"Miete = {m:.2f} * Fläche + {b:.2f}")
     print("80 m²:", round(linear.predict(neu)[0], 2), "Euro")
     print("Test-R2:", round(linear.score(Xre, yre), 3))
     grid = pd.DataFrame({"flaeche_qm": np.linspace(25, 130, 100)})
     fig, ax = plt.subplots(figsize=(7, 2.8))
     ax.scatter(Xre.iloc[:, 0], yre, s=18, label="Test")
     ax.plot(grid.iloc[:, 0], linear.predict(grid), color="#f15a24")
     ax.set(xlabel="Wohnfläche [m²]", ylabel="Miete [Euro]")
     fig.tight_layout()
     ''', notes=[('Ergebnis im Kurs', 'Für genau die gerundeten Mietdaten aus Set 5: Steigung 8,29 Euro/m², Achsenabschnitt 337,67 Euro, Vorhersage für 80 m² rund 1000,70 Euro. Die Regressionsmetriken stehen auf Seite 10.'),
            ('Nichtlinear über Features', 'PolynomialFeatures(degree=2, include_bias=False) ergänzt Quadrate und Wechselwirkungen. Das Modell bleibt linear in den Koeffizienten, kann aber gekrümmte Verläufe abbilden. Grad und Regularisierung innerhalb der CV wählen.'),
            ('Grenzen', 'Korrelation zwischen Merkmalen macht einzelne Koeffizienten instabil. Extrapolation außerhalb des Trainingsbereichs kann trotz guter Testgüte scheitern.')])

page('Logistische Regression',
     'LogisticRegression modelliert Klassenwahrscheinlichkeiten; der Name bezeichnet ein Klassifikationsverfahren. Für binäre Ziele ist der Logit der positiven Wahrscheinlichkeit linear in den Merkmalen.',
     'predict_proba liefert Wahrscheinlichkeiten in der Reihenfolge classes_. Der Entscheidungsschwellenwert ist eine zusätzliche fachliche Wahl.',
     'Set 5: 03_logistische_regression.ipynb; 04_pipeline_palmer_penguins.ipynb',
     '''
     from sklearn.linear_model import LogisticRegression
     logistic = make_pipeline(StandardScaler(),
         LogisticRegression(C=1, max_iter=2000))
     logistic.fit(Xct, yct)
     classes = logistic[-1].classes_
     pos = list(classes).index(1)
     p = logistic.predict_proba(Xce)[:, pos]
     pred = (p >= .5).astype(int)
     print("Klassen:", classes)
     print("Erste Wahrscheinlichkeiten:", np.round(p[:5], 3))
     print("Test-F1:", round(f1_score(yce, pred), 3))
     print("Gewichte:", np.round(logistic[-1].coef_, 3))
     ''', notes=[('Was bedeutet C?', 'C ist die inverse Regularisierungsstärke: kleineres C bedeutet stärkere Regularisierung. Standardmäßig wird L2-Regularisierung eingesetzt. Eingaben skalieren und C innerhalb der CV auswählen.'),
            ('Gerade Grenzen', 'Auf Halbmond-Daten kann eine lineare Entscheidungsgrenze unterpassen. Eine RBF-SVM oder fachlich sinnvolle nichtlineare Features können besser passen; dafür muss die Bewertung gleich aufgebaut sein.'),
            ('Koeffizienten', 'Ein positives binäres Gewicht erhöht den Logit von classes_[1]. exp(Gewicht) ist der Faktor für die Odds bei einer Merkmalseinheit mehr. Bei standardisierten Merkmalen entspricht eine Einheit einer Trainingsstandardabweichung; korrelierte Features erschweren die Interpretation.')])

page('Regularisierung mit Ridge und Lasso',
     'Regularisierung begrenzt die Komplexität: Ridge schrumpft Gewichte mit einer L2-Strafe, Lasso kann mit einer L1-Strafe Gewichte exakt auf null setzen. ElasticNet verbindet beide.',
     'Bei Ridge/Lasso bedeutet größeres alpha stärkere Regularisierung. Skalierung und die Wahl von alpha gehören in dieselbe Pipeline und CV.',
     'Set 6: 02_regularisierung_l1_l2.ipynb; 03_hyperparameter_tuning_regression.ipynb',
     '''
     from sklearn.datasets import make_regression
     from sklearn.linear_model import Ridge, Lasso, ElasticNet
     from sklearn.model_selection import GridSearchCV, KFold
     X, y = make_regression(n_samples=60, n_features=30,
         n_informative=5, noise=20, random_state=42)
     a, b, c, d = train_test_split(X, y, test_size=.3, random_state=42)
     pipe = Pipeline([("scale", StandardScaler()), ("reg", Ridge())])
     cv = KFold(5, shuffle=True, random_state=42)
     grid = [{"reg": [Ridge()], "reg__alpha": [.1, 1, 10, 100]},
             {"reg": [Lasso(max_iter=20000)],
              "reg__alpha": [.1, 1, 10]}]
     search = GridSearchCV(pipe, grid, cv=cv,
         scoring="neg_root_mean_squared_error")
     search.fit(a, c)
     pred = search.predict(b)
     print("Gewählt:", search.best_params_)
     print("Test-RMSE:", round(np.sqrt(mean_squared_error(d, pred)), 2))
     print("Gewichte != 0:",
           np.count_nonzero(search.best_estimator_[-1].coef_))
     ''', notes=[('Bias und Varianz', 'Sehr flexible Modelle können Trainingsrauschen lernen. Stärkere Regularisierung erhöht oft den Bias und senkt die Varianz. Ein wachsender Abstand zwischen Trainings- und Validierungsfehler ist ein Warnsignal für Overfitting.'),
            ('Lasso und ElasticNet', 'Lasso-Selektion kann bei stark korrelierten Merkmalen zwischen ähnlichen Variablen wechseln. ElasticNet(alpha=..., l1_ratio=...) mischt L1 und L2; l1_ratio nahe 1 verhält sich stärker wie Lasso. Nullgewichte sind kein Beweis fachlicher Irrelevanz.')])

page('Naive Bayes und Textmerkmale',
     'Naive Bayes ist eine schnelle probabilistische Baseline mit bedingter Unabhängigkeitsannahme. GaussianNB passt zu kontinuierlichen Merkmalen, MultinomialNB zu nichtnegativen Zählmerkmalen wie Wortanzahlen.',
     'Der Textvektorisierer lernt sein Vokabular nur am Training. StandardScaler mit Zentrierung passt nicht vor MultinomialNB, weil negative Werte entstehen können.',
     'Set 7: 01_gaussian_naive_bayes.ipynb; 03_textmerkmale_multinomial_naive_bayes.ipynb',
     '''
     from sklearn.naive_bayes import GaussianNB, MultinomialNB
     from sklearn.feature_extraction.text import CountVectorizer
     nb = GaussianNB().fit(Xct, yct)
     print("GaussianNB F1:", round(f1_score(yce, nb.predict(Xce)), 3))
     path = ROOT / "set7-naive-bayes-und-textklassifikation/daten"
     sms = pd.read_csv(path / "SMSSpamCollection", sep="\t",
                       header=None, names=["label", "text"])
     a, b, c, d = train_test_split(sms.text, sms.label,
         stratify=sms.label, test_size=.25, random_state=42)
     spam = make_pipeline(CountVectorizer(), MultinomialNB(alpha=1))
     spam.fit(a, c)
     pred = spam.predict(b)
     print("Spam-F1:", round(f1_score(d, pred, pos_label="spam"), 3))
     print("Vokabular:", len(spam[0].vocabulary_))
     ''', notes=[('Wofür die Varianten gut sind', 'GaussianNB modelliert pro Klasse und Merkmal eine Normalverteilung. MultinomialNB nutzt nichtnegative Häufigkeiten; BernoulliNB modelliert binäre Merkmalspräsenz. Keine dieser Annahmen ist automatisch durch den Namen des Datensatzes erfüllt.'),
            ('Glättung und Bewertung', 'alpha verhindert Nullwahrscheinlichkeiten für ungesehene Wörter. Für Spam Precision und Recall der Klasse spam prüfen. Naive-Bayes-Wahrscheinlichkeiten können überkonfident sein, obwohl die Klassenentscheidung nützlich ist.'),
            ('Wiederholte Nachrichten', 'Duplikate, Sendergruppen und zeitliche Änderungen können Zufallssplits zu optimistisch machen. Der kleine Kursvergleich ist ein Einstieg; für die reale Anwendung entsprechend splitten.')])

page('Entscheidungsbäume und Ensembles',
     'Ein Entscheidungsbaum bildet nichtlineare Wenn-dann-Regeln. Random Forest mittelt viele zufällig variierte Bäume; Gradient Boosting ergänzt schrittweise Bäume zur Fehlerkorrektur.',
     'Bäume benötigen normalerweise keine Skalierung. Tiefe, Mindestblattgröße und bei Ensembles Lernrate bzw. Anzahl der Bäume steuern die Komplexität.',
     'Set 8: 01_entscheidungsbaum_klassifikation.ipynb bis 04_gradient_boosting_und_modellvergleich.ipynb',
     '''
     from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor
     from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
     models = {
         "Baum": DecisionTreeClassifier(max_depth=4, random_state=42),
         "Forest": RandomForestClassifier(n_estimators=200,
             min_samples_leaf=2, random_state=42),
         "Boosting": GradientBoostingClassifier(n_estimators=100,
             learning_rate=.05, max_depth=2, random_state=42)}
     for name, model in models.items():
         model.fit(Xct, yct)
         print(name, "F1:", round(f1_score(yce, model.predict(Xce)), 3))
     tree_r = DecisionTreeRegressor(max_depth=3, min_samples_leaf=5,
                                    random_state=42).fit(Xrt, yrt)
     print("Regressionsbaum-MAE:",
           round(mean_absolute_error(yre, tree_r.predict(Xre)), 2))
     ''', notes=[('Klassifikation und Regression', 'Klassifikationsbäume reduzieren typischerweise Gini-Unreinheit oder Entropie, Regressionsbäume die Streuung der Zielwerte. Regressionsbäume liefern stückweise konstante Vorhersagen und extrapolieren Trends schlecht.'),
            ('Regeln visualisieren', 'from sklearn.tree import plot_tree; plot_tree(models["Baum"], max_depth=2, feature_names=["x1", "x2"], filled=True). Die Begrenzung im Plot kürzt nur die Anzeige, nicht das trainierte Modell.'),
            ('Kein Sieger aus diesem Einzeltest', 'Die drei festen Konfigurationen illustrieren unterschiedliche Verfahren. Für eine Modellauswahl dieselben CV-Splits und Suchbudgets verwenden; danach den reservierten Test einmal auswerten. Impurity-Importances können hochkardinale Merkmale bevorzugen.')])

page('SVM und nächste Nachbarn',
     'SVM sucht eine trennende Grenze mit kontrollierter Marge; mit RBF-Kernel auch nichtlinear. kNN entscheidet anhand ähnlicher Trainingspunkte und ist eine anschauliche lokale Baseline.',
     'Beide reagieren auf Merkmalsabstände. Skalierung gehört davor in die Pipeline; irrelevante Dimensionen können Nachbarschaften unbrauchbar machen.',
     'Set 9: 01_knn_pipeline_klassifikation.ipynb, 03_distanzen_gewichtung_und_regression.ipynb; Set 10: 01/02',
     '''
     from sklearn.svm import SVC, SVR
     from sklearn.neighbors import KNeighborsClassifier, KNeighborsRegressor
     for name, estimator in [
         ("SVM", SVC(C=1, gamma="scale", kernel="rbf")),
         ("kNN", KNeighborsClassifier(n_neighbors=7, weights="distance"))]:
         model = make_pipeline(StandardScaler(), estimator).fit(Xct, yct)
         print(name, "F1:", round(f1_score(yce, model.predict(Xce)), 3))
     for name, estimator in [
         ("SVR", SVR(C=500, epsilon=20)),
         ("kNN-Reg", KNeighborsRegressor(n_neighbors=7,
                                         weights="distance"))]:
         model = make_pipeline(StandardScaler(), estimator).fit(Xrt, yrt)
         print(name, "MAE:",
               round(mean_absolute_error(yre, model.predict(Xre)), 2))
     ''', notes=[('SVM-Parameter', 'Größeres C bestraft Trainingsverletzungen stärker. Größeres gamma macht die RBF-Wirkung lokaler und kann überfitten. SVR ignoriert Fehler innerhalb des epsilon-Schlauchs; epsilon wird in Zieleinheiten angegeben. Decision-Scores sind keine Wahrscheinlichkeiten.'),
            ('kNN-Parameter', 'Kleines k reagiert stärker auf Rauschen; großes k glättet. weights="distance" gewichtet nahe Punkte stärker. Für Minkowski-Distanz liefert p=1 Manhattan und p=2 Euklidisch. PCA oder Feature-Auswahl nur innerhalb der CV fitten.'),
            ('Kursresultat', 'Die SVM-Konfiguration auf den identischen Halbmond-Daten aus Set 10 liefert im gespeicherten Kurslauf Accuracy 0,976 und F1 0,975. Das ist die feste Ausgangskonfiguration vor der dortigen Parametersuche.')])

page('CRF für zusammenhängende Labels',
     'Conditional Random Fields vergeben Labels für ganze Sequenzen, etwa Person, Ort oder sonstiges Wort. Übergänge zwischen Nachbarlabels ergänzen die lokalen Merkmals-Scores.',
     'Viterbi findet die Sequenz mit dem höchsten Score. Forward berechnet die Normierung über alle Sequenzen; beides hat eine andere Aufgabe.',
     'Exkurs: exkurs-conditional-random-fields/01_crf_score_forward_viterbi.ipynb',
     '''
     # Kompakte Viterbi-Dekodierung, analog zum Kurs-Exkurs
     labels = np.array(["PER", "LOC", "O"])
     W = np.array([[1.4,-1,-1,-.5,0], [1,1.8,-1,-.5,-.2],
                   [-.8,-.4,1.2,1.4,.5]])
     A = np.array([[.4,-.6,.7],[-.5,.3,.6],[.2,1.1,.8]])
     tokens = ["Anna", "lebt", "in", "Berlin"]
     F = np.array([[float(w[0].isupper()),
         float(i>0 and tokens[i-1].lower()=="in"),
         float(w.lower() in {"lebt","wohnt","arbeitet"}),
         float(w.lower()=="in"), 1.] for i,w in enumerate(tokens)])
     E = F @ W.T
     delta, back = E[0].copy(), []
     for e in E[1:]:
         kandidaten = delta[:, None] + A
         back.append(kandidaten.argmax(axis=0))
         delta = e + kandidaten.max(axis=0)
     pfad = [int(delta.argmax())]
     for bp in reversed(back):
         pfad.append(int(bp[pfad[-1]]))
     print(list(zip(tokens, labels[pfad[::-1]].tolist())))
     print("Sequenzscore:", round(float(delta.max()), 2))
     ''', notes=[('Was dieses Beispiel tut', 'Die Gewichte W und A sind didaktisch vorgegeben, nicht trainiert. Der Kurs zeigt Sequenzscore, vollständige Aufzählung, Forward-Normierung und Viterbi. Das Rezept behauptet deshalb keine trainierte CRF-Qualität.'),
            ('Wahrscheinlichkeit', 'P(y|x) = exp(Score(x,y) - log Z(x)). log Z wird numerisch stabil mit logsumexp berechnet. Hoher roher Score ist ohne Normierung keine Wahrscheinlichkeit.'),
            ('Wie bewerten?', 'Nach kompletten Sätzen oder Dokumenten splitten. Token-F1 und bei Entitäten zusätzlich exakten Span-F1 berichten; ein fast richtiger Mehrwort-Ort kann tokenweise gut und auf Entitätsebene falsch sein.')])

page('Zeitreihen vorbereiten und verstehen',
     'Zeitreihen enthalten Reihenfolge, Trend und häufig saisonale Muster. Resampling, rollende Statistiken sowie ACF/PACF helfen, diese Struktur vor dem Modellieren zu verstehen.',
     'Jedes Merkmal muss zum Prognosezeitpunkt verfügbar sein. Ein gleitender Mittelwert mit zukünftigen Werten erzeugt für Prognosen Leakage.',
     'Set 12: 01_zeitreihen_darstellen_und_fenster_interaktiv.ipynb; 02_trend_saisonalitaet_und_autokorrelation.ipynb',
     '''
     from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
     index = pd.date_range("2025-01-01", periods=240, freq="D")
     rng = np.random.default_rng(42)
     serie = pd.Series(20 + .1*np.arange(240)
         + 3*np.sin(2*np.pi*np.arange(240)/30)
         + rng.normal(0, .3, 240), index=index)
     ts_train, ts_test = serie.iloc[:200], serie.iloc[200:]
     print("Train/Test:", len(ts_train), len(ts_test))
     print("Letztes Trainingsdatum:", ts_train.index[-1].date())
     fig, ax = plt.subplots(1, 3, figsize=(10, 2.6))
     ts_train.plot(ax=ax[0], title="Nur Training")
     plot_acf(ts_train.diff().dropna(), lags=40, ax=ax[1])
     plot_pacf(ts_train.diff().dropna(), lags=40, ax=ax[2], method="ywm")
     fig.tight_layout()
     # Vergangenheitsmerkmal für Prognose am Zeitpunkt t
     roll = serie.shift(1).rolling(7, min_periods=7).mean()
     ''', notes=[('Resampling', 'Set 12 Energie: pd.read_csv(..., parse_dates=["date"]).set_index("date").sort_index(). Danach rechts geschlossene Stundenintervalle mit label="right", closed="right": Appliances summieren, T1 und RH_1 mitteln, nur Stunden mit sechs Messungen verwenden.'),
            ('ACF und PACF', 'ACF misst Korrelation mit verzögerten Werten; PACF die verbleibende lineare Korrelation nach Berücksichtigung kürzerer Lags. Bei stationären idealen AR(p)- bzw. MA(q)-Prozessen helfen Abbruchmuster als Heuristik, ersetzen aber keine Validierung.'),
            ('Stationarität', 'Ein wachsender Mittelwert kann Differenzierung verlangen. Saisonalität bleibt nach einmaliger Differenzierung möglicherweise erhalten. Trend, Saison, fehlende Zeitpunkte und Messraster zuerst prüfen; Glättung ist keine neue unabhängige Messung.')])

page('AR MA ARMA und ARIMA',
     'AR nutzt vergangene Reihenwerte, MA vergangene Innovationsfehler; ARMA kombiniert beide. ARIMA differenziert zusätzlich d-mal, um etwa einen Trend zu behandeln.',
     'In statsmodels werden alle vier über ARIMA(order=(p,d,q)) formuliert. Ein MA(q)-Modell ist kein einfacher gleitender Mittelwert der beobachteten Werte.',
     'Set 12: 00_arma_arima_ganz_einfach.ipynb; 03b_ar_ma_und_arma.ipynb',
     '''
     from statsmodels.tsa.arima.model import ARIMA
     # Demo-Reihe von Seite 19; Parameter sind hier vorgegeben.
     fit_ts = ARIMA(ts_train, order=(2, 1, 1), trend="t").fit()
     forecast = fit_ts.get_forecast(steps=len(ts_test))
     mean = forecast.predicted_mean
     ci = forecast.conf_int(alpha=.05)
     naive = np.repeat(ts_train.iloc[-1], len(ts_test))
     print("ARIMA-MAE:", round(mean_absolute_error(ts_test, mean), 3))
     print("Naiv-MAE:", round(mean_absolute_error(ts_test, naive), 3))
     fig, ax = plt.subplots(figsize=(8, 2.8))
     ts_train.iloc[-60:].plot(ax=ax, label="Training")
     ts_test.plot(ax=ax, label="Test")
     mean.plot(ax=ax, label="Prognose", color="#f15a24")
     ax.fill_between(ci.index, ci.iloc[:,0], ci.iloc[:,1], alpha=.2)
     ax.set(ylabel="Messwert"); ax.legend(); fig.tight_layout()
     ''', table=[('Verfahren', 'order / Bedeutung'), ('AR(p)', '(p,0,0): lineare Abhängigkeit von p Vorwerten'),
     ('MA(q)', '(0,0,q): q vergangene Innovationsfehler'), ('ARMA(p,q)', '(p,0,q): Werte und Innovationsfehler'),
     ('ARIMA(p,d,q)', '(p,d,q): ARMA auf differenzierter Reihe')],
     notes=[('Trend und Unsicherheit', 'Bei d=1 erlaubt trend="t" in dieser ARIMA-Formulierung einen Drift in der Originalreihe. Prognoseintervalle beruhen auf Modellannahmen; 95 % bedeutet keine garantierte Abdeckung bei Strukturbrüchen.'),
            ('Auswahl und Diagnostik', 'p, d und q per Zeitvalidierung vergleichen. AIC/BIC nur für vergleichbare Fits ergänzend nutzen. Residuenplot und ACF prüfen. Für saisonale Dynamik seasonal_order=(P,D,Q,s) erwägen; ein tägliches Muster ist nicht durch d=1 erledigt.')])

page('Lags Backtesting und exogene Größen',
     'Lag-Modelle machen aus der Zeitreihe eine überwachte Aufgabe. Backtesting wiederholt die Bewertung an historischen Prognoseursprüngen; exog ergänzt Größen, die für den Prognosehorizont bereits bekannt sind.',
     'Eine feste 40-Tage-Prognose und täglich aktualisierte Ein-Schritt-Prognosen sind verschiedene Aufgaben. Den Horizont und die verfügbare Information immer nennen.',
     'Set 12: 03_zeitlicher_split_lags_und_backtesting.ipynb; 00_b und 00_c',
     '''
     from sklearn.model_selection import TimeSeriesSplit
     from sklearn.linear_model import Ridge
     tab = pd.DataFrame({"y": serie})
     for lag in [1, 2, 7, 30]:
         tab[f"lag{lag}"] = serie.shift(lag)
     tab = tab.dropna()
     # Ein-Schritt-Backtest: vorherige echte Werte sind verfügbar.
     dev = tab.loc[tab.index <= ts_train.index[-1]]
     cv = TimeSeriesSplit(n_splits=3, test_size=20)
     errors = []
     for tr, va in cv.split(dev):
         m = make_pipeline(StandardScaler(), Ridge(alpha=1))
         m.fit(dev.iloc[tr].drop(columns="y"), dev.iloc[tr].y)
         p = m.predict(dev.iloc[va].drop(columns="y"))
         errors.append(mean_absolute_error(dev.iloc[va].y, p))
     print("Fold-MAE:", np.round(errors, 3))
     print("Mittlerer MAE:", round(np.mean(errors), 3))
     ''', notes=[('Warum das kein fester Mehrschritt-Forecast ist', 'Die Lag-Zeilen der Validierung enthalten jeweils zuvor beobachtete echte Werte. Das entspricht fortlaufend aktualisierten Ein-Schritt-Vorhersagen. Bei einem Forecast ohne neue Messwerte müssen Lags rekursiv mit Prognosen gefüllt oder direkte Horizontmodelle gelernt werden.'),
            ('Exogene Größen im Kurs', 'ARIMA(training, order=(1,0,1), exog=merkmale_training).fit(); anschließend get_forecast(steps=H, exog=merkmale_zukunft). Ein Produktionsplan kann bekannt sein; das tatsächlich gemessene Wetter oder Sensorsignal von morgen normalerweise nicht.'),
            ('Schrittweise aktualisieren', 'Erst forecast(steps=1, exog=naechste_merkmale), dann echten Wert beobachten, dann fit.append(neuer_wert, exog=naechste_merkmale, refit=False). append aktualisiert dabei den Zustand, ohne die Parameter neu zu schätzen. Bei h-Schritt-Zielen Trainingsgrenze und ggf. gap entsprechend absichern.')])

page('MLP für Tabellen und Regression',
     'Ein Multi-Layer Perceptron lernt nichtlineare Merkmalskombinationen. MLPRegressor liefert Zahlen, MLPClassifier Klassen; mehrere versteckte Schichten bilden die Grundlage tiefer Netze.',
     'Eingaben skalieren und Overfitting an Validierungsdaten beobachten. Early Stopping beendet das Training, wenn die Validierung nicht mehr besser wird.',
     'Set 13: 01_mlp_regression.ipynb; 02_mlp_klassifikation.ipynb',
     '''
     from sklearn.neural_network import MLPRegressor, MLPClassifier
     rng = np.random.default_rng(42)
     Xm = np.sort(rng.uniform(-3.5, 3.5, 500)).reshape(-1, 1)
     ym = 1.3*np.sin(1.4*Xm[:,0]) + .25*Xm[:,0]
     ym += rng.normal(0, .22, len(Xm))
     a, b, c, d = train_test_split(Xm, ym, test_size=.25, random_state=42)
     mlp = make_pipeline(StandardScaler(), MLPRegressor(
         hidden_layer_sizes=(32,16), learning_rate_init=.01,
         alpha=.001, batch_size=32, max_iter=1200,
         early_stopping=True, validation_fraction=.15,
         n_iter_no_change=40, random_state=42))
     mlp.fit(a, c)
     p = mlp.predict(b)
     print("MAE:", round(mean_absolute_error(d, p), 3),
           "R2:", round(r2_score(d, p), 3))
     print("Epochen:", mlp[-1].n_iter_)
     fig, ax = plt.subplots(figsize=(7, 2.6))
     ax.plot(mlp[-1].loss_curve_)
     ax.set(xlabel="Epoche", ylabel="Trainings-Loss")
     fig.tight_layout()
     ''', notes=[('Klassifikation', 'MLPClassifier(hidden_layer_sizes=(32,16), early_stopping=True, random_state=42) in derselben Skalierungs-Pipeline verwenden. Bei Multiclass predict_proba mit einer Wahrscheinlichkeit je Klasse; Bewertung wie auf Seite 11.'),
            ('Parameter', 'hidden_layer_sizes legt Breite und Anzahl der Hidden Layer fest; learning_rate_init die Schrittweite von Adam, alpha die L2-Strafe, batch_size die Beispiele pro Update. Training und Validierung gemeinsam ansehen; allein eine fallende Trainings-Loss-Kurve reicht nicht.'),
            ('Gruppen und Zeit', 'Das interne early_stopping=True verwendet einen eigenen Zufallssplit. Bei Zeitreihen oder Gruppen ist das nicht automatisch passend. Dann eine explizite Validierung mit passender Struktur und kontrollierter Trainingsschleife verwenden.')])

page('CNN mit PyTorch',
     'Convolutional Neural Networks nutzen die räumliche Struktur von Bildern. Faltungen lernen lokale Filter, ReLU erzeugt Nichtlinearität und Pooling reduziert die räumliche Auflösung.',
     'CrossEntropyLoss erwartet rohe Logits und Klassenindizes als long. Vor der Loss kein Softmax anwenden; für Wahrscheinlichkeiten erst nach dem Training.',
     'Set 14: 02_cnn_filter_pooling_und_feature_maps.ipynb; cv_tools.py',
     '''
     import torch
     sys.path.insert(0, str(ROOT / "set14-neuronale-netze-nn2"))
     from cv_tools import (cpu_setup, ziffern_split, loader,
         KleinesCNN, trainiere, auswerten, lernkurven)
     cpu_setup()
     bilder, labels_nn, split = ziffern_split()  # 60/20/20
     tr_loader = loader(bilder[split["train"]],
         labels_nn[split["train"]], shuffle=True)
     va_loader = loader(bilder[split["val"]], labels_nn[split["val"]])
     te_loader = loader(bilder[split["test"]], labels_nn[split["test"]])
     cnn = KleinesCNN()
     hist = trainiere(cnn, tr_loader, va_loader, epochen=20, lr=.003)
     metriken, probs_nn, echte_nn = auswerten(cnn, te_loader)
     print("Test:", {k: round(v, 3) for k,v in metriken.items()})
     print("Eingabe:", tuple(bilder[:2].shape))
     lernkurven(hist)
     ''', notes=[('Training in sechs Schritten', 'modell.train(); optimizer.zero_grad(); logits = modell(x); loss = loss_fn(logits,y); loss.backward(); optimizer.step(). cv_tools.trainiere führt diese Schritte für alle Batches aus und lädt anschließend die Gewichte mit dem niedrigsten Validierungs-Loss.'),
            ('Formen im Kurs', 'Digits enthält 8×8-Graubilder: Batchform (N,1,8,8), Pixel geteilt durch 16. Zwei Conv-ReLU-Pooling-Blöcke erzeugen (N,16,2,2), danach Flatten und Linear(64,10). Das kleine CNN hat 1898 trainierbare Parameter.'),
            ('Auswerten', 'modell.eval() schaltet Trainingsverhalten um; torch.inference_mode() verhindert Gradientenaufbau. Gewichte nicht anhand des Tests auswählen. Lernkurven, Konfusionsmatrix und falsch erkannte Bilder ergänzen; bei realen Bildern nach Aufnahmequelle splitten.')])

page('Transfer Learning und Modellkopf',
     'Transfer Learning verwendet einen bereits gelernten Merkmalsextraktor und trainiert nur einen kleinen neuen Kopf. Im Kurs liefert ein eingefrorenes MobileNet Bildmerkmale für die Ziffernklassifikation.',
     'Einfrieren betrifft Gewichte und zustandsbehaftete Schichten wie BatchNorm. Eingabeaufbereitung und Feature-Skalierung sind Teil des Modells.',
     'Set 14: 03_transfer_learning_nur_der_kopf.ipynb',
     '''
     # Im Transfer-Notebook nach features=extrahiere_features(...):
     train_features = features[split["train"]]
     with torch.no_grad():
         modell.feature_mean.copy_(train_features.mean(0))
         modell.feature_std.copy_(train_features.std(0).clamp_min(1e-4))
     z = (features-modell.feature_mean) / modell.feature_std
     tl = loader(z[split["train"]], labels[split["train"]], shuffle=True)
     vl = loader(z[split["val"]], labels[split["val"]])
     test_loader = loader(z[split["test"]], labels[split["test"]])
     historie = trainiere(modell.head, tl, vl, epochen=24, lr=.003)
     metriken, probs, echte = auswerten(modell.head, test_loader)
     print(metriken)
     ''', run=False, notes=[('Voraussetzung des Ausschnitts', 'Dieses Rezept ist ein gezielter Ausschnitt aus dem Transfer-Notebook und wird dort nach der Feature-Extraktion ausgeführt. modell ist FrozenMobileNet, features sind dessen unveränderte Backbone-Ausgaben; bilder, labels, split und Hilfsfunktionen sind dort definiert. Der begleitende Cheat-Sheet-Lauf führt diesen Ausschnitt nicht automatisch aus.'),
            ('Aufbereitung', 'Die Hilfsfunktion mobilenet_bilder macht aus 8×8-Graubildern RGB-Eingaben im erwarteten 224×224-Format und verwendet die zum Gewichtesatz passenden Normalisierungen. Das Hochskalieren erzeugt keine zusätzlichen Bilddetails.'),
            ('Ergebnis prüfen', 'Das Kursnotebook verifiziert, dass Backbone-Gewichte und BatchNorm-Puffer unverändert bleiben und vollständiges Bildmodell und gecachte Features dieselben Vorhersagen liefern. Bei geändertem Backbone oder Preprocessing muss der Feature-Cache erneuert werden.'),
            ('Einmaliger Download', 'Die ImageNet-Gewichte werden beim ersten Lauf geladen; danach ist der lokale Cache nutzbar. Ob Transfer auf die kleinen Ziffernbilder hilft, wird am gleichen Train/Val/Test-Split mit MLP und CNN geprüft.')])

page('PCA für Merkmalsreduktion',
     'PCA erzeugt orthogonale lineare Richtungen maximaler Varianz. Sie kann korrelierte Merkmale verdichten, Rauschen reduzieren und eine zweidimensionale Ansicht ermöglichen.',
     'Große Varianz ist nicht automatisch wichtig für das Ziel. PCA bei überwachter Bewertung innerhalb der Pipeline ausschließlich am Training lernen.',
     'Set 11: 01_pca_und_merkmalsreduktion.ipynb; Set 3: 06_pca_sensor_features.ipynb',
     '''
     from sklearn.decomposition import PCA
     # Iris nur zur explorativen 2D-Darstellung; keine Testgüte.
     scaled = StandardScaler().fit_transform(iris.data)
     pca = PCA(n_components=2, random_state=42)
     z = pca.fit_transform(scaled)
     print("Varianzanteile:", np.round(pca.explained_variance_ratio_, 3))
     print("Summe:", round(pca.explained_variance_ratio_.sum(), 3))
     fig, ax = plt.subplots(figsize=(7, 2.7))
     ax.scatter(z[:,0], z[:,1], c=iris.target, cmap="viridis", s=16)
     ax.set(xlabel="PC 1", ylabel="PC 2"); fig.tight_layout()
     # Für Vorhersagen: make_pipeline(StandardScaler(),
     #     PCA(n_components=.95), LogisticRegression(...))
     # anschließend per CV innerhalb der Entwicklungsdaten bewerten.
     ''', notes=[('Ergebnis lesen', 'explained_variance_ratio_ enthält den Anteil pro Komponente. np.cumsum(...) ergibt die kumulierte erklärte Varianz. n_components=.95 wählt bei geeigneter Solverwahl genügend Komponenten für mindestens 95 % Trainingsvarianz.'),
            ('Loadings und Rückprojektion', 'components_ enthält die Richtungen im Merkmalsraum. pca.inverse_transform(z) rekonstruiert die skalierten Eingaben näherungsweise. Vorzeichen von Komponenten können wechseln, ohne dass sich ihre Bedeutung ändert.'),
            ('Skalierung bewusst entscheiden', 'Standardisierung gewichtet jede Ausgangsvariable nach ihrer Streuung; unskalierte PCA bevorzugt große Skalen. Welche Variante fachlich sinnvoll ist, hängt von Einheiten und Messrauschen ab. Farbig getrennte Klassen im PCA-Plot sind keine validierte Klassifikation.')])

page('NMF und t-SNE',
     'NMF zerlegt nichtnegative Daten in additive Bausteine und deren Gewichte. t-SNE erstellt eine nichtlineare 2D-Ansicht, die vor allem lokale Nachbarschaften sichtbar machen soll.',
     'NMF ist eine Rekonstruktionsmethode; t-SNE eine explorative Darstellung. Abstände zwischen t-SNE-Inseln und Inselgrößen nicht als globale Geometrie interpretieren.',
     'Set 11: 02_nmf_und_tsne.ipynb',
     '''
     from sklearn.decomposition import NMF, PCA
     from sklearn.manifold import TSNE, trustworthiness
     # Additive nichtnegative Spektren wie im Kurs, kompakt simuliert.
     wl = np.linspace(400, 800, 80)
     H = np.array([np.exp(-.5*((wl-c)/25)**2) for c in [470,590,710]])
     rng = np.random.default_rng(42)
     spectra = rng.gamma(1.8, 1, (240,3)) @ H
     nmf = NMF(n_components=3, init="nndsvda", max_iter=2000,
               tol=.001, random_state=42)
     Wn = nmf.fit_transform(spectra)
     print("W / H:", Wn.shape, nmf.components_.shape)
     print("Rekonstruktionsfehler:", round(nmf.reconstruction_err_, 3))
     digits = load_digits()
     dx = StandardScaler().fit_transform(digits.data[:600])
     reduced = PCA(n_components=30, random_state=42).fit_transform(dx)
     embedded = TSNE(n_components=2, perplexity=30, init="pca",
         learning_rate="auto", random_state=42).fit_transform(reduced)
     print("Trustworthiness:", round(trustworthiness(reduced, embedded), 3))
     fig, ax = plt.subplots(figsize=(7, 2.6))
     ax.scatter(embedded[:,0], embedded[:,1], c=digits.target[:600],
                cmap="tab10", s=10)
     ax.set(title="t-SNE: Digits, explorativ"); fig.tight_layout()
     ''', notes=[('NMF-Voraussetzungen', 'Alle Eingaben müssen >= 0 sein. Zentrierte Standardisierung passt daher nicht davor. X ≈ W @ H; Komponentenanzahl und Rekonstruktionsfehler gemeinsam mit fachlicher Interpretierbarkeit prüfen. Nichtnegativität durch Abschneiden ist nur dann sinnvoll, wenn fachlich begründet.'),
            ('t-SNE-Voraussetzungen', 'perplexity muss kleiner als die Zahl der Datenpunkte sein. Mehrere Seeds und Perplexities prüfen; sklearn-t-SNE besitzt keine normale transform-Methode für neue Daten. Trustworthiness bewertet lokale Nachbarschaftserhaltung, keine Klassen- oder Clusterwahrheit.')])

page('KMeans und hierarchische Cluster',
     'KMeans sucht kompakte Gruppen um Zentren. Agglomeratives Clustering führt schrittweise nahe Gruppen zusammen und macht eine hierarchische Struktur zugänglich.',
     'Cluster sind gefundene Strukturen, keine automatisch bekannten Klassen. Skalierung, Distanz und gewählte Clusterzahl verändern das Ergebnis.',
     'Set 11: 03_kmeans_und_clusterbewertung.ipynb; 04_hierarchisch_dbscan_und_gmm.ipynb',
     '''
     from sklearn.datasets import make_blobs
     from sklearn.cluster import KMeans, AgglomerativeClustering
     from sklearn.metrics import silhouette_score, adjusted_rand_score
     blobs, hidden = make_blobs(n_samples=400, centers=4,
         cluster_std=.8, random_state=42)
     zb = StandardScaler().fit_transform(blobs)
     km = KMeans(n_clusters=4, n_init=10, random_state=42)
     lab = km.fit_predict(zb)
     hierarchical = AgglomerativeClustering(n_clusters=4, linkage="ward")
     lab_h = hierarchical.fit_predict(zb)
     print("Silhouette KMeans:", round(silhouette_score(zb, lab), 3))
     print("Silhouette Hierarchie:", round(silhouette_score(zb, lab_h), 3))
     print("ARI zur simulierten Wahrheit:",
           round(adjusted_rand_score(hidden, lab), 3))
     fig, ax = plt.subplots(figsize=(7, 2.7))
     ax.scatter(zb[:,0], zb[:,1], c=lab, cmap="tab10", s=13)
     ax.scatter(km.cluster_centers_[:,0], km.cluster_centers_[:,1],
                marker="x", c="black", s=80)
     ax.set(xlabel="z1", ylabel="z2"); fig.tight_layout()
     ''', notes=[('Clusterzahl wählen', 'Elbow-Plot mit km.inertia_ für mehrere k und Silhouette-Plot ergänzen. Silhouette liegt zwischen -1 und 1, benötigt 2 bis n-1 Cluster und bevorzugt häufig kompakte, getrennte Gruppen. Die höchste Zahl ist nicht automatisch die fachlich beste Lösung.'),
            ('Hierarchie', 'Ward minimiert den Zuwachs innerhalb der Cluster und verwendet euklidische Distanzen. Andere Linkages beantworten andere Distanzfragen. sklearn-AgglomerativeClustering besitzt keine gewöhnliche predict-Methode für neue Punkte.'),
            ('Labels nur nachträglich', 'adjusted_rand_score ist invariant gegenüber umbenannten Cluster-IDs und braucht externe Referenzlabels. Hier sind hidden nur zur Illustration bekannt; sie gehen nicht in fit ein. Ein gutes Ergebnis auf make_blobs ist keine reale Anwendungsgarantie.')])

page('DBSCAN und Gaussian Mixtures',
     'DBSCAN findet dichte Gebiete beliebiger Form und markiert isolierte Punkte als Noise. Gaussian Mixture Models beschreiben Daten als Mischung mehrerer Normalverteilungen und liefern weiche Zugehörigkeiten.',
     'DBSCAN bestimmt Noise und Cluster aus eps und min_samples. GMM benötigt eine Komponentenanzahl und Annahmen über die Kovarianzstruktur.',
     'Set 11: 04_hierarchisch_dbscan_und_gmm.ipynb',
     '''
     from sklearn.cluster import DBSCAN
     from sklearn.mixture import GaussianMixture
     from sklearn.metrics import silhouette_score
     moon, _ = make_moons(n_samples=620, noise=.075, random_state=42)
     zm = StandardScaler().fit_transform(moon)
     db = DBSCAN(eps=.22, min_samples=8).fit(zm)
     lab_db = db.labels_
     mask = lab_db != -1
     k = len(set(lab_db[mask]))
     print("Cluster:", k, "Noise-Anteil:", round((~mask).mean(), 3))
     if 1 < k < mask.sum():
         print("Silhouette ohne Noise:",
               round(silhouette_score(zm[mask], lab_db[mask]), 3))
     gmm = GaussianMixture(n_components=4, covariance_type="full",
                           n_init=5, random_state=42).fit(zb)
     print("GMM Zugehörigkeiten:\\n", np.round(gmm.predict_proba(zb[:3]), 3))
     print("BIC:", round(gmm.bic(zb), 1))
     ''', notes=[('DBSCAN einstellen', 'eps ist ein Radius in der gewählten skalierten Distanz, min_samples die Mindestzahl einschließlich des Punkts selbst. k-Distanz-Plot und Stabilität über mehrere Parameter prüfen. Bei stark wechselnder Dichte kann ein einzelnes eps scheitern.'),
            ('Noise ist keine Klasse', 'Label -1 bezeichnet Noise. Beim Silhouette-Score Noise ausschließen und gleichzeitig Noise-Anteil sowie Clusterzahl nennen; andernfalls kann eine Lösung durch das Aussortieren schwieriger Punkte besser aussehen.'),
            ('GMM bewerten', 'Kleineres BIC/AIC bevorzugt bei gleichen Daten eine bessere Anpassung nach Komplexitätsstrafe. predict_proba sind modellinterne Zugehörigkeiten, keine extern validierten Klassenwahrscheinlichkeiten. Ein GMM-Cluster ist ellipsoid; mehrere Komponenten können zusammen eine fachliche Gruppe beschreiben.')])

page('Anomalien und Schwellenwerte',
     'Anomalieerkennung bewertet, wie ungewöhnlich ein Punkt gegenüber einer Referenz ist. Isolation Forest isoliert seltene Strukturen; OneClassSVM grenzt eine Normalregion ein.',
     'Score-Richtung ausdrücklich prüfen. Einen Schwellenwert an unabhängigen Validierungsdaten festlegen und Fehlalarme sowie verpasste Anomalien getrennt berichten.',
     'Set 11: 05_anomalieerkennung_und_thresholds.ipynb',
     '''
     from sklearn.ensemble import IsolationForest
     from sklearn.metrics import precision_score, recall_score
     rng = np.random.default_rng(42)
     normal_train = rng.normal(size=(500,2))
     normal_val = rng.normal(size=(200,2))
     test_normal = rng.normal(size=(200,2))
     test_bad = rng.uniform(4, 7, size=(20,2))
     detector = IsolationForest(n_estimators=200, random_state=42)
     detector.fit(normal_train)
     # Bei score_samples: kleiner = ungewöhnlicher; Vorzeichen drehen.
     val_score = -detector.score_samples(normal_val)
     threshold = np.quantile(val_score, .99)
     test_x = np.vstack([test_normal, test_bad])
     test_y = np.r_[np.zeros(200), np.ones(20)]
     score = -detector.score_samples(test_x)
     flag = score >= threshold
     print("Precision:", round(precision_score(test_y, flag), 3),
           "Recall:", round(recall_score(test_y, flag), 3))
     print("Fehlalarmrate normal:", round(flag[:200].mean(), 3))
     ''', notes=[('Was der Quantilwert bedeutet', 'Das 99%-Quantil der normalen Validierung setzt etwa 1 % dieser Referenz oberhalb der Schwelle. Das garantiert keine 1 % Fehlalarme auf zukünftigen Daten. Hier sind die Anomalien absichtlich stark getrennt und damit leicht erkennbar.'),
            ('Andere Verfahren', 'OneClassSVM benötigt typischerweise Standardisierung; nu steuert die Lösung, ist aber keine garantierte zukünftige Fehlalarmrate. GMM-Dichte oder PCA-Rekonstruktionsfehler können ebenfalls Scores liefern, wenn ihre Modellannahmen passen.'),
            ('Betrieb', 'Normale Änderungen von Last, Umgebung und Sensoralter können wie Fehler aussehen. Alarmrate pro Zeit, Verzögerung bis zur Erkennung und Fehlalarme pro Maschine sind oft relevanter als ein einzelner zeilenweiser F1.')])

page('Erklären speichern und wiederverwenden',
     'Eine Vorhersage ist erst reproduzierbar, wenn Vorverarbeitung, Modell, Spalten und Umgebung zusammenpassen. Erklärungen helfen beim Plausibilitätscheck, ersetzen aber keinen passenden Split.',
     'Die vollständige Pipeline speichern. Einen eigenen Transformer über eine importierbare Python-Datei verfügbar halten und nach dem Laden die Vorhersagen vergleichen.',
     'Set 5: 05_xai_koeffizienten.ipynb; Set 15: 01/02/03; custom_transformer_einfach.py',
     '''
     from sklearn.inspection import permutation_importance
     # Diagnose auf separaten Bewertungsdaten, keine kausale Aussage.
     importance = permutation_importance(iris_model, ie, je,
         scoring="accuracy", n_repeats=10, random_state=42)
     print(pd.Series(importance.importances_mean,
                     index=iris.data.columns).round(3))

     import joblib
     artifact = ROOT / "tmp/ml-cheatsheet/iris_pipeline.joblib"
     artifact.parent.mkdir(parents=True, exist_ok=True)
     joblib.dump(iris_model, artifact)
     loaded = joblib.load(artifact)
     print("Vorhersagen identisch:", np.array_equal(
         iris_model.predict(ie), loaded.predict(ie)))
     ''', notes=[('Interpretation', 'Permutation Importance misst den Score-Verlust beim Mischen eines Eingabemerkmals. Bei korrelierten Merkmalen kann Wichtigkeit verteilt oder verdeckt sein. Bei einer kompletten Pipeline werden hier die ursprünglichen Iris-Eingaben permutiert, nicht die ergänzten Flächen einzeln.'),
            ('Modellpaket', 'Zusätzlich Spaltennamen und Reihenfolge, Klassenbezeichnungen, Paketversionen, Trainingsdatenversion und Bewertungsprotokoll sichern. joblib/pickle nur aus vertrauenswürdigen Quellen laden. Eigene Klassen und kompatible Bibliotheken müssen beim Laden verfügbar sein.'),
            ('PyTorch', 'torch.save(modell.state_dict(), pfad) speichert Gewichte; die Architektur muss separat rekonstruiert werden. Danach load_state_dict(torch.load(pfad, map_location="cpu", weights_only=True), strict=True) und modell.eval(). Preprocessing, Klassen und Modellkonfiguration ebenfalls mitführen.'),
            ('Offizielle API-Referenzen', 'scikit-learn.org/stable/common_pitfalls.html; scikit-learn.org/stable/modules/generated/sklearn.manifold.TSNE.html; statsmodels.org/stable/generated/statsmodels.tsa.arima.model.ARIMA.html. Kursdateien sind die primäre Zuordnung der Beispiele; Stand des Hefts: 20.11.2026.')])

page('Ein eigener Transformer im Detail',
     'TransformerMixin ergänzt fit_transform, BaseEstimator die Parameter-Schnittstelle für Pipelines und Parametersuchen. Das folgende Minimalbeispiel zeigt die Rechenregel aus Set 15 vollständig.',
     'transform verändert die übergebene Tabelle nicht. Eingaben müssen dieselben erwarteten Spalten enthalten; die ergänzten Merkmale bleiben für neue Daten identisch definiert.',
     'Set 15: custom_transformer_einfach.py; 02b_sklearn_eigener_transformer_schritt_fuer_schritt.ipynb',
     '''
     from sklearn.base import BaseEstimator, TransformerMixin

     class FlaechenDemo(TransformerMixin, BaseEstimator):
         def fit(self, X, y=None):
             return self  # feste Regel, keine Statistik zu lernen

         def transform(self, X):
             out = X.copy()
             out["kelch_flaeche"] = (X["sepal length (cm)"]
                                      * X["sepal width (cm)"])
             out["blueten_flaeche"] = (X["petal length (cm)"]
                                        * X["petal width (cm)"])
             return out

     demo = FlaechenDemo()
     erweitert = demo.fit_transform(iris.data.iloc[:2])
     print("Vorher:", iris.data.iloc[:2].shape,
           "Nachher:", erweitert.shape)
     print(erweitert[["kelch_flaeche", "blueten_flaeche"]].round(2))
     ''', notes=[('Warum in einer .py-Datei?', 'Eine in einer Notebookzelle definierte Klasse ist beim Laden in einem frischen Prozess nicht automatisch verfügbar. Für das gespeicherte Modell wird auf Seite 6 daher die importierbare Kursklasse FlaechenMerkmale aus custom_transformer_einfach.py verwendet.'),
            ('Wenn die Regel Parameter hat', 'Optionen als gleichnamige Attribute in __init__ speichern, ohne dort Daten zu verarbeiten. Aus Training gelernte Attribute in fit üblicherweise mit einem Unterstrich am Ende benennen und in transform wiederverwenden.'),
            ('Fehlende Werte und Reihenfolge', 'Fehlt eine Länge oder Breite, wird auch das Produkt NaN. Im Rezept folgt deshalb die Imputation auf die feste Feature-Bildung. Ob zuerst Rohgrößen imputiert oder Produkte imputiert werden sollen, ist eine bewusste fachliche Entscheidung.')])

from ml_bilder import erweitern
PAGES = erweitern(PAGES)
