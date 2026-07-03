import re
from datetime import datetime
MONTHS={m.lower():i for i,m in enumerate(['January','February','March','April','May','June','July','August','September','October','November','December'],1)}
MONTHS.update({m[:3].lower():i for m,i in list(MONTHS.items())})
MONTHS.update({'ינואר':1,'פברואר':2,'מרץ':3,'אפריל':4,'מאי':5,'יוני':6,'יולי':7,'אוגוסט':8,'ספטמבר':9,'אוקטובר':10,'נובמבר':11,'דצמבר':12})
def normalize_month(value):
    if hasattr(value,'strftime'): return value.strftime('%Y-%m')
    s=str(value).strip()
    m=re.match(r'^(\d{4})[-/](\d{1,2})$',s)
    if m: return f"{int(m.group(1)):04d}-{int(m.group(2)):02d}"
    m=re.search(r'([A-Za-z]+|[א-ת]+)\s+(\d{4})',s)
    if m and m.group(1).lower() in MONTHS: return f"{int(m.group(2)):04d}-{MONTHS[m.group(1).lower()]:02d}"
    m=re.search(r'(\d{4})\s+([A-Za-z]+|[א-ת]+)',s)
    if m and m.group(2).lower() in MONTHS: return f"{int(m.group(1)):04d}-{MONTHS[m.group(2).lower()]:02d}"
    raise ValueError(f'Cannot normalize month: {value!r}')
def month_range(start,end):
    sy,sm=map(int,start.split('-')); ey,em=map(int,end.split('-')); out=[]
    while (sy,sm)<=(ey,em):
        out.append(f'{sy:04d}-{sm:02d}'); sm+=1
        if sm==13: sy+=1; sm=1
    return out
