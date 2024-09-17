import calendar

month, day, year = list(map(int,input().split()))

weekday = calendar.weekday(year, month, day)

days = ['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY']
day_name = days[weekday]

print(day_name)


#OUTPUT:
#Input
#08 05 2015
#Expected Output
WEDNESDAY
