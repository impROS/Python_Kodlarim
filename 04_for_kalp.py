# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 23:30:28 2018

@author: impROS
"""
import sys
for i in range(10,0,-1):
    for j in range(0,10-i+1):
        sys.stdout.write(" ")


    for j in range(0,i):
        sys.stdout.write("*")
      
    for j in range(1,i-5):
        sys.stdout.write(" ")
    for j in range(1,i):
        sys.stdout.write("*")
    sys.stdout.write("\n")
        
    