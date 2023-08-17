def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False

def days_in_month(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month > 12 or month < 1:
        return "invalid input"
    elif is_leap(year) and month == 2:
        return 29
    else:
        return month_days[month - 1]
  
  
month_names = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
  

year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
name = month_names[month - 1]
# print(days)
print(f"{name} of {year} has {days} days.")