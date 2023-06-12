# Part B: Saving, with a raise

# Build on your solution to Part A by factoring in a raise every six months.

# In ​ps1b.py​, copy your solution to Part A (as we are going to reuse much of that machinery). Modify your program to include the following

# 1. Have the user input a semi-annual salary raise ​semi_annual_raise​ (as a decimal percentage)
# 2. After the 6t​h​ month, increase your salary by that percentage. Do the same after the 12t​h
# month, the 18​th​ month, and so on.

# Write a program to calculate how many months it will take you save up enough money for a down payment. LIke before, assume that your investments earn a return of ​r​ = 0.04 (or 4%) and the required down payment percentage is 0.25 (or 25%). Have the user enter the following variables:
# 1. The starting annual salary (annual_salary)
# 2. The percentage of salary to be saved (portion_saved)
# 3. The cost of your dream home (total_cost)
# 4. The semi­annual salary raise (semi_annual_raise)

# User inputs
annual_salary = float(input("Enter annual salary: "))
portion_saved = float(input("Enter percent of salary to be saved, as a decimal: "))
total_cost = float(input("Enter total cost of your dream home: "))
semi_annual_raise = float(input("Enter semi-annual raise, as a decimal: "))

# Initialize state variables (convert annual values into monthly values)
portion_down_payment = 0.25
current_savings = 0
r = 0.04
monthly_salary = annual_salary/12
months = 0

# Every month -> while loop:
# Calculation in while loop
while current_savings <= total_cost*portion_down_payment:
    current_savings += monthly_salary*portion_saved + current_savings*r/12 #  Remeber to add '+=' sum of calculation to current savings
    months += 1 # Everytime loop is iterated, add 1 month to months 
    if months % 6 == 0: # E.g. if months is 6, 6 % 6 = 0 so TRUE. if months is 7, 7 % 6 = 1 so FALSE
        monthly_salary += monthly_salary*semi_annual_raise

print("Months to save up enough money for a down payment: ", months) 