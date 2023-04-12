import cv2
import numpy as np

img = cv2.imread("Resources/lambo.png")
print(img.shape)   # output is (462,623,3) where 462-height , 623-width , 3-no. of color channels which is BGR

imgResize = cv2.resize(img,(1000,500))  # here note - width comes first , then the height
print(imgResize.shape)

# height first , then the width
imgCropped = img[0:200,200:500]

cv2.imshow("Image",img)
#cv2.imshow("Image Resize",imgResize)
cv2.imshow("Image Cropped",imgCropped)

cv2.waitKey(0)