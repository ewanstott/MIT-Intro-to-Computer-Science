#"How long (in months) would you have to save in order to afford a down payment given the cost of the home, a salary, and the portion to be saved each month?" 

# 1. The starting annual salary (annual_salary) 120000
# 2. The portion of salary to be saved (portion_saved) 0.10
# 3. The cost of your dream home (total_cost) 1000000

# Set initial state variables
portion_down_payment = 0.25   # Percent of home value for down payment
r = 0.04   # Rate of investment return

# Input salary, portion saved, and total cost of home
annual_salary = float(input("Input your starting annual salary: "))
portion_saved = float(input("Input portion of salary to be saved, as a decimal: ")) #should be decimal form
total_house_cost = float(input("Input cost of your dream home: ")) 

# Monthly salary and down payment
monthly_salary = annual_salary/12
monthly_return = r/12
down_payment = portion_down_payment*total_house_cost

# Months and current savings (variables here used to count and track values)
months = 0
current_savings = 0

while current_savings <= down_payment: #keep running loop until savings match required down_payment
    # Increase current savings using savings and return on investment
    current_savings += portion_saved*monthly_salary + current_savings*monthly_return
    months += 1 #Inside the loop, calculate the increase to current_savings for the month and increment the count += 1  
# plus-equals operator += provides a convenient way to add a value to an existing variable and assign the new value back to the same variable

print("Number of months: ", months)

#print('%s months required to save %s down payment for a %s dollary home with a salary of %s setting aside %s'
     #% (months, down_payment, total_house_cost, annual_salary, portion_saved))