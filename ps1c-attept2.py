# Problem set 1 - section c

# In Part B, you had a chance to explore how both the percentage of your salary that you save each month 
# and your annual raise affect how long it takes you to save for a down payment. 
# This is nice, but suppose you want to set a particular goal, e.g. to be able to afford the down payment in three years. 
# How much should you save each month to achieve this? In this problem, you are going to write a program to answer that question. 
# To simplify things, assume:

# 1. Your semi­annual raise is .07 (7%)
# 2. Your investments have an annual return of 0.04 (4%)
# 3. The down payment is 0.25 (25%) of the cost of the house
# 4. The cost of the house that you are saving for is $1M.

# We simply want your savings to be within $100 of the required down payment.
# You are now going to try to find the best rate of savings to achieve a down payment on a $1M house in 36 months. Since hitting this exactly is a challenge, we simply want your savings to be within $100 of the required down payment.
# In​ ps1c.py​, write a program to calculate the best savings rate, as a function of your starting salary. You should use ​bisection search​ to help you do this efficiently. You should keep track of the number of steps it takes your bisections search to finish. You should be able to reuse some of the code you wrote for part B in this problem.


#Go through this solution fresh again to check if I recall 

annual_salary = float(input("Enter your annual salary: "))
total_cost = 1000000
semi_annual_raise = 0.07

portion_down_payment = 0.25
r = 0.04

# declare function
def calculate_current_savings(portion_saved): # Portion saved is a value between 0-1
    monthly_salary = annual_salary/12
    current_savings = 0
    for months in range(36): #for months 0-35
        current_savings += monthly_salary*portion_saved
        current_savings += current_savings*r/12
        if months % 6 == 0 and months > 0:
            monthly_salary += monthly_salary*semi_annual_raise
    return current_savings

if calculate_current_savings(1) >= total_cost*portion_down_payment: #portion_saved = 1 means saving 100% of salary. So if we save 100% of salary, and its less than the down_payment -> user cannot afford down_payment!
    low = 0
    high = 10000
    portion_saved = ((low + high)/2)/10000 # / by 10,000 to get decimal - GUESS
    epsilson = 100
    steps = 0

    while abs(calculate_current_savings(portion_saved) - total_cost*portion_down_payment) >= epsilson: # Returns current_savings >> ((calculate_current_savings(portion_saved)). If bigger than EPSILON, continue guessing. If not, finish as guess good enough
        if calculate_current_savings(portion_saved) > total_cost*portion_down_payment:
            high = portion_saved*10000
            portion_saved = ((low + high)/2)/10000
        else:
            low = portion_saved*10000
            portion_saved = ((low + high)/2)/10000
        steps += 1
        
    print("Best savings rate is: ", portion_saved)
    print("Based on the code completition, current savings after 3 years will be: ", calculate_current_savings(portion_saved))
    print("Steps in bisection search: ", steps)
else:
    print("It is not possible to pay the down payment in 3 years")