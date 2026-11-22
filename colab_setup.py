"""Gemeinsame Einrichtung für die Colab-Startzellen der Kursnotebooks."""

import os
import importlib.util
from importlib.metadata import version
from pathlib import Path
import subprocess
import sys

REPO = Path(__file__).resolve().parent

def setup(notebook, cpu=False):
    repo = REPO
    folder = (repo / notebook).resolve().parent
    folder.relative_to(repo)
    # Prozesslokal: Nach einem Laufzeitneustart werden die Pakete erneut geprüft.
    installed = getattr(sys, "_mlkurs_colab_packages", set())
    for requirements in ["requirements.txt"]:
        if requirements not in installed:
            subprocess.check_call([
                sys.executable, "-m", "pip", "install", "-q",
                "-r", str(repo / requirements),
            ])
            installed.add(requirements)
            sys._mlkurs_colab_packages = installed
    # `cpu` kennzeichnet die bisherigen PyTorch-Notebooks. Vorhandene Builds
    # (auch CUDA) behalten; CPU-Wheels sind nur der Fallback ohne PyTorch.
    torch_changed = False
    if cpu:
        has_torch = importlib.util.find_spec("torch") is not None
        has_vision = importlib.util.find_spec("torchvision") is not None
        if not has_torch:
            subprocess.check_call([
                sys.executable, "-m", "pip", "install", "-q",
                "-r", str(repo / "requirements-cpu.txt"),
            ])
            torch_changed = True
        elif not has_vision:
            # Die vorhandene Torch-Version festhalten, damit der Resolver sie
            # beim Ergänzen von torchvision nicht austauscht.
            subprocess.check_call([
                sys.executable, "-m", "pip", "install", "-q",
                f"torch=={version('torch')}", "torchvision",
            ])
        else:
            print("Vorhandenes PyTorch und torchvision werden weiterverwendet (auch GPU-Builds).")
    os.chdir(folder)
    if str(folder) not in sys.path:
        sys.path.insert(0, str(folder))
    if torch_changed and "torch" in sys.modules:
        raise RuntimeError(
            "PyTorch wurde bereits geladen. Bitte die Colab-Sitzung neu starten "
            "und anschließend die Setup-Zelle erneut ausführen."
        )
    print(f"Kurs eingerichtet. Arbeitsordner: {folder}")
