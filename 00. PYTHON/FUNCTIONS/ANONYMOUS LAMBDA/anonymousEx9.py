#write a program for which will accept number of days and it will convert into number of years and number pf months and left out days by using anonymous function
#anonymousEx9.py
def days_cal(days):
    year = days//365
    month=(days%365)//30
    rdays=(days%365)%30
    return year,month,rdays
#mainprogram
days = int(input("Enter the days for finding years and month and left days:"))
res=days_cal(days)
years,months,days = days_cal(days)
print("{} Years,{} Months and {} Days".format(years,months,days))

