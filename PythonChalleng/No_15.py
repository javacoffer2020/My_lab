from calendar import isleap
from datetime import date

TUESDAY = 1

for year in range(1700, 2020):
    t = date(year, 1, 27)
    if isleap(year) and t.weekday() == TUESDAY:
        print(t.isoformat())

