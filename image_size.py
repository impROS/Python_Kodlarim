# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 15:23:05 2018

@author: impROS
"""

from PIL import Image
im=Image.open("dog.jpg")
width,height=im.size
print(width," ",height)