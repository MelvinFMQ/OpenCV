import cv2
import numpy as np

#create a black image
#create an array of diemensions 512 * 512* 8 with datatpye unsinged int8
img = np.zeros((512,512,3), np.uint8)

#draw from what point (512) to what point (512), colour of blue ( 255,0,0) BGR , and thickness of 5
cv2.line(img, (0,0), (511,511), (255,0,0), 5)
#same as line but draw rectange, green and thickness of 3
cv2.rectangle(img, (384, 0), (510,128), (0,255,0), 3)

#point, (major axis, minor axis), angle ,angle start, angle end ,  color, thickness
cv2.ellipse(img, (256,256), (100, 50), 0,90,180,(0,255,0),-1)

#must be type int32
pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
print(pts.shape) # 4  * 2
print(pts[0,0])
pts = pts.reshape((-1,1,2)) #reshape to diementions 4,1,2 --> -1 is auto calculated
print(pts)
cv2.polylines(img, [pts], True, (0,255,255))

cv2.imshow('image', img)

font = cv2.FONT_HERSHEY_SIMPLEX


i = 0

cap = cv2.VideoCapture(0)
while cv2.waitKey(10) != ord('q'):
    ret, img = cap.read()
    if i > 512:
        i = -512
    #point, radius, redline, thickeness
    cv2.circle(img, ((512 + i)//2,512), 63, (0,0,255), -1)
    cv2.circle(img, ((511-63-63 + i)//2,512), 63, (0,0,0), -1)
    #text, point, font, size, color, thickness , or default look 
    cv2.putText(img, 'fk', ((10 + i)//2,256), font , 4, (255,255,255), 2, cv2.LINE_AA)
    cv2.putText(img, 'fk', ((9 + i)//2,256), font , 4, (0,0,0), 2, cv2.LINE_AA)
    #print(i)
    cv2.imshow('image', img)    
    i += 10
cv2.destroyAllWindows


