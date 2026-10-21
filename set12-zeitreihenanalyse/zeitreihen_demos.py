"""Einfache, reproduzierbare Lehrdaten und ARIMA-Vergleiche für Set 12."""
import numpy as np
import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_absolute_error, root_mean_squared_error

MODELL_SPECS = {
    "AR(1)": ((1, 0, 0), False),
    "AR(2)": ((2, 0, 0), False),
    "MA(2)": ((0, 0, 2), False),
    "ARMA(2,1)": ((2, 0, 1), False),
    "ARIMA + Tagesmuster": ((1, 1, 0), True),
}


def demo_reihen(n=360, seed=42):
    """15 Tage stündlich: gleiche Einheit, festes Muster, sehr wenig Rauschen."""
    rng = np.random.default_rng(seed)
    t = np.arange(n)
    index = pd.date_range("2024-01-01", periods=n, freq="h", name="Zeit")
    sinus = 8 * np.sin(2 * np.pi * t / 24)
    return {
        "Sinus": pd.Series(50 + sinus + rng.normal(0, 0.03, n), index=index, name="Wert"),
        "Sinus + Trend": pd.Series(50 + 0.08 * t + sinus + rng.normal(0, 0.03, n), index=index, name="Wert"),
        "Nur Rauschen": pd.Series(50 + rng.normal(0, 0.03, n), index=index, name="Wert"),
    }


def tagesmerkmale(index):
    """Nur Uhrzeit; keine zukünftigen Messwerte und keine bekannte Amplitude."""
    phase = 2 * np.pi * index.hour / 24
    return pd.DataFrame({"Tages_sin": np.sin(phase), "Tages_cos": np.cos(phase)}, index=index)


def arima_fit(training, order, tagesmuster=False, trend=None):
    """Alle Modellfamilien werden ausschließlich mit ARIMA geschätzt."""
    model = ARIMA(training, order=order, trend=trend if trend is not None else ("t" if order[1] else "c"),
                  exog=tagesmerkmale(training.index) if tagesmuster else None,
                  enforce_stationarity=tagesmuster)
    kwargs = {}
    if order[0] == 0 and order[1] == 0 and order[2]:
        # Gültige Startwerte für MA statt ungeeigneter sinusbasierter Startschätzung.
        kwargs["start_params"] = np.r_[training.mean(), np.zeros(order[2]), training.var()]
    fit = model.fit(method_kwargs={"maxiter": 1000, "method": "powell" if tagesmuster else "lbfgs"}, **kwargs)
    if not fit.mle_retvals["converged"]:
        fit = model.fit(start_params=fit.params, method_kwargs={"method": "powell", "maxiter": 2000})
    if not fit.mle_retvals["converged"]:
        raise RuntimeError(f"ARIMA{order} hat nicht konvergiert.")
    return fit


def feste_prognose(fit, index, tagesmuster=False):
    result = fit.get_forecast(steps=len(index), exog=tagesmerkmale(index) if tagesmuster else None)
    if not result.predicted_mean.index.equals(index):
        raise ValueError("Prognoseindex passt nicht zum Auswertungsblock.")
    return result


def rollende_prognose(fit, test, tagesmuster=False):
    state = fit
    predictions = []
    for timestamp, value in test.items():
        index = pd.date_range(timestamp, periods=1, freq="h", name=test.index.name)
        features = tagesmerkmale(index) if tagesmuster else None
        predictions.append(float(state.forecast(1, exog=features).iloc[0]))
        observation = pd.Series([value], index=index, name=test.name)
        # Neue Messung erst NACH der Prognose hinzufügen. Kein neuer Fit.
        state = state.append(observation, exog=features, refit=False)
    return pd.Series(predictions, index=test.index)


def baselines(historie, test, rollend=False, volle_reihe=None):
    if rollend:
        if volle_reihe is None:
            raise ValueError("Rollende Baselines benötigen die beobachtete Historie.")
        return {"Letzter Wert": volle_reihe.shift(1).loc[test.index],
                "Vortag (24 h)": volle_reihe.shift(24).loc[test.index]}
    return {"Letzter Wert": pd.Series(historie.iloc[-1], index=test.index),
            "Vortag (24 h)": pd.Series(np.resize(historie.iloc[-24:].to_numpy(), len(test)), index=test.index)}


def auswertung(test, predictions, daten, protokoll):
    """Baselines und Modelle auf exakt denselben Zielzeiten vergleichen."""
    scores = {}
    for name, prediction in predictions.items():
        if isinstance(prediction, pd.Series) and not prediction.index.equals(test.index):
            raise ValueError(f"Indexfehler: {name}")
        if not np.isfinite(np.asarray(prediction)).all():
            raise ValueError(f"Ungültige Prognose: {name}")
        scores[name] = (mean_absolute_error(test, prediction), root_mean_squared_error(test, prediction))
    last, season = scores["Letzter Wert"][0], scores["Vortag (24 h)"][0]
    rows = []
    for name, (mae, rmse) in scores.items():
        best_baseline = min(last, season)
        rows.append({"Daten": daten, "Protokoll": protokoll, "Modell": name,
                     "MAE": mae, "RMSE": rmse,
                     "vs. letzter Wert [%]": 100 * (1 - mae / last),
                     "vs. Vortag [%]": 100 * (1 - mae / season),
                     "Besser als beide": "ja" if mae < best_baseline else "nein"})
    return pd.DataFrame(rows)


def zeitraum_plan(reihen):
    rows = []
    for name, y in reihen.items():
        for phase, block in [("Training", y.iloc[:240]), ("Validierung", y.iloc[240:288]), ("Test", y.iloc[288:])]:
            rows.append({"Daten": name, "Abschnitt": phase, "Von": block.index[0],
                         "Bis": block.index[-1], "Stunden": len(block)})
    return pd.DataFrame(rows)


def lesbare_tabelle(frame):
    """Jupyter-Tabelle: sichtbare Fehlerdifferenzen und farbiger Befund."""
    formats = {}
    for col in frame.columns:
        if "MAE" in str(col) or "RMSE" in str(col):
            formats[col] = "{:.4f}"
        if "[%]" in str(col):
            formats[col] = "{:+.1f}%"
    style = frame.style.format(formats).hide(axis="index")
    style = style.set_table_styles([
        {"selector":"th", "props":[("background-color","#e2e8f0"),("color","#0f172a"),("padding","7px 9px"),("text-align","left")]},
        {"selector":"td", "props":[("padding","6px 9px"),("border-bottom","1px solid #e2e8f0")]},
    ])
    for col in ["Befund", "Besser als beide"]:
        if col in frame.columns:
            style = style.map(lambda value: "background-color: #dcfce7; color: #166534" if value in ["ja","Modell besser"] else "background-color: #fee2e2; color: #991b1b", subset=[col])
    return style
