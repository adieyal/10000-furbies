from israel_tourism_etl.normalize_country import normalize_country

def test_variants():
    assert normalize_country('USA')[:2] == ('United States','USA')
    assert normalize_country('United States of America')[:2] == ('United States','USA')
    assert normalize_country('UK')[:2] == ('United Kingdom','GBR')
    assert normalize_country('Britain')[:2] == ('United Kingdom','GBR')
    assert normalize_country('Russian Federation')[:2] == ('Russia','RUS')
    assert normalize_country('Korea, Republic of')[:2] == ('South Korea','KOR')
