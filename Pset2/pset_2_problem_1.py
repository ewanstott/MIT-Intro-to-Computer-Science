#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 09:53:13 2023

@author: ewstott
"""
"""
Problem 1 - Paying Debt off in a year

Write a program to calculate the credit card balance after one year if a person only pays the 
minimum monthly payment required by the credit card company each month.

For each month, calculate statements on the monthly payment and remaining balance.
At the end of 12 months, print out the remaining balance. 

A summary of the required math is found below:
    
Monthly interest rate= (Annual interest rate) / 12.0
Minimum monthly payment = (Minimum monthly payment rate) x (Previous balance)
Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)


Psuedocode:
- At beginning of month 0, you owe b0 (b = balance, 0 = month)
Thus, unpaid balance for month 0 is ub0 = b0 - p0
- At the beginning on month1, you are charged interest on unpaid balance
Take Annual interest rate, at the beginning of month1, then New Balance is your Previous Balance, plus Interest
on this Unpaid Balance for the month = b1 = ubo + r/12.0 * ub1
- In month 1, we make another payment, p1. 
The balance at the beginning of month 2 (b2), can be calulated by first calculating the unpaid balance after paying p1, 
then adding the interest accrued: 


"""
# SOLUTION 1:
    
# Initialized variables
# balance = 42
# annualInterestRate = 0.2
# monthlyPaymentRate = 0.04

# for months in range(12):
#     balance = balance - (balance * monthlyPaymentRate) + ((balance - (balance * monthlyPaymentRate)) * (annualInterestRate/12))
#     months += 1
# print("Remaining balance: ", round(balance, 2))
    

##############

# SOLUTION 2:

balance = 484
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
monthlyInterestRate = annualInterestRate / 12.0

for month in range(12):
    minMonthlyPayment =  monthlyPaymentRate * balance
    unpaidBalance = balance - minMonthlyPayment    
    updatedPayment = unpaidBalance + (monthlyInterestRate * unpaidBalance)
    balance = unpaidBalance + (monthlyInterestRate * unpaidBalance)
    month += 1

print("Remaining balance: ", round(balance, 2))
