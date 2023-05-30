#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 11 10:45:18 2023

@author: ewstott
"""

# s = "abc"
# s[1]

# s = "hello"
# s = 'y'+s[1:len(s)]

an_letters = "aefhilmnorsxAEFHILMNORSX"
word = input("I will cheer for you! Enter a word: ")
times = int(input("Gnar level (1-10): "))

i = 0
while i < len(word):
    char = word[i]
    if char in an_letters:
        print("Give me an " + char + "! " + char)
    else:
        print("Give me a " + char + "!! " + char)
    i += 1