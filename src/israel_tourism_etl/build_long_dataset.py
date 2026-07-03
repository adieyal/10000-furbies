import csv
from pathlib import Path
from .paths import INTERIM, PROCESSED
from .parse_excel import parse_workbook
from .normalize_country import normalize_country
COLS=['month','country','iso3','arrivals','source_url','source_file','source_table','retrieved_at','aggregate_country','notes']
def write_csv(path, rows, cols):
    with open(path,'w',newline='') as f: w=csv.DictWriter(f,fieldnames=cols); w.writeheader(); w.writerows(rows)
def main():
    manifest=list(csv.DictReader((INTERIM/'source_manifest.csv').open())) if (INTERIM/'source_manifest.csv').exists() else []
    parsed=[]
    for s in manifest:
        p=s.get('local_path')
        if p and Path(p).suffix.lower() in ('.xlsx','.xls','.csv') and Path(p).exists(): parsed += parse_workbook(p,s['source_id'],s.get('month'))
    write_csv(INTERIM/'parsed_country_month_rows.csv', parsed, ['month','raw_country','arrivals','source_id','source_file','source_table','parser_name','parse_confidence','notes'])
    byid={r['source_id']:r for r in manifest}; out=[]; cmap=[]; seen=set()
    for r in parsed:
        name,iso,agg,decision=normalize_country(r['raw_country']); s=byid.get(r['source_id'],{})
        key=(r['raw_country'],name,iso,r['source_id'],decision)
        if key not in seen:
            cmap.append({'raw_country':r['raw_country'],'normalized_country':name,'iso3':iso,'first_seen_source_id':r['source_id'],'decision':decision,'notes':''}); seen.add(key)
        out.append({'month':r['month'],'country':name,'iso3':iso,'arrivals':int(r['arrivals']),'source_url':s.get('source_url',''),'source_file':r['source_file'],'source_table':r['source_table'],'retrieved_at':s.get('retrieved_at',''),'aggregate_country':str(agg).lower(),'notes':r['notes']})
    write_csv(INTERIM/'country_normalization_map.csv', cmap, ['raw_country','normalized_country','iso3','first_seen_source_id','decision','notes'])
    write_csv(PROCESSED/'israel_tourism_country_month_long.csv', out, COLS)
if __name__=='__main__': main()
