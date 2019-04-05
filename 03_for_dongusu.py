# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 22:37:55 2018

@author: impROS
"""
import sys
#print(*range(10,1,-1))

for i in range(9,1,-1):
    for j in range(1,i):
        sys.stdout.write('*')
        
    for l in range(1,10-i):
        sys.stdout.write(' ')
        
    for l in range(1,10-i):
        sys.stdout.write(' ')
        
    for j in range(1,i):
        sys.stdout.write('*')
    sys.stdout.write('\n')
#2.kisim
for i in range(2,10):
    for j in range(1,i):
        sys.stdout.write('*')
        
    for l in range(1,10-i):
        sys.stdout.write(' ')
        
    for l in range(1,10-i):
        sys.stdout.write(' ')
        
    for j in range(1,i):
        sys.stdout.write('*')
    sys.stdout.write('\n')
    

        
