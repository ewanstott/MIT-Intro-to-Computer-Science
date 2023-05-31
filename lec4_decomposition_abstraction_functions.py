
# Variable Scope
# This tells python we have a function named 'X', but don't care whats in the code yet becuase we havn't called the function yet. 
# def f(x):
#     x = x + 1
#     print('in f(x): x =', x)
#     return x # If no return statement, Python returns the value 'None'

# x = 3
# z = f(x) #< function call = 4 (x = x (3) + 1 )


# def is_even_with_return(i):
#     """
#     input: i, a positive int
#     Returns True if i is even, otherwise false
#     """
#     print('with return')
#     remainder = i % 2 
#     return remainder == 0

# is_even_with_return(3) # <- Returns False
# print(is_even_with_return(3))


# def is_even_without_return(i):
#     """
#     Input: i, a positive int
#     Does not retrun anything """
#     print('without return')
#     remainder = i % 2
#     # return None (Pythong automatically adds this) 

# is_even_without_return(3) # <- None
# print(is_even_without_return(3))

# # Simple is_even function definition
# def is_even(i):
#     """Input: i, a positive int
#     Returns True if i is even, otherwise False"""
#     remainder = i % 2
#     return remainder == 0

# # Use this is_even function later on in the code
# print("All numbers between 0 and 20: even or not")
# for i in range(20):
#     if is_even(i):
#         print(i, "even")
#     else:
#         print(i, "odd")


# def is_multiple_of_10(j):
#     remainder = j % 10
#     return remainder == 0

# print("All number divisible by 10 between 1 - 100")
# for j in range(100):
#     if is_multiple_of_10(j):
#         print(j, "multiple of 10")
#     else:
#         print(j, "Not multiple of 10")    
      
# def g(x):
#     def h():
#         x = 'abc'
#     x = x + 1
#     print('g: x =', x)
#     h()
#     return x

# x = 3
# z = g(x)

# Quiz 1. 
# def add(x, y):
#     return x+y

# def mult(x, y):
#     print(x*y)

# add(1,2)
# print(add(2,3))
# mult(3,4)
# print(mult(4,5))

# Quiz 2.
# def sq(func, x): 
#     y = x**2
#     return func(y)
# # y = 2**2 = 4
# # return func(y) = return func(4) (just remplacing the parameters i.e. y with 4)

# def f(x):
#     return x**2
# # def f(x) (where x = 4 from previous function)
# # f returns 4**4 = 16 

# # Function call is below
# calc = sq(f,2) # sq(func = f, x = 2)
# print(calc)

# def max_val(x, y):
#     if x > y:
#         return x
#     else:
#         return y

# max_val = max_val(3, 2)
# print(max_val)

def find_root(x, power, epsilon):
    # Find interval containing answer
    if x < 0 and power%2 == 0:
        return None # Negative number has no even-powered roots
    low = min(-1, x)
    high = max(1, x) 
    # Use bisection search
    ans = (high + low)/2
    while abs(ans**power - x) >= epsilon:
        if ans**power < x:
            low = ans
        else: 
            high = ans
        ans = (high + low)/2
    return ans

# find_root = find_root(1, powers, 0.001)
# print(find_root)

"""
Finger exercise 11: Write a function isIn that accepts two strings as
arguments and returns True if either string occurs anywhere in the other,
and False otherwise. Hint: you might want to use the built-in str
operation in.
"""

def is_In(str1, str2):
    if len(str1) > len(str2): # Comparing which string is longer and checking to see
        if str2 in str1:      # if the shorter string is present in the longer string 
        return True
    else:
        if str1 in str2:
        return True
    return False

test = isIn('abc','abcdef')
print(test)


