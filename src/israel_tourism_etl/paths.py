from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT/'data'
INTERIM = DATA/'interim'
PROCESSED = DATA/'processed'
RAW = DATA/'raw'
OUTPUTS = ROOT/'outputs'
for p in [INTERIM, PROCESSED, RAW/'cbs', RAW/'tourism_ministry', OUTPUTS]: p.mkdir(parents=True, exist_ok=True)
