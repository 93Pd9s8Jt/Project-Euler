start=6
months = {"January": 31,
    "February": 28,
    "March": 31,
    "April": 30,
    "May": 31,
    "June": 30,
    "July": 31,
    "August": 31,
    "September": 30,
    "October": 31,
    "November": 30,
    "December": 31}
total = 0
for year in range(1901, 2000+1):
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        leap = 1
    else:
        leap = 0
    for month in months.keys():
        days = months[month]
        day = start
        if month == "February":
            days += leap
        # day holds Sundays
        if day == 1:
            total += 1
        if (days % 7) == 0:
            pass # start doesn't change
        else:
            start = (start - (days % 7)) % 7
        if start == 0:
            start = 7

print(total)        

