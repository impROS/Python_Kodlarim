# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 15:25:29 2017

@author: impROS
"""

from PIL import Image
img = Image.open("dog.jpg")
area = (97, 126, 586, 445)
cropped_img = img.crop(area)
cropped_img.show()