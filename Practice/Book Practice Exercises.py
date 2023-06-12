#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 10 08:41:50 2023

@author: ewstott
"""

#print('abc'[1])
#print('abc'[1:3])
#name = input('enter name: ')
# print('are you really', name, '?')

# birthday = input('Enter birthday in the form mm/dd/yyyy: ')
# year = birthday[-4:]
# print('You were born in the year', year)

# x = 3
# ans = 0
# num_interations = 0
# while (num_interations < x):
#     ans = ans + x
#     num_interations = num_interations + 1
# print(f'{x}*{x} = {ans}')

# total = 0
# for num in (77, 11, 3):
#     total = total + num
# print(total)

# x = 4
# for i in range(x):
#     print(i)

x = 4
for j in range(x):
    print('Iteration of outer loop')
    for i in range(x):
        print('    Iteration of inner loop')
        x = 2
        