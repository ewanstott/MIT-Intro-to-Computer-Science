#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 11 07:36:19 2023

@author: ewstott
"""
"""
Telusko Tutorial: OOP in Python | Object Oriented Programming
"https://www.youtube.com/watch?v=qiSCMNBIP2g"
"""

# << ---------------------------------- >>

# 1. Classes and objects

class Student:

    school = 'Bristol'
    
    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
        
    def avg(self):
        return (self.m1 + self.m2 + self.m3)/3
    
    @classmethod
    def getSchool(cls):
        return cls.school
    
    @staticmethod
    def info():
        print("This is Student class")
        


s1 = Student(34,54,65)
s2 = Student(65,34,12)

print(s1.avg())
print(Student.getSchool())

Student.info()











































            # Attributes aka Varialbles
            # Behavior aka Methods (Function)
            
#     def __init__(self,cpu,ram):
#     self.cpu = cpu
#     self.ram = ram
 
         
            
#     def config(self):
#         print("Config is ", self.cpu, self.ram)
        

# com1 = Computer('i5', 16)
# com2 = Computer('Ryzen 3', 8)


# com1.config()
# com2.config()

