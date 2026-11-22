"""Gemeinsame Einrichtung für die Colab-Startzellen der Kursnotebooks."""

import os
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
    cpu_changed = cpu and "requirements-cpu.txt" not in installed
    for requirements in ["requirements.txt"] + (["requirements-cpu.txt"] if cpu else []):
        if requirements not in installed:
            subprocess.check_call([
                sys.executable, "-m", "pip", "install", "-q",
                "-r", str(repo / requirements),
            ])
            installed.add(requirements)
            sys._mlkurs_colab_packages = installed
    os.chdir(folder)
    if str(folder) not in sys.path:
        sys.path.insert(0, str(folder))
    if cpu_changed and "torch" in sys.modules:
        raise RuntimeError(
            "PyTorch wurde bereits geladen. Bitte die Colab-Sitzung neu starten "
            "und anschließend die Setup-Zelle erneut ausführen."
        )
    print(f"Kurs eingerichtet. Arbeitsordner: {folder}")
