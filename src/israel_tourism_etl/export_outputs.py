import csv
from .paths import PROCESSED, OUTPUTS
COLS=['month','country','iso3','arrivals','source_url','source_file','source_table','retrieved_at','aggregate_country','notes']
def main():
    p=PROCESSED/'israel_tourism_country_month_long.csv'; rows=list(csv.DictReader(open(p))) if p.exists() else []
    with open(OUTPUTS/'israel_tourism_country_month_long.csv','w',newline='') as f: w=csv.DictWriter(f,fieldnames=COLS); w.writeheader(); w.writerows(rows)
    countries=sorted({r['country'] for r in rows}); months=sorted({r['month'] for r in rows})
    with open(OUTPUTS/'israel_tourism_country_month_wide.csv','w',newline='') as f:
        w=csv.writer(f); w.writerow(['month']+countries)
        for m in months: w.writerow([m]+[next((r['arrivals'] for r in rows if r['month']==m and r['country']==c),'') for c in countries])
    (OUTPUTS/'data_dictionary.md').write_text('# Data dictionary\n\n'+'\n'.join([f'- `{c}`: see ETL schema.' for c in COLS]))
if __name__=='__main__': main()
