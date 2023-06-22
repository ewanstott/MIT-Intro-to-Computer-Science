#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 10:27:19 2023

@author: ewstott
"""
"""
assumes L is a list, f is a function
mutates L by replacing eacg element of x, of L by f(x)
"""

def square(a):
    return a*a
def halve(a):
    return a/2
def inc(a):
    return a+1


def applyEachTo(L, x):
    result = []
    for i in range(len(L)):
        result.append(L[i](x))
    return result


applyEachTo([inc, square, halve, abs], -3)

