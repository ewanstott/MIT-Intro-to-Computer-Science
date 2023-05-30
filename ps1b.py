# Set initial state variables
portion_down_payment = 0.25   # Percent of home value for down payment
r = 0.04   # Rate of investment return

# Input salary, portion saved, and total cost of home
annual_salary = float(input("Input your starting annual salary: "))
portion_saved = float(input("Input portion of salary to be saved, as a decimal: ")) #should be decimal form
total_house_cost = float(input("Input cost of your dream home: ")) 
semi_annual_raise = float(input("Input your semi annual raise, as a decial: "))


# Monthly salary and down payment
monthly_salary = annual_salary/12
monthly_return = r/12
down_payment = portion_down_payment*total_house_cost

# Months and current savings
months = 0
current_savings = 0

while current_savings <= down_payment:
    current_savings += portion_saved*monthly_salary + current_savings*monthly_return
    months += 1 
    if months % 6 == 0: #is a condition that evaluates to True i.e. if months divides by 6, execute this condition
        monthly_salary += monthly_salary*semi_annual_raise


# % = returns the remainder of dividing the left hand operand by right hand operand
# while current_savings <= down_payment:
#     current_savings += portion_saved*(monthly_salary*monthly_raise) + current_savings*monthly_return #<<ADD SEMI ANNUAL RAISE INTO CALCULATION
#     months += 1 

print("Number of months: ", months)





#for current_savings in range(0,current_savings <= down_payment, 6 months):
#raise salary on 6th, 12th, 18th month etc << use a 'months*6' step of some sort? 


