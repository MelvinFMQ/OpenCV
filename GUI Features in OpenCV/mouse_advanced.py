import cv2
import numpy as np

img = np.zeros((512,512,3), dtype = 'uint8')
start = (0,0)
end = (0,0)
draw = False
cv2.namedWindow('image')
def cal_dis(start, end):
    delta_x = start[0] - end[0]
    delta_y = start[1] - end[1]
    combined = int((delta_x ** 2 + delta_y ** 2) ** 0.5) //2 
    return combined

print(cal_dis((1,2),(3,4)))


def drawcircle(event, x,y, flags, params):
    global start, end , draw
    if event == cv2.EVENT_LBUTTONDOWN:
        draw = True
        start = (x, y)
        print('mouse down')
    elif event == cv2.EVENT_MOUSEMOVE:
        if draw:
            cv2.circle(img, (x,y) , 5, (255, 0 ,0 ), -1)
    elif event == cv2.EVENT_LBUTTONUP:
        draw = False
        end = (x, y)
        print('mouse up')
        cv2.circle(img, (int(start[0] + end[0] )// 2, int(start[1] + end[1]) // 2) , cal_dis(start, end), (255, 0 ,0 ), -1)

cv2.setMouseCallback('image', drawcircle)

while True:
    cv2.imshow('image', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
