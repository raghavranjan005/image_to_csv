import cv2
import matplotlib.pyplot as plt
import numpy as np

    

image_path="verticle_lines.jpg"
image=cv2.imread(image_path,0)


h,w=image.shape
print(h)
print(w)
print(image[323,117])

hh=h//2
vlposx=[]
for i in range(1,w):
    if image[hh,i-1]==0 and image[hh,i]==255:
        vlposx.append(i)

print(vlposx)

plt.imshow(image,cmap="gray")
plt.show()

