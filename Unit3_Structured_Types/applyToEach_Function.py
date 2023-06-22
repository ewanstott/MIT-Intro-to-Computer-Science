#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 08:47:20 2023

@author: ewstott
"""

L = [1, -2, 3.4]

def applyToEach(L, f):
    """assumes L is a list, f a function
    mutates L by replacing each element, 
    e, of L by f(e)"""
    for i in range(len(L)):
        L[i] = f(L[i])
        
applyToEach(L, abs)
applyToEach(L, int)
applyToEach(L, fact)
applyToEach(L, fib)