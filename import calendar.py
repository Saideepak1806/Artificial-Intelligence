import calendar

year = int(input("Enter year: "))
month = int(input("Enter month (1-12): "))

print("\nCalendar:")
print(calendar.month(year, month))
