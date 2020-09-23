import numpy as np
import cv2

red_lower = np.array([0,43,46])
red_upper = np.array([10,255,255])
green_lower = np.array([35,43,46])
green_upper = np.array([77,255,255])
cap = cv2.VideoCapture(0)

cap.set(3,320)
cap.set(4,240)
def ChestGreen():
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, green_lower, green_upper)
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.GaussianBlur(mask, (3, 3), 0)
    return mask
def ChestRed():
    ret, frame = cap.read()
    frame = cv2.GaussianBlur(frame, (5, 5), 0)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, red_lower, red_upper)
    mask = cv2.GaussianBlur(mask, (3, 3), 0)
    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
    if 25 < len(cnts) < 29:
        print("STOP!")
while 1:
    ret,frame = cap.read()
    frame = cv2.GaussianBlur(frame,(5,5),0)
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    mask = ChestGreen()
    ChestRed()
    res = cv2.bitwise_and(frame,frame,mask=mask)
    cnts = cv2.findContours(mask.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[-2]
    if len(cnts) > 0:
        c = max(cnts, key=cv2.contourArea)





        M = cv2.moments(c)

        center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
        x, y, w, h = cv2.boundingRect(mask)

        for i in range(0, len(cnts)):
            x, y, w, h = cv2.boundingRect(cnts[i])
            cv2.rectangle(mask, (x, y), (x + w, y + h), (255, 255, 0), 2)


            bottom_most = tuple(c[c[:, :, 1].argmax()][0])
            print("bottom_most", bottom_most)
            print("center", center)
            print("Green!")

    cv2.imshow("frame",frame)
    cv2.imshow("mask",mask)
    cv2.imshow("res",res)
    #cv2.imshow("img",img)
    if cv2.waitKey(5) & 0xFF == 27:
        break
cap.release()
cv2.destroyAllWindows()
