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



 
image_path='Capture1.PNG'
d=graphtextdetextor(image_path) 
print(d[1]) 


    
    
        
            
        

    