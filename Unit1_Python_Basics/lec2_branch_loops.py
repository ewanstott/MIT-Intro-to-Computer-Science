#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 10 10:26:44 2023

@author: ewstott
"""

# hi = "hello there"
# name = "Ewan"
# greet = hi + " " + name
# print(greet)
# silly = hi + (" " + name)*3
# print(silly)

# x = float(input("Enter a number for x: "))
# y = float(input("Enter a number for y: "))
# if x == y:
#         print("x and y are equal")
#         if y != 0: #!= means not-equal-to
#             print("therefore, x / y is", x/y)
#         elif x < y:
#             print("x is smaller")
#         else:
#             print("y is smaller")
#         print("thanks!")

# n = input("You are in the Lost Forest\n****************\n****************\n :)\n****************\n****************\nGo left or right? ")
# while n == "right" or n == "Right":
#     n = input("You are in the Lost Forest\n****************\n******       ***\n  (â•¯Â°â–¡Â°ï¼‰â•¯ï¸µ â”»â”â”»\n****************\n****************\nGo left or right? ")
# print("\nYou got out of the Lost Forest!\n\o/")


# direction = input("You are in the lost forest. Left or right?")
# n = 0
# while n < 2:
#     print("dead end!!!")
#     n = n + 1
#  print("You escaped!")


# n = 0
# while n < 5:
#     print(n)
#     n = n+1


# for n in range(5):
#     print(n)

# mysum = 0
# for i in range(7,10):
#     mysum += i
# print(mysum)

# mysum = 0
# for i in range(5, 11, 2):
#     mysum += i
#     print(mysum)

# Write a program that examines three variables— x, y, and z—and prints the largest odd number among them. 
# If none of them are odd, it should print the smallest value of the three.

# answer = min(x, y, z)
# if x%2 != 0:
#     answer = x
# if y%2 != 0 and y > answer:
#     answer = y
# if z%2 != 0 and z > answer:
#     answer = z
# print(answer)

# x = 3
# ans = 0
# num_iterations = 0
# while (num_iterations < x):
#     ans = ans + x
#     num_iterations = num_iterations + 1
# print(f'{x}*{x} = {ans}')

# Find the cube root of a perfect cube
# x = int(input("Enter an integer: "))
# ans = 0
# while ans**3 < abs(x):
#     ans = ans + 1
# if ans**3 != abs(x):
#     print(x, 'is not a perfect cube')
# else:
#     if x < 0:
#         ans = -ans
#     print('Cube root of', x, 'is', ans)

# max_val = int(input("Enter a positive integer: "))
# i = 0
# while i < max_val:
#     i = i + 1
# print(i)

# Test if an int > 2 is prime. If not, smallest divisor
# x = int(input("Enter an integer greater than 2: "))
# smallest_divisor = None
# for guess in range(2, x):
#     if x%guess == 0:
#         smallest_divisor = guess
#         break
# if smallest_divisor != None:
#     print('Smallest divisor of', x, 'is', smallest_divisor)
# else:
#     print(x, 'is a prime number')
        
# More efficient code - no need to check even numbers beyond 2.
x = int(input("Enter an integer greater than 2: "))
smallest_divisor = None
if x%2 == 0:
    smallest_divisor = 2
else:
    for guess in range(3, x, 2):
        if x%guess == 0:
            smallest_divisor = guess
            break
if smallest_divisor != None:
    print('Smallest divisor', x, 'is', smallest_divisor)
    print(x, 'is a prime number')