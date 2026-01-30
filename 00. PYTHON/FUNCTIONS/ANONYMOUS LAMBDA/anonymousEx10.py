# Lambda function to convert days into years, months, and days
convert_days = lambda days: [days // 365, (days % 365) // 30, (days % 365) % 30]
num_days = int(input("Enter number of days: "))
years, months, days = convert_days(num_days)
print("{} days is equivalent to {} years, {} months, and {} days.".format(num_days,years,months,days))