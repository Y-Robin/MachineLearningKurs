"""Zusätzliche Bildseiten mit reproduzierbaren Diagnoseplots zum Kurs."""
from textwrap import dedent
import re

def erweitern(original):
    extra = {}
    def bild(n, title, intro, principle, source, code, notes, height=200):
        extra.setdefault(n, []).append(dict(title=title, intro=intro,
            principle=principle, source=source, code=dedent(code).strip(),
            notes=notes, table=[], setup='', run=True, visual=True,
            figure_height=height))

    bild(3, 'Fehlende Werte sichtbar machen',
        'Vor dem Modellieren prüfen wir Vollständigkeit und Muster fehlender Werte. Balken zeigen die Häufigkeit, eine Fehlwertmatrix zeigt, ob Spalten in denselben Zeilen ausfallen.',
        'Ein fehlender Wert ist nicht automatisch zufällig. Muster erst verstehen, dann eine Imputationsstrategie festlegen.',
        'Set 3: 02_eda_palmer_penguins.ipynb; Set 4: 01_daten_verstehen_und_visualisieren.ipynb',
        '''
        cols = ["bill_length_mm", "bill_depth_mm", "flipper_length_mm",
                "body_mass_g", "sex"]
        missing = penguins[cols].isna()
        fig, ax = plt.subplots(1, 2, figsize=(9, 3.1))
        (100*missing.mean()).plot.barh(ax=ax[0], color="#f15a24")
        ax[0].set(xlabel="Fehlende Werte [%]", title="Anteil je Spalte")
        ax[1].imshow(missing, aspect="auto", cmap="Greys", interpolation="nearest")
        ax[1].set_xticks(range(len(cols)), ["Länge", "Tiefe", "Flosse", "Masse", "Sex"])
        ax[1].set(ylabel="Zeile im Datensatz", title="Schwarz = fehlt")
        fig.tight_layout()
        ''', [('Bild lesen', 'sex enthält mehr Fehlwerte als die Körpermaße. Bei mehreren Körpermaßen liegen Fehlwerte in denselben Zeilen. Die Zeilenreihenfolge kann Hinweise auf gemeinsame Messausfälle geben.'),
              ('Nächster Schritt', 'isna().sum() liefert die absoluten Zahlen. Vor Imputation klären, ob ein Messfehler, ein bestimmter Standort oder ein systematischer Ausfall dahintersteckt. Für Modellentscheidungen nur Trainingsdaten explorieren.')])

    bild(3, 'Histogramme und Verteilungen',
        'Histogramme zeigen Schiefe, Häufungen und mehrere Gipfel. Gleiche Bins und Achsen helfen, Gruppen zu vergleichen; Rohdaten und Gruppenmischung können unterschiedlich aussehen.',
        'Ein zweiter Gipfel kann eine echte Untergruppe statt eines Ausreißers sein. Verteilungen deshalb auch nach fachlichen Gruppen betrachten.',
        'Set 3: 02_eda_palmer_penguins.ipynb; 03_eda_wine_quality.ipynb',
        '''
        fig, ax = plt.subplots(1, 2, figsize=(9, 3.1))
        bins = np.arange(2500, 6501, 300)
        for art, gruppe in penguins.groupby("species"):
            ax[0].hist(gruppe.body_mass_g.dropna(), bins=bins,
                       alpha=.5, label=art, edgecolor="white")
        ax[0].set(xlabel="Körpermasse [g]", ylabel="Anzahl")
        ax[0].legend(fontsize=8)
        ax[1].hist(wein["residual sugar"], bins=30, color="#f15a24")
        ax[1].set(xlabel="Restzucker [g/L]", ylabel="Anzahl",
                  title="Rotwein: rechtsschiefe Verteilung")
        fig.tight_layout()
        ''', [('Bild lesen', 'Gentoo liegt bei der Körpermasse überwiegend weiter rechts. Restzucker ist rechtsschief: wenige hohe Werte verlängern den rechten Rand; der Mittelwert kann deshalb stärker als der Median verschoben sein.'),
              ('Code variieren', 'Mit density=True wird die Dichte statt der Anzahl gezeigt. Für positive rechtsschiefe Größen kann eine fachlich passende Log-Transformation helfen; sie muss anschließend auch bei neuen Daten identisch angewendet werden.')])

    bild(3, 'Boxplots und einzelne Messpunkte',
        'Boxplots vergleichen Lage und Streuung zwischen Gruppen. Zusätzliche Messpunkte zeigen Stichprobengröße, Häufungen und die Verteilung, die eine Box allein verbergen kann.',
        'Ein Punkt außerhalb der Whisker ist nach der Boxplot-Regel auffällig. Er ist dadurch noch kein falscher Messwert und wird nicht automatisch gelöscht.',
        'Set 3: 02_eda_palmer_penguins.ipynb; 03_eda_wine_quality.ipynb',
        '''
        arten = sorted(penguins.species.dropna().unique())
        fig, ax = plt.subplots(1, 2, figsize=(9, 3.1))
        werte = [penguins.loc[penguins.species==a, "body_mass_g"].dropna()
                 for a in arten]
        ax[0].boxplot(werte, tick_labels=arten, showfliers=False)
        rng = np.random.default_rng(42)
        for i, vals in enumerate(werte, 1):
            ax[0].scatter(i+rng.normal(0,.055,len(vals)), vals,
                          s=6, alpha=.25, color="#f15a24")
        ax[0].set(ylabel="Körpermasse [g]", title="Box + Rohdaten")
        qual = sorted(wein.quality.unique())
        ax[1].boxplot([wein.loc[wein.quality==q, "alcohol"] for q in qual],
                      tick_labels=qual)
        ax[1].set(xlabel="Qualität", ylabel="Alkohol [% vol]",
                  title="Standard-Whisker: 1,5 × IQR")
        fig.tight_layout()
        ''', [('Box lesen', 'Die Linie ist der Median, die Box reicht vom 25%- bis zum 75%-Quantil. IQR ist die Boxhöhe. Whisker enden bei den äußersten Datenpunkten innerhalb der Grenzen Q1 - 1,5 IQR und Q3 + 1,5 IQR.'),
              ('Ergebnis einordnen', 'Höhere Weinqualität geht hier tendenziell mit höherem Alkoholgehalt einher, aber die Verteilungen überlappen. Aus dieser EDA folgt weder eine perfekte Vorhersage noch ein kausaler Effekt.')])

    bild(3, 'Scatterplots nach Gruppen',
        'Scatterplots zeigen Beziehungen zwischen zwei numerischen Merkmalen. Farbe und Transparenz machen Gruppen, Überlagerungen und Unterschiede in Steigung oder Streuung erkennbar.',
        'Einen Zusammenhang in der Gesamttabelle immer auch innerhalb plausibler Gruppen ansehen. Mischungen können Korrelationen verstärken, abschwächen oder umkehren.',
        'Set 3: 02_eda_palmer_penguins.ipynb; 03_eda_wine_quality.ipynb',
        '''
        fig, ax = plt.subplots(1, 2, figsize=(9, 3.1))
        for art, gruppe in penguins.groupby("species"):
            ax[0].scatter(gruppe.bill_length_mm, gruppe.bill_depth_mm,
                          s=13, alpha=.6, label=art)
        ax[0].set(xlabel="Schnabellänge [mm]", ylabel="Schnabeltiefe [mm]")
        ax[0].legend(fontsize=8)
        pts = ax[1].scatter(wein.alcohol, wein.density, c=wein.quality,
                            cmap="viridis", s=10, alpha=.5)
        ax[1].set(xlabel="Alkohol [% vol]", ylabel="Dichte [g/cm³]")
        fig.colorbar(pts, ax=ax[1], label="Qualität")
        fig.tight_layout()
        ''', [('Bild lesen', 'Die Pinguinarten bilden unterschiedlich gelegene Punktwolken. Bei Rotwein sind höhere Alkoholwerte häufig mit geringerer Dichte verbunden; die Qualitätsstufen bleiben jedoch stark überlagert.'),
              ('Viele Punkte', 'alpha und kleine Marker reduzieren Überdeckung. Bei großen Tabellen hexbin oder eine 2D-Häufigkeitsdarstellung nutzen. Achsen und Einheiten angeben; eine Farbskala für Kategorien braucht klar unterscheidbare Klassenfarben.')])

    bild(3, 'Korrelationen als Heatmap',
        'Eine Korrelationsmatrix fasst paarweise Zusammenhänge zusammen. Pearson misst lineare, Spearman monotone Beziehungen und ist bei Rängen oder stark schiefen Größen oft eine nützliche Ergänzung.',
        'Korrelation ist kein Kausalnachweis. Eine hohe Korrelation zwischen Eingaben kann auch redundante Merkmale anzeigen.',
        'Set 3: 02_eda_palmer_penguins.ipynb; 03_eda_wine_quality.ipynb',
        '''
        cols = ["alcohol", "density", "residual sugar", "quality"]
        labels_corr = ["Alkohol", "Dichte", "Zucker", "Qualität"]
        fig, ax = plt.subplots(1, 2, figsize=(9, 3.3))
        for a, method in zip(ax, ["pearson", "spearman"]):
            corr = wein[cols].corr(method=method)
            im = a.imshow(corr, vmin=-1, vmax=1, cmap="coolwarm")
            a.set_xticks(range(4), labels_corr, rotation=30, ha="right")
            a.set_yticks(range(4), labels_corr)
            a.set_title(method.title())
            for i in range(4):
                for j in range(4):
                    a.text(j, i, f"{corr.iloc[i,j]:.2f}",
                           ha="center", va="center", fontsize=9)
        fig.tight_layout()
        ''', [('Farben und Zahlen', 'Rot bedeutet positive, Blau negative Korrelation; die Skala ist in beiden Bildern identisch von -1 bis 1. Die Diagonale ist immer 1. Alkohol und Qualität hängen positiv, Alkohol und Dichte negativ zusammen.'),
              ('Grenzen', 'Pearson nahe 0 schließt einen gekrümmten Zusammenhang nicht aus. Fehlwerte können zu unterschiedlichen paarweisen Stichproben führen. Für fachliche Aussagen zusätzlich Scatterplots, Gruppenstruktur und Fallzahlen ansehen.')])

    bild(3, 'Mehrere Merkmale im Paarvergleich',
        'Eine Scatter-Matrix zeigt für mehrere Merkmale alle paarweisen Beziehungen. Auf der Diagonale stehen Verteilungen; außerhalb der Diagonale Punktwolken.',
        'Für wenige ausgewählte Merkmale ist die Matrix ein schneller Überblick. Bei vielen Spalten wird sie unlesbar; dann fachlich vorsortieren.',
        'Set 3: 02_eda_palmer_penguins.ipynb; Set 4: 01_daten_verstehen_und_visualisieren.ipynb',
        '''
        from pandas.plotting import scatter_matrix
        cols = ["bill_length_mm", "flipper_length_mm", "body_mass_g"]
        pairs = penguins.dropna(subset=cols+["species"]).copy()
        kurz = pairs[cols].rename(columns={
            "bill_length_mm":"Schnabel [mm]",
            "flipper_length_mm":"Flosse [mm]", "body_mass_g":"Masse [g]"})
        axes = scatter_matrix(kurz, c=pairs.species.astype("category").cat.codes,
            cmap="viridis", diagonal="hist", alpha=.5, s=10,
            figsize=(7, 5), grid=False)
        axes[0,0].figure.tight_layout()
        ''', [('Bild lesen', 'Flossenlänge und Masse steigen in der Gesamttabelle gemeinsam. Die Farben markieren Arten; innerhalb einer Farbe kann der Zusammenhang anders aussehen. Gespiegelte Felder enthalten dieselben Punkte mit vertauschten Achsen.'),
              ('Gezielt weiterarbeiten', 'Auffällige Paare anschließend groß als einzelnen Scatterplot untersuchen. Die Diagonale zeigt die Gesamtverteilung, keine getrennten Histogramme pro Farbe. Diese Ansicht dient der EDA und ist keine Modellbewertung.')], height=285)

    bild(4, 'Vor und nach der Skalierung',
        'Merkmale mit großen Zahlenbereichen dominieren unskalierte Distanzen. Ein direkter Vorher-nachher-Vergleich zeigt, wie Standardisierung die Skalen angleicht.',
        'Standardisieren ändert Einheiten und Abstände, nicht die grundlegende Rangfolge der Werte innerhalb einer Spalte.',
        'Set 4: 02_sklearn_transformer_basics.ipynb',
        '''
        raw = penguins[["bill_length_mm", "body_mass_g"]].dropna()
        raw_train, raw_test = train_test_split(raw, test_size=.25, random_state=42)
        scaler_vis = StandardScaler().fit(raw_train)
        z_vis = scaler_vis.transform(raw_train)
        fig, ax = plt.subplots(1, 2, figsize=(9, 3))
        ax[0].boxplot(raw_train.to_numpy(), tick_labels=["Schnabel [mm]", "Masse [g]"])
        ax[0].set(title="Rohdaten: verschiedene Einheiten", ylabel="Rohwert")
        ax[1].boxplot(z_vis, tick_labels=["Schnabel", "Masse"])
        ax[1].axhline(0, ls="--", color="grey")
        ax[1].set(title="StandardScaler: Training", ylabel="z-Wert")
        fig.tight_layout()
        ''', [('Bild lesen', 'Links wirkt der Schnabelbereich neben den Grammwerten fast wie eine Linie. Rechts liegen die Merkmale auf vergleichbaren Skalen. Die linke Darstellung ist absichtlich ein Beispiel für einen irreführenden gemeinsamen Rohwertmaßstab.'),
              ('Wichtig', 'StandardScaler erzeugt keine Normalverteilung und entfernt keine Ausreißer. Die rechte Box muss nicht exakt um den Median 0 liegen, da nach Mittelwert und Standardabweichung skaliert wird.')])

    bild(7, 'Splits visuell kontrollieren',
        'Splitdiagramme machen sichtbar, welche Beobachtungen in Training und Test landen. Besonders bei wiederholten Messungen ist damit eine zufällige Durchmischung von Maschinen schnell erkennbar.',
        'Ein Splitplot ist ein Plausibilitätscheck. Ob Zeilen tatsächlich unabhängig sind, entscheidet der Messaufbau.',
        'Set 4: 04_daten_richtig_aufteilen.ipynb; 05_kreuzvalidierung_ohne_data_leakage.ipynb',
        '''
        from sklearn.model_selection import GroupShuffleSplit
        n_vis = 100
        group_vis = np.repeat(np.arange(10), 10)
        rand_tr, rand_te = train_test_split(np.arange(n_vis), test_size=.2, random_state=42)
        gtr, gte = next(GroupShuffleSplit(n_splits=1, test_size=.2,
            random_state=42).split(np.zeros((n_vis,1)), groups=group_vis))
        fig, ax = plt.subplots(1, 3, figsize=(9, 2.8))
        splits_vis = [(rand_tr,rand_te), (gtr,gte), (np.arange(80),np.arange(80,100))]
        for a, (tr,te), name in zip(ax, splits_vis, ["Zufall", "Gruppen", "Zeit"]):
            a.scatter(tr, group_vis[tr], s=14, label="Training")
            a.scatter(te, group_vis[te], s=18, label="Test", color="#f15a24")
            a.set(title=name, xlabel="Zeilenposition", ylabel="Maschine / Gruppe")
        ax[0].legend(fontsize=8)
        fig.tight_layout()
        ''', [('Bild lesen', 'Beim Zufallssplit sind orange Testpunkte über fast alle Maschinen verteilt. Im Gruppensplit liegen ganze Maschinen im Test. Der Zeitsplit reserviert den rechten, späteren Bereich; er garantiert bei anderer Zeilensortierung keine Gruppentrennung.'),
              ('Kombinierte Anforderungen', 'Wer neue Maschinen in der Zukunft vorhersagen will, muss Gruppen und Zeit gemeinsam berücksichtigen. Für Sequenzen, Personen oder Originalaufnahmen gelten entsprechende Gruppengrenzen.')])

    bild(8, 'Tuningwerte mit Streuung zeigen',
        'Ein einzelner bester CV-Wert verdeckt die Unterschiede zwischen Folds. Fehlerbalken zeigen, ob die Parameterwahl deutlich oder nur knapp besser abschneidet.',
        'Die Standardabweichung über CV-Folds ist ein Streuungsmaß und kein unabhängiges Konfidenzintervall der zukünftigen Modellgüte.',
        'Set 6: 03_hyperparameter_tuning_regression.ipynb; Set 4: 05_kreuzvalidierung_ohne_data_leakage.ipynb',
        '''
        result_vis = pd.DataFrame(suche.cv_results_)
        c_vis = result_vis["param_clf__C"].astype(float)
        fig, ax = plt.subplots(figsize=(8, 3))
        ax.errorbar(c_vis, result_vis.mean_test_score,
            yerr=result_vis.std_test_score, marker="o", capsize=4,
            color="#f15a24", label="CV-Mittel ± Fold-Standardabweichung")
        ax.set(xscale="log", xlabel="C (inverse Regularisierung)",
               ylabel="F1 der Validierungsfolds", title="Logistische Regression: Parametersuche")
        ax.legend(fontsize=9)
        fig.tight_layout()
        ''', [('Bild lesen', 'Großes C bedeutet schwächere Regularisierung. Überlappende Fehlerbalken erinnern daran, dass winzige Unterschiede im Mittelwert keine eindeutige praktische Überlegenheit belegen.'),
              ('Nächster Schritt', 'Bei ähnlicher Leistung ein einfacheres oder stabileres Modell erwägen. Die Parameterauswahl bleibt in der CV; ein endgültiger Testwert darf nicht zur nachträglichen Feinabstimmung verwendet werden.')])

    bild(14, 'Regularisierung an Gewichten erkennen',
        'Koeffizientenplots zeigen, wie Ridge alle Gewichte schrumpft und Lasso viele Gewichte auf null setzt. Standardisierte Eingaben machen die Größen im Vergleich besser lesbar.',
        'Weniger große Koeffizienten können Overfitting reduzieren. Ein auf null gesetztes Gewicht ist keine allgemeine Aussage über die Bedeutung einer Messgröße.',
        'Set 6: 02_regularisierung_l1_l2.ipynb',
        '''
        from sklearn.datasets import make_regression
        from sklearn.linear_model import LinearRegression, Ridge, Lasso
        xv, yv = make_regression(n_samples=60, n_features=20,
            n_informative=4, noise=25, random_state=42)
        xv = StandardScaler().fit_transform(xv)
        fig, ax = plt.subplots(1, 2, figsize=(9, 3))
        for name, est in [("Linear",LinearRegression()),
                           ("Ridge α=100",Ridge(alpha=100)),
                           ("Lasso α=8",Lasso(alpha=8, max_iter=20000))]:
            est.fit(xv, yv)
            ax[0].plot(est.coef_, ".-", label=name, alpha=.8)
            ax[1].bar(name, np.count_nonzero(np.abs(est.coef_)>1e-8))
        ax[0].set(xlabel="Merkmalsindex", ylabel="Koeffizient")
        ax[0].axhline(0, color="grey", ls="--"); ax[0].legend(fontsize=8)
        ax[1].set(ylabel="Anzahl Gewichte ≠ 0", title="Gleiche Trainingsdaten")
        fig.tight_layout()
        ''', [('Bild lesen', 'Ridge verkleinert die Gewichte, lässt sie typischerweise aber ungleich null. Lasso entfernt bei dieser Stärke viele schwache Koeffizienten vollständig. Die α-Werte der Verfahren sind keine direkt gleichwertigen Skalen.'),
              ('Keine Bewertung im Trainingsplot', 'Hier werden die Effekte auf denselben Trainingsdaten demonstriert. Die Abbildung berichtet keine Testgüte. Welche Regularisierung am besten generalisiert, wird mit einer Pipeline in CV bestimmt.')])

    bild(16, 'Entscheidungsregeln als Baum',
        'Ein Baumdiagramm zeigt die nacheinander verwendeten Schwellen. An jedem Knoten wird eine Zeile nach links oder rechts weitergeleitet, bis ein Blatt eine Klasse liefert.',
        'Eine lesbare Baumgrafik ist eine Darstellung des Modells. Die fachliche Plausibilität seiner Regeln und die Leistung auf neuen Daten müssen separat geprüft werden.',
        'Set 8: 01_entscheidungsbaum_klassifikation.ipynb',
        '''
        from sklearn.tree import DecisionTreeClassifier, plot_tree
        vis_tree = DecisionTreeClassifier(max_depth=2, min_samples_leaf=10,
                                           random_state=42).fit(Xct, yct)
        fig, ax = plt.subplots(figsize=(10, 4.4))
        plot_tree(vis_tree, feature_names=["Merkmal 1", "Merkmal 2"],
            class_names=["Klasse 0", "Klasse 1"], filled=True,
            rounded=True, impurity=True, proportion=False,
            fontsize=9, ax=ax)
        fig.tight_layout()
        ''', [('Knoten lesen', 'Die erste Zeile zeigt die Splitbedingung. Die erfüllte Bedingung führt nach links. samples zählt Trainingsbeispiele, value enthält die Klassenverteilung, class die Mehrheitsklasse. Je nach sklearn-Version kann value Anteile statt absoluter Zahlen anzeigen.'),
              ('Unreinheit und Tiefe', 'Gini nahe 0 bedeutet im Training fast nur eine Klasse in diesem Knoten. Tiefe Bäume können sehr reine Blätter mit wenigen Beispielen erzeugen und trotzdem schlecht generalisieren. Die hier gewählte Tiefe 2 hält die gesamte Grafik lesbar.')], height=245)

    bild(17, 'Entscheidungsgrenzen im Vergleich',
        'Entscheidungsflächen zeigen, welche Klasse ein Modell an jeder Position des Merkmalsraums vorhersagt. Darübergelegte Trainingspunkte machen Unteranpassung und lokale Grenzformen sichtbar.',
        'Diese Grafik funktioniert hier, weil das Modell genau zwei Eingaben hat. Ein 2D-Ausschnitt aus vielen Dimensionen ist nur eine bedingte Ansicht.',
        'Sets 5, 8, 9 und 10: Klassifikationsnotebooks mit Entscheidungsgrenzen',
        '''
        from sklearn.inspection import DecisionBoundaryDisplay
        from sklearn.linear_model import LogisticRegression
        from sklearn.svm import SVC
        from sklearn.neighbors import KNeighborsClassifier
        fig, ax = plt.subplots(1, 3, figsize=(10, 3))
        estimators_vis = [LogisticRegression(), SVC(C=1, kernel="rbf"),
                          KNeighborsClassifier(7, weights="distance")]
        for a, est, name in zip(ax, estimators_vis, ["Logistisch", "RBF-SVM", "kNN"]):
            m_vis = make_pipeline(StandardScaler(), est).fit(Xct, yct)
            DecisionBoundaryDisplay.from_estimator(m_vis, Xct,
                response_method="predict", ax=a, cmap="coolwarm", alpha=.25)
            a.scatter(Xct[:,0], Xct[:,1], c=yct, cmap="coolwarm",
                       edgecolors="white", linewidths=.3, s=13)
            a.set(title=name, xlabel="Merkmal 1", ylabel="Merkmal 2")
        fig.tight_layout()
        ''', [('Bild lesen', 'Die logistische Regression erzeugt hier eine gerade Grenze. Die RBF-SVM kann den Halbmondformen folgen. kNN reagiert stärker auf lokale Nachbarschaften und kann kleine Inseln bilden.'),
              ('Güte nicht aus Schönheit ableiten', 'Glatt oder komplex ist allein kein Gütekriterium. Modellwahl und Parameter gehören in dieselben Trainings- und Validierungssplits. Die Punkte im Bild sind ausschließlich Trainingspunkte; Testmetriken stehen im Methodenrezept.')])

    bild(19, 'Trend Glättung und Autokorrelation',
        'Zeitverlauf und gleitender Mittelwert zeigen langsame und schnelle Anteile. ACF und PACF machen verzögerte Zusammenhänge sichtbar und helfen, Modellannahmen zu hinterfragen.',
        'Die Diagnose verwendet nur die Trainingsperiode. Differenzierung kann Trend entfernen, aber saisonale Abhängigkeiten erhalten.',
        'Set 12: 02_trend_saisonalitaet_und_autokorrelation.ipynb',
        '''
        from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
        fig, ax = plt.subplots(2, 2, figsize=(9, 4.3))
        ts_train.plot(ax=ax[0,0], alpha=.6, label="Messwert")
        ts_train.rolling(7).mean().plot(ax=ax[0,0], label="7-Tage-Mittel")
        ax[0,0].legend(fontsize=8); ax[0,0].set_title("Training und Glättung")
        diff_vis = ts_train.diff().dropna()
        diff_vis.plot(ax=ax[0,1], color="#f15a24", title="Erste Differenz")
        plot_acf(diff_vis, lags=40, ax=ax[1,0])
        plot_pacf(diff_vis, lags=40, ax=ax[1,1], method="ywm")
        fig.tight_layout()
        ''', [('Bild lesen', 'Der 7-Tage-Mittelwert glättet das Rauschen und folgt den langsameren Bewegungen. Die Differenzen schwanken um einen annähernd stabilen Mittelwert, zeigen aber weiterhin die periodische Dynamik.'),
              ('ACF und PACF', 'Balken außerhalb des farbigen Bandes zeigen unter den jeweiligen Annahmen auffällige Lags. Die Bänder sind punktweise Näherungen, kein Beweis eines bestimmten ARIMA-Modells; viele getestete Lags und Saisonalität beachten.')], height=245)

    bild(23, 'CNN Fehler und Filter ansehen',
        'Konfusionsmatrix, falsch klassifizierte Bilder und gelernte Filter ergänzen Lernkurven. Sie zeigen, welche Ziffern verwechselt werden und welche lokalen Muster die erste Faltung gelernt hat.',
        'Filterbilder helfen beim Verstehen der Architektur. Einzelne Filter sind keine vollständige Erklärung einer konkreten Vorhersage.',
        'Set 14: 02_cnn_filter_pooling_und_feature_maps.ipynb; cv_tools.py',
        '''
        from sklearn.metrics import ConfusionMatrixDisplay
        predicted_nn = probs_nn.argmax(1)
        wrong_nn = (predicted_nn != echte_nn).nonzero().flatten()[:4]
        fig = plt.figure(figsize=(10, 4))
        gs = fig.add_gridspec(2, 5, width_ratios=[1.5,1,1,1,1])
        ConfusionMatrixDisplay.from_predictions(echte_nn.numpy(),
            predicted_nn.numpy(), ax=fig.add_subplot(gs[:,0]),
            colorbar=False, cmap="Oranges")
        for j in range(4):
            a = fig.add_subplot(gs[0,j+1]); a.axis("off")
            if j < len(wrong_nn):
                idx = int(wrong_nn[j])
                a.imshow(bilder[split["test"]][idx,0], cmap="gray")
                a.set_title(f"Ist {int(echte_nn[idx])}, Netz {int(predicted_nn[idx])}", fontsize=9)
            b = fig.add_subplot(gs[1,j+1]); b.axis("off")
            b.imshow(cnn.features[0].weight[j,0].detach().numpy(), cmap="coolwarm")
            b.set_title(f"3×3-Filter {j}", fontsize=9)
        fig.tight_layout()
        ''', [('Konfusionsmatrix', 'Diagonale Zellen sind korrekte Vorhersagen, andere Zellen Verwechslungen. Zeilen sind echte Klassen, Spalten Vorhersagen. Die ausgewählten Fehlerbilder stammen aus genau diesem Testlauf.'),
              ('Filter und Feature Maps', 'Die untere Reihe zeigt vier gelernte 3×3-Kernel. Feature Maps erhält man mit cnn.features[:2](probe) nach Faltung und ReLU. Testfehler dienen hier der abschließenden Diagnose, nicht einer anschließenden Optimierung anhand derselben Testdaten.')], height=210)

    bild(26, 'NMF Bausteine und Rekonstruktion',
        'NMF lässt sich direkt an den gelernten Komponenten prüfen. Eine rekonstruierte Messung zeigt, ob die additive Zerlegung die Eingabestruktur erfasst.',
        'Ein kleiner Rekonstruktionsfehler beweist nicht, dass jeder gefundene Baustein einer eindeutigen physikalischen Quelle entspricht.',
        'Set 11: 02_nmf_und_tsne.ipynb',
        '''
        fig, ax = plt.subplots(1, 2, figsize=(9, 3.1))
        for i, component in enumerate(nmf.components_, 1):
            ax[0].plot(wl, component, label=f"Baustein {i}")
        ax[0].set(xlabel="Wellenlänge [nm]", ylabel="Komponentenwert")
        ax[0].legend(fontsize=8)
        reconstruction_vis = Wn @ nmf.components_
        ax[1].plot(wl, spectra[0], label="Original", lw=2)
        ax[1].plot(wl, reconstruction_vis[0], "--", label="W @ H")
        ax[1].set(xlabel="Wellenlänge [nm]", ylabel="Intensität",
                  title="Ein simuliertes Spektrum")
        ax[1].legend(fontsize=8)
        fig.tight_layout()
        ''', [('Bild lesen', 'Die Komponenten lokalisieren die drei simulierten Spektralbereiche. Die Rekonstruktion liegt nahe an der Originalkurve. Komponentenreihenfolge und Skalierung können sich ändern, obwohl das Produkt W @ H fast gleich bleibt.'),
              ('Diagnose ausbauen', 'Rekonstruktionsfehler für einzelne Messungen statt nur als Gesamtsumme ansehen. Falls neue Spektren beurteilt werden, NMF am Training fitten und neue Daten mit transform in die gelernten Komponenten zerlegen.')])

    bild(28, 'Clusterformen und weiche Zuordnung',
        'DBSCAN ist bei gebogenen dichten Gruppen hilfreich, GMM beschreibt ellipsoidartige Komponenten. Eine farbige Darstellung macht die unterschiedlichen Modellannahmen deutlicher als ein Score allein.',
        'Eine niedrigere Silhouette kann bei gebogenen Gruppen trotzdem zu einer fachlich sinnvollen Lösung gehören. Score und Geometrie gemeinsam lesen.',
        'Set 11: 04_hierarchisch_dbscan_und_gmm.ipynb',
        '''
        fig, ax = plt.subplots(1, 2, figsize=(9, 3))
        ax[0].scatter(zm[mask,0], zm[mask,1], c=lab_db[mask], cmap="tab10", s=12)
        ax[0].scatter(zm[~mask,0], zm[~mask,1], c="black", marker="x",
                       label="Noise", s=28)
        ax[0].set(title="DBSCAN: Halbmonde", xlabel="z1", ylabel="z2")
        ax[0].legend(fontsize=8)
        prob_vis = gmm.predict_proba(zb)
        sc = ax[1].scatter(zb[:,0], zb[:,1], c=prob_vis.max(axis=1),
                            vmin=0, vmax=1, cmap="viridis", s=13)
        ax[1].set(title="GMM: höchste Zugehörigkeit", xlabel="z1", ylabel="z2")
        fig.colorbar(sc, ax=ax[1], label="max P(Komponente | x)")
        fig.tight_layout()
        ''', [('Bild lesen', 'DBSCAN folgt den zwei Halbmondformen und markiert wenige Punkte als Noise. Die vier simulierten Blob-Gruppen rechts sind so deutlich getrennt, dass die höchste modellinterne GMM-Zugehörigkeit fast überall nahe 1 liegt.'),
              ('Vorsicht bei hoher Sicherheit', 'Hohe Zugehörigkeit heißt nur, dass eine Komponente relativ zu den anderen dominiert. Ein weit entfernter neuer Punkt kann trotzdem eine hohe relative Zugehörigkeit haben; für Anomalien zusätzlich die absolute Dichte prüfen.')])

    bild(29, 'Anomaliescores und Alarmgrenzen',
        'Score-Verteilungen zeigen, wie stark Normalfälle und Anomalien überlappen. Ein räumlicher Plot ergänzt, an welchen Stellen das gewählte Verfahren tatsächlich Alarm auslöst.',
        'Der Schwellenwert verschiebt den Kompromiss zwischen Fehlalarm und verpasstem Fehler. Für die reale Anwendung müssen Anomalien und Normalvarianten repräsentativ sein.',
        'Set 11: 05_anomalieerkennung_und_thresholds.ipynb',
        '''
        fig, ax = plt.subplots(1, 2, figsize=(9, 3))
        bins_vis = np.linspace(score.min(), score.max(), 22)
        ax[0].hist(score[test_y==0], bins=bins_vis, alpha=.6,
                    density=True, label="Normal")
        ax[0].hist(score[test_y==1], bins=bins_vis, alpha=.6,
                    density=True, label="Anomalie")
        ax[0].axvline(threshold, color="black", ls="--", label="Schwelle aus Validierung")
        ax[0].set(xlabel="Anomaliescore (größer = auffälliger)", ylabel="Dichte")
        ax[0].legend(fontsize=7)
        ax[1].scatter(test_x[~flag,0], test_x[~flag,1], s=13, label="Kein Alarm")
        ax[1].scatter(test_x[flag,0], test_x[flag,1], s=25, marker="x",
                      color="#f15a24", label="Alarm")
        ax[1].set(xlabel="Merkmal 1", ylabel="Merkmal 2")
        ax[1].legend(fontsize=8); fig.tight_layout()
        ''', [('Bild lesen', 'In diesem bewusst einfachen Beispiel liegen die simulierten Anomalien weit außerhalb der normalen Wolke. Einige normale Randpunkte überschreiten ebenfalls die festgelegte Schwelle; sie sind Fehlalarme.'),
              ('Nicht am Test nachjustieren', 'Die vertikale Grenze wurde zuvor aus normalen Validierungsdaten bestimmt. Ihre Lage nach Betrachtung dieser Testhistogramme zu ändern würde einen neuen unabhängigen Test erfordern.')])

    # Interleave visuals with methods; retain original IDs for result formatting.
    combined = []
    physical = {}
    for n, p in enumerate(original, 1):
        physical[n] = len(combined)+1
        p['original_id'] = n
        combined.append(p)
        combined.extend(extra.get(n, []))
    def references(s):
        return re.sub(r'Seite\s+(\d+)', lambda m: 'Seite '+str(physical.get(int(m[1]),int(m[1]))), s)
    for p in combined:
        p['code'] = references(p['code'])
        p['notes'] = [(t,references(b)) for t,b in p['notes']]
    ranges = [(2,3,'Imports, Datensätze und EDA mit sechs Bildseiten'),
              (4,6,'Vorverarbeitung und eigene Merkmale'),
              (7,9,'Splits, CV und seltene Klassen'),
              (10,11,'Metriken und Diagnoseplots'),
              (12,18,'Überwachte Modelle und CRF'),
              (19,21,'Zeitreihen und Prognosen'),
              (22,24,'MLP, CNN und Transfer Learning'),
              (25,28,'PCA, NMF, t-SNE und Cluster'),
              (29,31,'Anomalien, Speichern und Transformer-Klasse')]
    combined[0]['table'] = [('Seiten','Nachschlagen')]+[
        (f'{physical[a]}–{physical[b]+len(extra.get(b,[]))}',t) for a,b,t in ranges]
    combined[0]['intro'] += ' Die erweiterte Bildfassung zeigt EDA und Modell-Diagnostik direkt bei den jeweiligen Methoden.'
    return combined
