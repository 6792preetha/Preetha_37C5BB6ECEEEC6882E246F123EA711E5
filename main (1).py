import calendar

yr = int(input("Enter a Year = "))

if calendar.isleap(yr):
    print(yr, "is a Leap Year.")
else:
    print(yr, "is not.")