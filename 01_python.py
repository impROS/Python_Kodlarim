# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 16:19:43 2018

@author: impROS
"""

print("A Sayisini Giriniz..")
a=input()

print("B Sayisini Giriniz..")
b=input()

c=int(a)+int(b)

print("A+B = ",c)

bilgiler =[a,b,c]
print("{}+{}={}".format(bilgiler[0],bilgiler[1],bilgiler[2]))