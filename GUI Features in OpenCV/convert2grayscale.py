import numpy as np
import cv2

img = cv2.imread('files\picture2.jpg', cv2.IMREAD_GRAYSCALE)
#cv2.IMREAD_GRAYSCALE) #0
#cv2.IMREAD_COLOR
cv2.imshow('image', img)
k = cv2.waitKey(0)
if k == 27: #id for esc
    cv2.destroyAllWindows()
elif k == ord('s'): #ascii for s
    cv2.imwrite('picture2grey.jpg', img)
    cv2.destroyAllWindows()
    
