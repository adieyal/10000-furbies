VARIANTS={'usa':'United States','u.s.a':'United States','u.s.a.':'United States','united states':'United States','united states of america':'United States','us':'United States','uk':'United Kingdom','britain':'United Kingdom','great britain':'United Kingdom','united kingdom':'United Kingdom','russia':'Russia','russian federation':'Russia','south korea':'South Korea','korea, republic of':'South Korea','republic of korea':'South Korea'}
ISO={'United States':'USA','United Kingdom':'GBR','Russia':'RUS','South Korea':'KOR','France':'FRA','Germany':'DEU','Canada':'CAN','Other':'XXX'}
def normalize_country(raw):
    s=' '.join(str(raw).strip().replace('\xa0',' ').split()); key=s.lower().strip('.')
    name=VARIANTS.get(key, s.title() if s.isupper() else s)
    if name.lower() in ('other','others','not stated','total'):
        return ('Other','XXX', True, 'aggregate_or_residual')
    return (name, ISO.get(name,''), False, 'variant_map' if key in VARIANTS else 'literal')
