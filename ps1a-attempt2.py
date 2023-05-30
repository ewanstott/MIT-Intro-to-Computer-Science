#Inputs
annual_salary = float(input("Enter annual salary: "))
portion_saved = float(input("Enter portion of salary to save, in decimal: "))
cost_home = float(input("Enter cost of dream home: "))

#State Variables
portion_down_payment = 0.25
r = 0.04
down_payment = portion_down_payment*cost_home

#Savings Monthly salary
current_savings = 0
months = 0
monthly_salary = annual_salary/12
monthly_return = r/12

#Calculations
while current_savings <= down_payment:
    current_savings += monthly_salary*portion_saved + current_savings*monthly_return
    months += 1

print("Number of months: ", months)