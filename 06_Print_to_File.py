# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 01:00:05 2018

@author: impROS
"""
import os
import sys
dosya=open("deneme.txt","a")
print("impROS",file=dosya)
dosya.close()

print(os.getcwd())

print("Ridvan","Orhan","Seyhmus",end="\n",sep=" - ",
      file=sys.stdout)

#kalici olarak yazma yerini degistir
dosya=open("deneme.txt","a")
sys.stdout=dosya

print("bu Komut da dosyaya yazılacak",flush=True)
