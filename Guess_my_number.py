# EXERCISE: Guess my number 
# Ask user for number between 0 & 100
# Print 1st guess at ans - 
# Ask user to enter h, l or c
    # if h:
        # h += ans
        

low = 0
high = 100
print("Please think of a number between 0 and 100!")

while True:
    guess = (high + low)//2
    print("Is your secret number " + str(guess) + "?")
    ans = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    if ans == 'c':
        print("Game over. Your secret number was: " + str(guess))
        break
    elif ans == 'l': # ans to low
        low = guess 
    elif ans == 'h': # ans to high
        high = guess
    else:
        print("Sorry, I did not understand your input.")