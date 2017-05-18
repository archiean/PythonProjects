import datetime
sundays=0
for year in range(2001,2017):
    for month in range(1,13):
        d=datetime.date(year, month, 1)
        if d.weekday()==6:
            sundays=sundays+1
print(sundays)
