"""Die zwei CC-BY-4.0-Datensätze aus ihren UCI-Originalarchiven beziehen."""
from pathlib import Path
from urllib.request import Request, urlopen
from zipfile import ZipFile
from io import BytesIO, StringIO
import csv
import hashlib
import json

ROOT = Path(__file__).resolve().parent
QUELLEN = {
    "bike": "https://archive.ics.uci.edu/static/public/275/bike+sharing+dataset.zip",
    "energie": "https://archive.ics.uci.edu/static/public/374/appliances+energy+prediction.zip",
}
# Die geprüften Archiv-Hashes werden nach dem erstmaligen Bezug eingetragen.
ERWARTETE_HASHES = {'bike': 'b70182d0d0508e9abbb79306ce5c0cec34869000f8220175ac83d11dbe845401', 'energie': '2fccf354445d886e7917620b0195db1f3e3e34d5a067a93b844694a4c561255a'}

def main():
    manifest = {}
    for name, url in QUELLEN.items():
        print("Lade", name, flush=True)
        with urlopen(Request(url, headers={"User-Agent": "ML-Kurs/1.0"}), timeout=90) as response:
            data = response.read()
        sha = hashlib.sha256(data).hexdigest()
        if name in ERWARTETE_HASHES and sha != ERWARTETE_HASHES[name]:
            raise ValueError(f"Quellarchiv {name} hat sich geändert; Quelle und Lizenz erneut prüfen.")
        with ZipFile(BytesIO(data)) as z:
            if name == "bike":
                member = next(m for m in z.namelist() if m.endswith('day.csv'))
                path = ROOT / 'bike_day.csv'
                path.write_bytes(z.read(member))
                changes = "Original day.csv unverändert, lokal in bike_day.csv umbenannt."
            else:
                member = next(m for m in z.namelist() if m.endswith('energydata_complete.csv'))
                raw = z.read(member).decode('utf-8-sig')
                rows = csv.DictReader(StringIO(raw))
                path = ROOT / 'energie_sensoren.csv'
                with path.open('w', encoding='utf-8', newline='') as f:
                    writer = csv.DictWriter(f, fieldnames=['date','Appliances','T1','RH_1'])
                    writer.writeheader()
                    for row in rows:
                        writer.writerow({k:row[k] for k in writer.fieldnames})
                changes = "Nur date, Appliances, T1 und RH_1 übernommen; alle Zeilen unverändert."
        manifest[name] = {"quelle":url,"lizenz":"CC BY 4.0","archiv_sha256":sha,
                          "datei":path.name,"datei_sha256":hashlib.sha256(path.read_bytes()).hexdigest(),
                          "aenderung":changes}
        print(path.name, path.stat().st_size, sha, flush=True)
    (ROOT / 'quellen_manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

if __name__ == '__main__':
    main()
