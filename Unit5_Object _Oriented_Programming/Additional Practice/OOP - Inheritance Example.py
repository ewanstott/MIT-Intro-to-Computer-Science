#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 15 10:31:59 2023

@author: ewstott
"""


# 3. Inheritance Example

class A:
    def feature1(self):
        print("Feature 1 working")

    def feature2(self):
        print("Feature 2 working")

class B(A):  # << Child or Subclass (Inheriting all the features from Class A)
    def feature3(self):
        print("Feature 3 working")

    def feature4(self):
        print("Feature 4 working")

class C(A, B): # Class C show multimple inheritance, it inherits from Class A & Class B
    def feature5(self):
        print("Feature 5 working")


a1 = A()

a1.feature1()
a1.feature2()


b1 = B()

c1 = c()
c1.fe
