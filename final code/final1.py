import cv2
import pytesseract
from pytesseract import Output
from PIL import Image


#get the text as in input

def graphtextdetextor(image_path):
    """
    pass image path as an argument
    """
    img=cv2.imread(image_path)

    #img=image_filter.rotate_anticlockwise(img)


    custom_config_number=r'--oem 3 --psm 6 outputbase digits'
    custom_config=r'--oem 3 --psm 6'

    custom_config1=r'--oem 3 --psm 1'

    custom_config2=r'--oem 3 --psm 4'

    text=pytesseract.image_to_string(img,config=custom_config)
    text2=pytesseract.image_to_string(img,config=custom_config1)
    text3=pytesseract.image_to_string(img,config=custom_config2)



    d=pytesseract.image_to_data(img,config=custom_config,output_type=Output.DICT)

    #print(text3)
    return [text,text2,text3]



 
image_path='final.jpeg'
d=graphtextdetextor(image_path) 
#print(d[1])


#spilited the string text
ss=d[2].split()
ww=[]
for i in range(len(ss)):
    ww.append(ss[i])
#print(ww)

# generated vertical and horizontal lines
import cv2
import numpy as np
import matplotlib.pyplot as plt


img=cv2.imread('final.jpeg',0)

    # Thresholding the image
(thresh, img_bin) = cv2.threshold(img, 254, 255,0)
    # Invert the image
img_bin = 255-img_bin 

    

    # Defining a kernel length
kernel_length = np.array(img).shape[1]//5
 
# A verticle kernel of (1 X kernel_length), which will detect all the verticle lines from the image.
verticle_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, kernel_length))
# A horizontal kernel of (kernel_length X 1), which will help to detect all the horizontal line from the image.
hori_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (kernel_length, 1))
# A kernel of (3 X 3) ones.
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))

# Morphological operation to detect vertical lines from an image
img_temp1 = cv2.erode(img_bin, verticle_kernel, iterations=3)
verticle_lines_img = cv2.dilate(img_temp1, verticle_kernel, iterations=3)
cv2.imwrite("verticle_lines.jpg",verticle_lines_img)
# Morphological operation to detect horizontal lines from an image
img_temp2 = cv2.erode(img_bin, hori_kernel, iterations=3)
horizontal_lines_img = cv2.dilate(img_temp2, hori_kernel, iterations=3)
cv2.imwrite("horizontal_lines.jpg",horizontal_lines_img)
    

'''
plt.imshow(horizontal_lines_img,cmap="gray")
plt.show()
plt.imshow(verticle_lines_img,cmap="gray")
plt.show()
plt.imshow(img,cmap="gray")
plt.show()
'''
#get the position of lines and no. of lines
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

#print(vlposx)

h,w=horizontalimage.shape


hlposy=[]
hw=w//2
for i in range(1,h):
    if horizontalimage[i-1,hw]==0 and horizontalimage[i,hw]==255:
        hlposy.append(i)
#print(hlposy)
heninu=len(hlposy)-1
#print(heninu)


#get the text string splitted to characters and get the position of text

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

#print(data)

import re
pdms=data.split()
Sum=0
Count=0
f=[]
tt=[]
q=[]
for i in range(0,len(pdms)):
    tt.append(pdms[i])


for i in range(0,len(tt),6):
    if(tt[i]!='~'):
        
        f.append(tt[i])
        vv=int(tt[i+1])+int(tt[i+3])
        y=vv//2
        q.append(y)
#print(f)
#print(q)


v=vlposx
t=q
m=f
c=ww

fh=0

arr1 = [[0 for i in range(len(v)-1)] for j in range(heninu)]
z=len(c[0])-1

i=0
while(i<len(c)):
    k=0
   # print(t[z])
   # print(min(v),max(v))
    if(t[z]>min(v) and t[z]<max(v)):
        while(k<(len(v)-1)):
            ps=""
#            print(i)
            while( i<len(c) and z<len(t) and k<(len(v)-1) and t[z]>v[k] and t[z]<v[k+1] ):
 #               print(c[i])
  #              print(" ")
                ps=ps+c[i]
               # print(z)
               # print(s)
                i=i+1
                ps=ps+" "
                if i<len(c):
                    z=z+(len(c[i]))
                
            arr1[fh][k]=ps
            k=k+1
        fh=fh+1
        
    else:
        i=i+1
    
print(arr1)



#give input array to csv code

fg=arr1[0]
#print(fg)
arr1.__delitem__(0)

# Python program to demonstrate 
# writing to CSV 

import csv 
	
# field names 
fields = fg
	
# data rows of csv file 
rows = arr1
	
# name of csv file 
filename = "marks.csv"
	
# writing to csv file 
with open(filename, "w") as csvfile: 
	# creating a csv writer object 
	csvwriter = csv.writer(csvfile) 
		
	# writing the fields 
	csvwriter.writerow(fields) 
		
	# writing the data rows 
	csvwriter.writerows(rows) 





