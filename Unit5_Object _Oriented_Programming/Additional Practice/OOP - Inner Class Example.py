#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 15 10:30:47 2023

@author: ewstott
"""


# 2. Inner classes example (class within a class):

class Student:

    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.Laptop()

        
    def show(self):
        print(self.name, self.rollno)
        self.lap.show()         
    
    class Laptop: # inner class
        
        def __init__(self):
            self.brand = 'HP'
            self.cpu = 'i5'
            self.ram = 8

        def show(self):
            print(self.brand, self.cpu, self.ram)


s1 = Student('Navin',2)
s2 = Student('Ewan',3)

s1.show()
        