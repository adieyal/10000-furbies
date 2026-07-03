def duplicate_count(rows):
    keys={};
    for r in rows: keys[(r['month'],r['country'])]=keys.get((r['month'],r['country']),0)+1
    return sum(v for v in keys.values() if v>1)
def missing_months(rows, expected): return [m for m in expected if m not in {r['month'] for r in rows}]
def test_duplicate_and_missing_detection():
    rows=[{'month':'2015-01','country':'USA'},{'month':'2015-01','country':'USA'}]
    assert duplicate_count(rows)==2
    assert missing_months(rows,['2015-01','2015-02'])==['2015-02']
def test_enriched_metric_calculation():
    rows=[{'month':'2019-01','country':'USA','arrivals':100},{'month':'2020-01','country':'USA','arrivals':120}]
    prior={(r['country'],r['month']):r['arrivals'] for r in rows}
    assert prior.get(('USA','2019-01'))==100
