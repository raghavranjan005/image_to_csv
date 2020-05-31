import cv2
import matplotlib.pyplot as plt
import numpy as np

    

image_path="verticle_lines.jpg"
verticalimage=cv2.imread(image_path,0)

image_path="horizontal_lines.jpg"
horizontalimage=cv2.imread(image_path,0)


h,w=verticalimage.shape


hh=h//2
vlposx=[]
for i in range(1,w):
    if verticalimage[hh,i-1]==0 and verticalimage[hh,i]==255:
        vlposx.append(i)

print(vlposx)

h,w=horizontalimage.shape


hlposy=[]
hw=w//2
for i in range(1,h):
    if horizontalimage[i-1,hw]==0 and horizontalimage[i,hw]==255:
        hlposy.append(i)
print(hlposy)
print(len(hlposy)-1)
plt.imshow(horizontalimage,cmap="gray")
plt.show()

