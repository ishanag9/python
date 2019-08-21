# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 15:35:33 2019

@author: Ishan Agrawal
"""
import math
import random

p = input("Enter value of p\n")
q = input("Enter value of q\n")
r = input("Enter value of r\n")
a = float(p)
b = float(q)
c = float(r)
A = math.acos((a*a - b*b - c*c) / (-2*b*c))
B = math.acos((b*b - a*a - c*c) / (-2*a*c))
C = math.acos((c*c - b*b - a*a) / (-2*a*b))
print(math.degrees(A))
print(math.degrees(B))
print(math.degrees(C))

print(format(57.467657,'10.2f'))
print(format(12345678.923,'10.2f'))
print(format(57.4,'10.2f'))
print(format(57,'10.2f'))

print(format(57.467657,'<10.2f'))
x = "Hello"
print("{:50s}".format(x))
print("{:<50s}".format(x))
print("{:>50s}".format(x))
    

x = random.randint(0,9)
y = random.randint(0,9)
z = x + y
print(z) 
a = int(input("Enter your answer"))
if a == z:
    print("Correct")
else:
    print("Wrong")
    
    
    
    
