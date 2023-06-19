#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 06:57:50 2023

@author: ewstott
"""

"""
We can use the idea of bisection search to determine if a character is in a string,
so long as the string is sorted in alphabetical order.

First, test the middle character of a string against the character you're looking for (the "test character"). 
If they are the same, we are done - we've found the character we're looking for!

If they're not the same, check if the test character is "smaller" than the middle character.
If so, we need only consider the lower half of the string; 
otherwise, we only consider the upper half of the string. 
(Note that you can compare characters using Python's < function.)

Implement the function isIn(char, aStr) which implements the above idea recursively to test if char is in aStr. 
char will be a single character and aStr will be a string that is in alphabetical order. 
The function should return a boolean value.

As you design the function, think very carefully about what the base cases should be.
"""

"""
Psuedocode:

Function:
Base case: 
    What happens when the string is empty? We haven't found the char we are looking for
    What happens when the string is of length 1? We haven't found the char we are looking for
    What happens when the test character equals the middle character? We've found the char we are looking for!

Is middle char same as "test char" 
    if same - we've found the char we are looking for!

else: check if test char < middle char (use string slicing?)
    if so, consider lower half of string
    else: consider upper half od string

"""

def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
# Base cases
def isIn(char, aStr):
    if aStr == "":
        return False
    elif len(aStr) == 1 and aStr == char:
        return True
    elif len(aStr) == 1 and aStr != char:
        return False
    elif aStr[len(aStr)//2] == char: # take middle of string, is it same as char? if yes, return true
        return True
    else:
        if char < aStr[len(aStr)//2]: # else, os char < 
            return isIn(char, aStr[:len(aStr)//2]) # ':' symbol at START of string, prints 1st half of strings chars
        else:
            return isIn(char, aStr[len(aStr)//2:]) # ':' symbol at END of string, prints 2nd half of strings chars

isIn('a', 'ewanstott')
isIn('o ', 'ewanstott')
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
# def toChars(s):
# aStr = aStr.lower()
# testChar = ""
# for c in aStr:
#     if c in 'aStr' 
#     testChar = testChar + c


# def testChar(aStr)
# testChar = ""
#     # Base case: 
# if mid("aStr") == testChar: # If middle of string - testChar, return True
#     return True 
# else len(aStr) <= 1: # If a string of length 0 or 1 = False, so continue guessing
#     return 

# while False:
# # Bisection search??
#     if testChar < # middle char



