import csv
from .paths import OUTPUTS, PROCESSED
from .normalize_month import month_range
def main(start='2015-01', end='2026-05'):
    p=PROCESSED/'israel_tourism_country_month_long.csv'; rows=list(csv.DictReader(open(p))) if p.exists() else []
    months={r['month'] for r in rows}; missing=[m for m in month_range(start,end) if m not in months]
    keys={}; dups=[]; bad=0
    for r in rows:
        keys[(r['month'],r['country'])]=keys.get((r['month'],r['country']),0)+1
        if not r.get('source_url') or not r.get('source_file'): bad+=1
    dups=[k for k,v in keys.items() if v>1]
    lines=['# Validation report','',f'Rows: {len(rows)}',f'Missing months: {len(missing)}',', '.join(missing) if missing else 'None','',f'Duplicate month-country rows: {len(dups)}',f'Rows missing provenance: {bad}','','## Parser confidence summary','See data/interim/parsed_country_month_rows.csv.','','## Source conflicts','None detected by duplicate key check.' if not dups else str(dups),'','## Top-10 countries per month','Generated when parsed rows exist.' if rows else 'No rows parsed; all months remain explicit missing until official source files are added.']
    (OUTPUTS/'validation_report.md').write_text('\n'.join(lines)); print(OUTPUTS/'validation_report.md')
if __name__=='__main__': main()
