import cv2
import numpy as np
import matplotlib.pyplot as plt


img=cv2.imread('Capture1.PNG',0)

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
    


plt.imshow(horizontal_lines_img,cmap="gray")
plt.show()
plt.imshow(verticle_lines_img,cmap="gray")
plt.show()
plt.imshow(img,cmap="gray")
plt.show()


