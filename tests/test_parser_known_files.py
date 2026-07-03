import csv
from israel_tourism_etl.parse_excel import parse_workbook

def test_known_workbook(tmp_path):
    p=tmp_path/'official.csv'
    with open(p,'w',newline='') as f:
        w=csv.writer(f); w.writerow(['Tourists by country of residence','']); w.writerow(['Country','Tourist arrivals']); w.writerow(['USA','123']); w.writerow(['France','45'])
    rows=parse_workbook(p,'test-source','2026-05')
    assert rows[0]['raw_country']=='USA' and rows[0]['arrivals']==123
    assert len(rows)==2
