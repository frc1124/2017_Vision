import numpy as np
import cv2

widthMin = 5
heightMin = 5

cap = cv2.VideoCapture(1)
cv2.namedWindow('result')

while(1):
    _,frame = cap.read()
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    lower_val = np.array([37,60,225])
    upper_val = np.array([87,255,255])
    mask = cv2.inRange(hsv,lower_val, upper_val)

    _, contours, _= cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    search = []
    for cnt in contours:
        rect = cv2.minAreaRect(cnt)
        width = rect[1][0]
        height = rect[1][1]
        if (width >= widthMin) and (height > heightMin):
            search.append(cnt)

    cv2.drawContours(frame,search,-1,(0,255,0),3)

    cv2.imshow('result',frame)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()