# Image is just a matrix or an array of pixels

import cv2
import numpy as np
# print("Package imported")


# img = cv2.imread("Resources/ab.png")
#
# cv2.imshow("Output",img)
# cv2.waitKey(0)




# Create a video capture object
# cap = cv2.VideoCapture("Resources/test_video.mp4")
#
# # Video is just sequence of images , so we'll need a while loop to go through each frame one by one
# while True:
#     success , img = cap.read()   # It will save our img into this vsriable img , and success variable will tell us whether it was done successfully or not
#     cv2.imshow("Video",img)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break



# cap = cv2.VideoCapture(0)
# cap.set(3,640)      # width - id no.3
# cap.set(4,480)      # height - id no.4
# cap.set(10,100)     # brightness - id no.10
#
# while True:
#     success , img = cap.read()   # It will save our img into this vsriable img , and success variable will tell us whether it was done successfully or not
#     cv2.imshow("Video",img)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break



img = cv2.imread("Resources/download.jpg")
kernel = np.ones((5,5),np.uint8)  # uint8 means unsigned integer of 8 bits , which means the values can range from 0 to 255

# Basically converts your image into different color spaces
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(7,7),0)
imgCanny = cv2.Canny(img,150,200)
imgDialation = cv2.dilate(imgCanny,kernel,iterations=1)  # how many iterations we want the kernel to move around , which means how much thickness do we actually need ! Dialation is used for making the edges thicker
# Opposite of dialation is erosion - to make the edges thinner
imgEroded = cv2.erode(imgDialation,kernel,iterations=1)

cv2.imshow("Gray Image",imgGray)
cv2.imshow("Blur Image",imgBlur)
cv2.imshow("Canny Image",imgCanny)
cv2.imshow("Dialation Image",imgDialation)
cv2.imshow("Eroded Image",imgEroded)
cv2.waitKey(0)
