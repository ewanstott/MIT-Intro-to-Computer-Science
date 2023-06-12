#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 08:14:14 2023

@author: ewstott
"""

# For loop
# Compare letter a to b, if a < b, a> b, a == a,  
# Print longest substring of s in which letters occur in alphabetical order

# Tips
# solution is simpler than you think, ~10 lines of code
# Builds on problem 2
# Instead of looking for 'bobs', looking for biggest substring 
# KEY - You can order or compare the order of strings (refer to lecture)
# To count longest variable, think about using multiple variables
# Require integers for your loops
# ALPHABETICAL ORDER COMPARISON 
# Convert to numbers ? 

# PSEUDOCODE
# s = 'abcbcd'
# longestString = create an empty string to hold alphabetical substrings

# iterate over string 
    # compare neighbours 
    # if neighbour 1 <= neighbour 2
        # store that value
        # Is your current substring longer than any previous one? 
            # if so, remember that! (check string length with (len(string))
    # Else: you don't have an alpha substring so get rid of your current alpha substring
# print result 

# cSS = currentSubString

s = 'azcbobobegghakl'
currentS = s[0]
longestS = s[0]
maxLen = 0

for i in range(len(s)-1): # iterate over string 
    if s[i+1] >= s[i]:    # if neighbour 1 <= neighbour 2
        currentS += s[i+1]   # store that value in currentS
        if (len(currentS)) > maxLen: # Is your current substring longer than any previous one? 
            maxLen = len(currentS)
            longestS = currentS # if so, remember that! # <- check how to replace currentSS with previousSS)
    else:
        currentS = s[i+1] # challenge here is not to reset longest string! Check! 
    i+=1
print("Longest substring in alphabetical order is: ", longestS)
    
    
    # Take neightbour 2 and add on to currentS
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # elif s[i] > s[i+1]:
    # # if 'a' is greater than 'z', do nothing
    # else s[i] == s[i+1]:
    # # if 'a' is equal to 'z', do nothing
    # i += 1
        
        # if in alphabetical order, store in temp

















    
    
  