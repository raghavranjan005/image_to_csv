import cv2
import pytesseract
from pytesseract import Output
from PIL import Image




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
    text4=pytesseract.image_to_string(img,config=custom_config_number)


    d=pytesseract.image_to_data(img,config=custom_config,output_type=Output.DICT)

    #print(text3)
    return [text,text2,text3,text4]



 
image_path='Capture1.PNG'
d=graphtextdetextor(image_path) 
print(d[1]) 



s=d[1]
f=s.split('\n')
count=0
d=list(f)

for i in d:
    for j in i:
        if(j==" "):
            count=count+1
   
    break

p=s.split()
#print(count)
Count1=0
b=[]

for i in range(0,len(p),count+1):
    t=[]
    for l in range(count+1):
        c=p[i+l]
        t.append(c)
        
    
    b.append(t)

#print(b)

'''
Sum=0
for i in range(1,len(b)):
    for j in range(len(b[i])):
        Sum=Sum+int(b[i][1])
        break
print(Sum)
'''

fg=b[0]
#print(fg)
b.__delitem__(0)

# Python program to demonstrate 
# writing to CSV 

import csv 
	
# field names 
fields = fg
	
# data rows of csv file 
rows = b 
	
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


    
  
        
            
        

    