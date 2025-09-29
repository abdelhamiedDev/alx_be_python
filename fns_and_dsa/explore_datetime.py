import datetime
from datetime import timedelta

def display_current_datetime():
    current_date = datetime.datetime.now()
    return current_date

def calculate_future_date(days_ahead):
    current_date = display_current_datetime()
    future_date = current_date + timedelta(days=days_ahead)
    future_date.strftime("%Y-%m-%d")
    return future_date

def main():
    print("Current date and time:", display_current_datetime())
    days = int(input("Enter number of days to add to the current date: "))
    future_date = calculate_future_date(days)
    print(f"Future date: {future_date}")

if __name__ == "__main__":
    main()