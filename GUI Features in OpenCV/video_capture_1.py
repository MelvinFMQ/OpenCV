import numpy as np
import cv2

#returns a video capture object, the argument is the camera.
#There can be multiple cameras connected to the computer
cap = cv2.VideoCapture(0)

#read from file
#cap = cv2.VideoCapture('output.avi')

while (True):
    #capture frame by frame
    #ret is return value - if it is read correctly --> true
    ret, frame = cap.read()
    if ret:

        # Our operations on the frame come here
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        #display the resulting frame
        cv2.imshow('frame', gray)
        #waitkey(1) returns the ascii value of keyboard pressed or -1 if nothing is pressed before delay
        #0xFF is hexidecimal for 16^2 == 11111111 in binary.
        #& is a bitwise operator, in this case, it returns the ascii code of the keypressed.
        if ret and cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()
