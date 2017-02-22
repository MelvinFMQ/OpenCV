import numpy as np
import cv2

#returns a video capture object, the argument is the camera.
#There can be multiple cameras connected to the computer
cap = cv2.VideoCapture(0)

#define the codec and create videowriter object
#the start infront, unpacks the argument list
#e.g
#f(*[1,2,3]) == f(1,2,3)
fourcc = cv2.VideoWriter_fourcc(*'MJPG')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640,480))
while (True):
    #capture frame by frame
    #ret is return value - either true of false - true if gream is read properly.
    ret, frame = cap.read()
    if ret == True:
        frame = cv2.flip(frame, 0)
        #write the flip frame
        out.write(frame)
        #display the resulting frame
        cv2.imshow('frame', frame)
        
        #waitkey(1) returns the ascii value of keyboard pressed or -1 if nothing is pressed before delay
        #0xFF is hexidecimal for 16^2 == 11111111 in binary.
        #& is a bitwise operator, in this case, it returns the ascii code of the keypressed.
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

    
    
cap.release()
out.release()
cv2.destroyAllWindows()
