#trackbar practice
import cv2
import numpy as np

#create a black image and a window
img = np.zeros((300,512,3), dtype = np.uint8)
cv2.namedWindow('image')

#passes in position of trackbar
def nothing(x):
    pass

#create trackbars for color change
cv2.createTrackbar('R', 'image', 0, 255, nothing)
cv2.createTrackbar('G', 'image', 0, 255, nothing)
cv2.createTrackbar('B', 'image', 0, 255, nothing)

switch = '0 : OFF \n1: ON'
cv2.createTrackbar(switch, 'image', 0 , 1, nothing)

while True:
    cv2.imshow('image', img)
    k = cv2.waitKey(1) & 0xFF
    if k == 27: #keypress for esc
        break
    r = cv2.getTrackbarPos('R', 'image')
    b = cv2.getTrackbarPos('B', 'image')
    g = cv2.getTrackbarPos('G', 'image')
    #my original implementation 
    #img[...,0], img[...,1], img[...,2] = b, g ,r
    #cleaner
    img[:] = [b,g,r] #creates a view of original and sets each 'z' to this
    cv2.imshow('image', img)

cv2.destroyAllWindows()
    
