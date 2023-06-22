#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 09:23:00 2023

@author: ewstott
"""

map(abs, [1, -2, 3, -4])

for elt in map(abs, [1, -2, 3, -4]):
    print(elt)
    

L1 = [1, 28, 36]
L2 = [2, 57, 9]

for elt in map(min, L1, L2):
    print(elt)