monthly_income = input("Enter your monthly income: ")
monthly_expenses = input("Enter your monthly expenses: ")
monthly_savings = int(monthly_income) - int(monthly_expenses)
interest_rate = 0.05
annual_savings = int(monthly_savings * 12 + (monthly_savings * 12 * interest_rate))
print("Your monthly savings are:", monthly_savings)
print("Projected savings after one year, with interest, is:", annual_savings)