import datetime
from datetime import timedelta

current_date = datetime.datetime.now()
print(f"Current date and time: {current_date}")

days_to_add = int(input("Enter the number of days to add to the current date: "))
new_date = current_date + timedelta(days=days_to_add)
print(f"Future date: {new_date}")