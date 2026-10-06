"""Kleine CWRU-Auswahl laden und Merkmale aus echten Vibrationssignalen bilden."""
from pathlib import Path
from urllib.request import Request, urlopen
import hashlib
import numpy as np
import pandas as pd
from scipy.io import loadmat
from scipy.stats import kurtosis

DATEN = Path(__file__).resolve().parent / "daten" / "cwru"
FS = 48_000  # DE-Kanal: alle hier ausgewählten Aufnahmen mit 48 kHz
AUFNAHMEN = [
    ("97", "gesund"),
    ("109", "Innenring"),
    ("122", "Kugel"),
    ("135", "Außenring"),
]
BASIS_URL = "https://engineering.case.edu/sites/default/files/"


def lade_aufnahmen():
    """Einmaliger Download von CWRU; danach wird der lokale Cache verwendet."""
    DATEN.mkdir(parents=True, exist_ok=True)
    signale, zeilen = {}, []
    for datei_id, zustand in AUFNAHMEN:
        pfad = DATEN / f"{datei_id}.mat"
        url = BASIS_URL + pfad.name
        if not pfad.exists():
            print(f"Lade {pfad.name} ({zustand}) ...")
            try:
                with urlopen(Request(url, headers={"User-Agent": "ML-Kurs/1.0"}), timeout=60) as antwort:
                    inhalt = antwort.read()
                # Erst prüfen, dann speichern: eine HTML-Fehlerseite wird nicht gecacht.
                from io import BytesIO
                mat = loadmat(BytesIO(inhalt))
                if not any(k.endswith("_DE_time") for k in mat):
                    raise ValueError("Kein DE-Signal in der heruntergeladenen Datei.")
                pfad.write_bytes(inhalt)
            except Exception as exc:
                raise RuntimeError(
                    f"Download von {url} fehlgeschlagen. Originaldatei manuell nach {pfad} "
                    "speichern und Zelle erneut starten. Keine synthetischen Ersatzdaten."
                ) from exc
        mat = loadmat(pfad)
        signal_keys = [k for k in mat if k.endswith("_DE_time")]
        if len(signal_keys) != 1:
            raise ValueError(f"DE-Kanal nicht eindeutig: {pfad}")
        x = np.asarray(mat[signal_keys[0]], dtype=float).ravel()
        if len(x) < FS or not np.isfinite(x).all():
            raise ValueError(f"Ungültiges oder zu kurzes Signal: {pfad}")
        rpm_keys = [k for k in mat if k.endswith("RPM")]
        rpm = float(np.asarray(mat[rpm_keys[0]]).item()) if rpm_keys else 1797.0
        signale[zustand] = x
        zeilen.append({"aufnahme": datei_id, "zustand": zustand, "fs_hz": FS,
                       "rpm": rpm, "rpm_quelle": "Datei" if rpm_keys else "Quelltabelle (ca.)",
                       "samples": len(x), "dauer_s": len(x) / FS,
                       "url": url, "sha256": hashlib.sha256(pfad.read_bytes()).hexdigest()})
    return signale, pd.DataFrame(zeilen)


def spektrum(x, fs=FS):
    """Einseitiges Amplitudenspektrum mit Mittelwertabzug und Hann-Fenster."""
    x = np.asarray(x, dtype=float)
    fenster = np.hanning(len(x))
    fft = np.fft.rfft((x - x.mean()) * fenster)
    amplitude = np.abs(fft) / fenster.sum()
    # Nur die positiven Frequenzen verdoppeln, nicht DC oder Nyquist.
    if len(x) % 2 == 0:
        amplitude[1:-1] *= 2
    else:
        amplitude[1:] *= 2
    return np.fft.rfftfreq(len(x), d=1 / fs), amplitude


def signal_merkmale(x, fs=FS):
    """Zeitmerkmale und relative spektrale Energie pro Messfenster."""
    x = np.asarray(x, dtype=float)
    x = x - x.mean()
    rms = np.sqrt(np.mean(x ** 2))
    peak = np.max(np.abs(x))
    f, a = spektrum(x, fs)
    # Relative Energie aus |FFT|²; DC und Nyquist werden nicht verdoppelt.
    energie = np.abs(np.fft.rfft(x * np.hanning(len(x)))) ** 2
    if len(x) % 2 == 0:
        energie[1:-1] *= 2
    else:
        energie[1:] *= 2
    gesamt = energie.sum()
    if rms == 0 or gesamt == 0:
        raise ValueError("Konstantes Signal: Spektralmerkmale nicht definiert.")
    merkmale = {
        "rms": rms,
        "mittel_abs": np.mean(np.abs(x)),
        "peak": peak,
        "peak_to_peak": np.ptp(x),
        "crest_faktor": peak / rms,
        "kurtosis": kurtosis(x, fisher=False, bias=False),
        "spektralschwerpunkt_hz": np.sum(f * energie) / gesamt,
        "peak_frequenz_hz": f[1:][np.argmax(a[1:])],
    }
    for unten, oben in [(0, 1000), (1000, 3000), (3000, 6000), (6000, 24000)]:
        # Letztes Band enthält Nyquist. Die Bänder partitionieren das Spektrum.
        maske = (f >= unten) & ((f <= oben) if oben == fs / 2 else (f < oben))
        merkmale[f"band_{unten}_{oben}"] = energie[maske].sum() / gesamt
    return merkmale


def erstelle_feature_tabelle(signale, metadata, fenster_samples=8192, max_fenster=24):
    """Gleich viele nicht überlappende Fenster je Aufnahme, keine Zufallsmischung."""
    anzahl = min(max_fenster, min(len(x) // fenster_samples for x in signale.values()))
    if anzahl < 2:
        raise ValueError("Zu wenige vollständige Fenster.")
    zeilen = []
    for zustand, x in signale.items():
        aufnahme = metadata.loc[metadata.zustand == zustand, "aufnahme"].iloc[0]
        for i in range(anzahl):
            start = i * fenster_samples
            zeilen.append({"aufnahme": aufnahme, "zustand": zustand, "fenster": i,
                           "start_s": start / FS,
                           **signal_merkmale(x[start:start + fenster_samples])})
    return pd.DataFrame(zeilen)
