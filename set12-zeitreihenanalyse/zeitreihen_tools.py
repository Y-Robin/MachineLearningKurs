"""Kleine gemeinsame Werkzeuge für die Zeitreihen-Notebooks in Set 12."""
from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.dates import AutoDateLocator, ConciseDateFormatter
from sklearn.metrics import mean_absolute_error, root_mean_squared_error

ROOT = Path(__file__).resolve().parent
FARBEN = {"roh": "#475569", "trend": "#ea580c", "saison": "#0d9488",
          "train": "#dbeafe", "val": "#fef3c7", "test": "#fee2e2", "prognose": "#7c3aed"}


def plot_stil():
    plt.rcParams.update({"figure.figsize": (11, 4), "figure.dpi": 105,
                         "axes.spines.top": False, "axes.spines.right": False,
                         "axes.grid": True, "grid.alpha": 0.22,
                         "axes.titlesize": 12, "axes.labelsize": 10,
                         "legend.frameon": False})


def zeitachse(ax):
    locator = AutoDateLocator(minticks=4, maxticks=8)
    ax.xaxis.set_major_locator(locator)
    ax.xaxis.set_major_formatter(ConciseDateFormatter(locator))


def synthetische_reihe(n=720, freq="h", seed=42):
    """Bekannter additiver Trend, Tages-/Wochenmuster, AR-Rauschen und Niveauwechsel."""
    rng = np.random.default_rng(seed)
    t = np.arange(n)
    innovation = rng.normal(0, 1.4, n)
    rauschen = np.zeros(n)
    for i in range(1, n):
        rauschen[i] = 0.55 * rauschen[i - 1] + innovation[i]
    trend = 30 + 0.018 * t + 5 * (t >= int(n * 0.72))
    saison = 5 * np.sin(2 * np.pi * t / 24) + 2 * np.sin(2 * np.pi * t / 168)
    return pd.DataFrame({"wert": trend + saison + rauschen, "trend": trend,
                         "saison": saison, "rauschen": rauschen},
                        index=pd.date_range("2024-01-01", periods=n, freq=freq, name="zeit"))


def lag_tabelle(y, lags=(1, 2, 24, 168), fenster=(24, 168)):
    """Ziel y[t] vorhersagen, wenn ausschließlich y bis t-1 bekannt ist.

    Kalendermerkmale für t sind vorher bekannt. Rollstatistiken sind kausal verschoben.
    NaNs am Anfang werden erst nach Erzeugung aller Merkmale entfernt.
    """
    X = pd.DataFrame(index=y.index)
    for lag in lags:
        X[f"lag_{lag}"] = y.shift(lag)
    vergangenheit = y.shift(1)
    for w in fenster:
        X[f"mittel_{w}"] = vergangenheit.rolling(w, min_periods=w).mean()
        X[f"std_{w}"] = vergangenheit.rolling(w, min_periods=w).std()
    X["stunde_sin"] = np.sin(2 * np.pi * X.index.hour / 24)
    X["stunde_cos"] = np.cos(2 * np.pi * X.index.hour / 24)
    X["wochentag_sin"] = np.sin(2 * np.pi * X.index.dayofweek / 7)
    X["wochentag_cos"] = np.cos(2 * np.pi * X.index.dayofweek / 7)
    X["tag_im_jahr_sin"] = np.sin(2 * np.pi * X.index.dayofyear / 365.25)
    X["tag_im_jahr_cos"] = np.cos(2 * np.pi * X.index.dayofyear / 365.25)
    tabelle = X.assign(ziel=y).dropna()
    return tabelle.drop(columns="ziel"), tabelle.ziel


def metriken(y, prognosen):
    return pd.DataFrame([{"Modell":name, "MAE":mean_absolute_error(y, p),
                          "RMSE":root_mean_squared_error(y, p)}
                         for name, p in prognosen.items()]).set_index("Modell")


def lade_bike():
    df = pd.read_csv(ROOT / "daten/bike_day.csv", parse_dates=["dteday"])
    df = df.set_index("dteday").sort_index()
    if df.index.has_duplicates:
        raise ValueError("Doppelte Tageszeitpunkte.")
    df = df.asfreq("D")
    if df.cnt.isna().any():
        raise ValueError("Fehlende Tageswerte: nicht still mit 0 auffüllen.")
    return df


def lade_energie():
    df = pd.read_csv(ROOT / "daten/energie_sensoren.csv", parse_dates=["date"])
    df = df.set_index("date").sort_index()
    if df.index.has_duplicates:
        raise ValueError("Doppelte Sensorzeitpunkte.")
    df = df.asfreq("10min")
    if df.isna().any().any():
        raise ValueError("Lücke im 10-Minuten-Raster: Ursache vor Prognose klären.")
    return df
