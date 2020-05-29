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



    d=pytesseract.image_to_data(img,config=custom_config,output_type=Output.DICT)

    #print(text3)
    return [text,text2,text3]



def findSum(str1): 
  
    # A temporary str1ing 
    temp = "0" 
  
    # holds sum of all numbers  
    # present in the str1ing 
    Sum = 0
  
    # read each character in input string 
    for ch in str1: 
  
        # if current character is a digit 
        if (ch.isdigit()): 
            temp += ch 
  
        # if current character is an alphabet 
        else: 
              
            # increment Sum by number found  
            # earlier(if any) 
            Sum += int(temp) 
  
            # reset temporary str1ing to empty 
            temp = "0"
          
    # atoi(temp.c_str1()) takes care  
    # of trailing numbers 
    return Sum + int(temp) 
image_path='Capture1.PNG'
d=graphtextdetextor(image_path) 
print(d[1]) 
#print(findSum(d[1]) )
    