#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 16 08:28:34 2023

@author: ewstott
"""

"""
Problem 2 - Paying Debt Off in a Year

Now write a program that calculates the minimum fixed monthly payment needed in order pay off a credit card balance 
within 12 months. By a fixed monthly payment, we mean a single number which does not change each month, 
but instead is a constant amount that will be paid each month.

In this problem, we will not be dealing with a minimum monthly payment rate.

The following variables contain values as described below:

balance - the outstanding balance on the credit card

annualInterestRate - annual interest rate as a decimal

The program should print out one line: the lowest monthly payment that will pay off all debt in under 1 year, 
for example:

Lowest Payment: 180 
Assume that the interest is compounded monthly according to the balance at the end of the month (
after the payment for that month is made). The monthly payment must be a multiple of $10 and is the same for all months. 
Notice that it is possible for the balance to become negative using this payment scheme, which is okay. 
A summary of the required math is found below:

Monthly interest rate = (Annual interest rate) / 12.0
Monthly unpaid balance = (Previous balance) - (Minimum fixed monthly payment)
Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)
"""
"""
TIPS:
    - making a guess for the minimum fixed monthly payment using Guess and check algo (easy one)
- Guesses must be multimples of 10
- balanceTemp used to reset as going through loops 
- May have to try ' if balanceTemp <= 0:' for while loop statement ? <<< 
 - BREAK ??

   
    # unpaidBalance = balance - minimumFixedMonthlyPayment
    # interest = unpaidBalance * (annualInterestRate/12.0)
    # balanceTemp = unpaidBalance + interest


PSEUDOCODE:

minimum fixed monthly payment = 10 
    
iterate over 12 months:
    unpaid balance is the balance minus the minimum fixed monthly payment 
    interest is the unpaid balance * annual interest rate divided by 12
    balance is unpaid balance + interest 
    
if balance is <= to 0:
    print result 
else: 
    minimum fixed monthly payment += 10 

"""

balance = 3329
annualInterestRate = 0.2

monthlyInterestRate = annualInterestRate/12.0
monthlyPayment = 10 
tempBalance = balance

while balance > 0:    
    for month in range(12):
        balance = balance - monthlyPayment + ((balance - monthlyPayment)* monthlyInterestRate)
    if balance > 0:
        monthlyPayment += 10
        balance = tempBalance   
    elif tempBalance <= 0:
        break
    
print("Lowest Payment: ", round(monthlyPayment, 2))
       
   












 
# for month in range(12):
#     unpaidBalance = balance - minimumFixedMonthlyPayment
#     interest = unpaidBalance * (annualInterestRate/12.0)
#     balanceTemp = unpaidBalance + interest
#         if balanceTemp <= 0:
#             print("Lowest Payment: ", lowestPayment)
#         else:
#             minimumFixedMonthlyPayment += 10
#             month += 1


