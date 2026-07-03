import csv, hashlib
from pathlib import Path
from datetime import datetime, timezone
from .paths import INTERIM, RAW

def main():
    mp=INTERIM/'source_manifest.csv'
    if not mp.exists(): raise SystemExit('Run discover_sources first')
    rows=list(csv.DictReader(mp.open()))
    for r in rows:
        if r.get('status')=='missing' or not r.get('source_url'): continue
        folder=RAW/('cbs' if 'cbs' in r.get('publisher','').lower() or 'cbs.gov.il' in r['source_url'] else 'tourism_ministry')
        name=Path(r['source_url'].split('?')[0]).name or (r['source_id']+'.bin')
        dest=folder/name
        import requests
        content=requests.get(r['source_url'],timeout=60).content
        if dest.exists() and hashlib.sha256(dest.read_bytes()).hexdigest()!=hashlib.sha256(content).hexdigest():
            dest=folder/(dest.stem+'_'+hashlib.sha256(content).hexdigest()[:8]+dest.suffix)
        if not dest.exists(): dest.write_bytes(content)
        r['local_path']=str(dest); r['retrieved_at']=datetime.now(timezone.utc).isoformat(); r['status']='downloaded'
    with mp.open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=rows[0].keys()); w.writeheader(); w.writerows(rows)
if __name__=='__main__': main()
