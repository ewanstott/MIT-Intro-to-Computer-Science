#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 09:56:52 2023

@author: ewstott
"""

L1 = [1,2,3,4]
L2 = [1,2,5,6]

# Function to remove duplicates
def remove_dups(L1, L2):
    for e in L1:
        if e in L2:
            L1.remove(e)

# However, this function doesn't remove the duplicate char '2', becuase Python automatically iterates in background and when '1' is removed as a dup, 
# it iterates over 2 as 2 has moved its order.

# We can use a function that creates a copy first to fix this:
def remove_dups(L1, L2):
    L1_copy = L1[:]
    for e in L1_copy:
        if e in L2:
            L1.remove(e)

