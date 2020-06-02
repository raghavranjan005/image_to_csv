import pytesseract
from pytesseract import pytesseract
import PIL
from PIL import Image
import cv2
import csv


import cv2
import matplotlib.pyplot as plt
import numpy as np

img = 'final.jpeg'
imge = Image.open(img)
data=pytesseract.image_to_boxes(imge)

print(data)

import re
pdms=data.split()
Sum=0
Count=0
f=[]
t=[]
c=[]
for i in range(0,len(pdms)):
    t.append(pdms[i])


for i in range(0,len(t),6):
    if(t[i]!='~'):
        
        f.append(t[i])
        v=int(t[i+1])+int(t[i+3])
        y=v//2
        c.append(y)
print(f)
print(c)

