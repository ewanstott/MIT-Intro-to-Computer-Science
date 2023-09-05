#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 15 10:41:02 2023

@author: ewstott
"""

# 3. Constructor in Inheritance

class A:
    
    def __init__(self):
        print("in A Init")
    
    def feature1(self):
        print("Feature 1 working")

    def feature2(self):
        print("Feature 2 working")

class B:  # << Child or Subclass (Inheriting all the features from Class A)
    
    def __init__(self):
        print("in B Init")

    def feature3(self):
        print("Feature 3 working")

    def feature4(self):
        print("Feature 4 working")


class C(A,B):
    
    def __init__(self):
        print("in C init")

a1 = C()
