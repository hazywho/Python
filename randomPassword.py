from datetime import date
from datetime import timedelta

today = date.today()

for i in range(51):
    d = today + timedelta(days=i)
    if d.weekday() < 5:            # Here
        print(d,end=", ")