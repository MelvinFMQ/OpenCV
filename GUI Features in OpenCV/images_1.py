import numpy as np
import cv2

#use this function to read a file
#path can be relative or full path
#for windows uses backslashes
#if no file is there, function wil not throw an eroor, but return none
img = cv2.imread('files\picture2.jpg',0)
#first arguement is the name of the window can create as many windows as you wish. 
cv2.imshow('image', img)
#function is keybinding function (aka handler), arugment is the number of miliseconds
#if 0 is passed, window will wait for an indefinate time
#it also handles more then key presses, MUST USE IT TO DISPLAY IMAGES
cv2.waitKey(0)
#to destroy a specific window, use destroyWindow( name of window)
#create a named window by namedWindow(name: string, cv2.WINDOW_NORMAL )
cv2.destroyAllWindows()
#does not create files
cv2.imwrite('picture2.png', img)
