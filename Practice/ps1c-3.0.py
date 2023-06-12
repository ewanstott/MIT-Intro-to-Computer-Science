#To save the down payment in 3 years, how much should I save each month? 
#Calculate best savings rate to achieve a down payment in 36 months

savings_rate = 0.03 #1st guess 

semi_annual_raise = 0.07
annual_return = 0.04
down_payment = 0.25
house_cost = 1000000
high = 10000
low = 0
months = 36 
num_guesses = 0
current_savings = 0

starting_salary = float(input("Enter starting salary: "))

#Use bisection search and a counter 
guess = (high + low)/2.0

while current_savings <= down_payment: #if this condition is FALSE, keep guessing 
    if guess < savings_rate: #<<?? CHECK THIS, NOT CORRECT                                      #if guess too low, set the low to be the guess
        low = guess
    else:
        high = guess
    guess =  (high + low)/2.0 #with new low and high boundaries, make another guess. Halving interval with every guess.
    num_guesses =+ 1 

    current_savings += portion_saved*monthly_salary + current_savings*monthly_return
    months += 1 

    if True:
        print("Percentage of salary you need to save per month to achieve down payment: ", savings_rate)

    if False:
        print("Not possible to save for a down payment in 36 months")


print("num_guesses: ", num_guesses)