from israel_tourism_etl.normalize_month import normalize_month, month_range

def test_months():
    assert normalize_month('January 2015') == '2015-01'
    assert normalize_month('2015-2') == '2015-02'
    assert normalize_month('מרץ 2016') == '2016-03'
    assert month_range('2015-11','2016-02') == ['2015-11','2015-12','2016-01','2016-02']
