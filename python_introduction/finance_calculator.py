monthly_income = int(input("Enter your monthly income: "))
monthly_expenses = int(input("Enter your monthly expenses: "))

monthly_savings = monthly_income - monthly_expenses

print("Your monthly savings are: $", monthly_savings)

interest_rate = 0.05

projected_annual_savings = int(monthly_savings * 12 + (monthly_savings * 12 * 0.05))

print( "Projected savings after one year, with interest, is: $", projected_annual_savings)