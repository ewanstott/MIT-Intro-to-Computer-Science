#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 10:22:31 2023

@author: ewstott
"""

# APPLY TO EACH

"""
 >>> print(testList)
  [1, 4, 8, 9]
"""
testList = [1, -4, 8, -9]

def absolute(a):
    return abs(a)

applyToEach(testList, absolute)




"""
 >>> print(testList)
  [2, -3, 9, -8]
"""
def addOne(a):
    return a + 1

applyToEach(testList, addOne)





"""
  >>> print testList
  [1, 16, 64, 81]
"""
def square(a):
    return a * a 

applyToEach(testList, square)