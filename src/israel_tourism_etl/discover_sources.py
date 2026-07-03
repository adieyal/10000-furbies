import argparse, csv
from datetime import datetime, timezone
from .paths import INTERIM
from .normalize_month import month_range

def main(argv=None):
    ap=argparse.ArgumentParser(); ap.add_argument('--start',default='2015-01'); ap.add_argument('--end',default='2026-05')
    a=ap.parse_args(argv); now=datetime.now(timezone.utc).isoformat()
    rows=[]
    for m in month_range(a.start,a.end):
        rows.append({'source_id':f'missing-{m}','year':m[:4],'month':m,'source_url':'','source_type':'official_monthly_release','file_type':'','local_path':'','title':'No official country-month source discovered automatically','publisher':'','retrieved_at':now,'status':'missing','notes':'Explicit missing month; add official CBS/Ministry source URL to manifest or improve discovery.'})
    out=INTERIM/'source_manifest.csv'; out.parent.mkdir(parents=True,exist_ok=True)
    with out.open('w',newline='') as f: csv.DictWriter(f,fieldnames=rows[0].keys()).writeheader(); csv.DictWriter(f,fieldnames=rows[0].keys()).writerows(rows)
    print(out)
if __name__=='__main__': main()
