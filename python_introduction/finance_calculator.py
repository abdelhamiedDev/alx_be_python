monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your monthly expenses: "))

monthly_savings = monthly_income - monthly_expenses
print(f"Your monthly savings are ${monthly_savings:.0f}.")

interest_rate = 0.05

annual_savings = int(monthly_savings * 12 + (monthly_savings * 12 * interest_rate))
print(f"Projected savings after one year, with interest, is: ${annual_savings:.0f}.")