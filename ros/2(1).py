
import cv2
import numpy as np
#cap = cv2.VideoCapture(0)#创建一个 VideoCapture 对象

path = "C:/Users/syc/Desktop/green1.png"
img = cv2.imread(path)
# Convert BGR to HSV
while(1):
    feedback=0
    countred = 0
    countgreen = 0
 #   ret, img = cap.read()

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    # cv2.imshow("3",hsv)
    # cv2.waitKey(0)
    sensitivity = 15
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
    # define range of red color in HSV
    lower_red_0, upper_red_0 = np.array([0, 100, 100]), np.array([sensitivity, 255, 255])
    lower_red_1, upper_red_1 = np.array([180 - sensitivity, 100, 100]), np.array([180, 255, 255])
    # Threshold the HSV image to get a range of red color
    mask_0 = cv2.inRange(hsv, lower_red_0, upper_red_0)
    mask_1 = cv2.inRange(hsv, lower_red_1, upper_red_1)
    mask_red = cv2.bitwise_or(mask_0, mask_1)
    mask_red = cv2.morphologyEx(mask_red, cv2.MORPH_CLOSE, kernel)
    mask_red = cv2.morphologyEx(mask_red, cv2.MORPH_OPEN, kernel)


   # cv2.imshow('mask_red', mask_red)
    image = cv2.cvtColor(mask_red, cv2.COLOR_GRAY2BGR)

    cv2.waitKey(100)
    mediu = cv2.medianBlur(mask_red, 25)
    cv2.imshow("mediu",mediu)

    #cv2.imshow('1', mediu)
    #cv2.waitKey(1000)

    ret, thresh = cv2.threshold(mediu, 127, 255, cv2.THRESH_BINARY)
    contours, hierarchy = cv2.findContours(thresh, 1, 2)

    if len(contours):
        # print(len(contours))
        cnt = contours[0]
        if cv2.contourArea(contours[0]) > 300:
            cv2.imshow('image', img)
            cv2.imshow("mask", mask_red)
            x, y, w, h = cv2.boundingRect(cnt)
            cv2.rectangle(mediu, (x, y), (x + w, y + h), (111, 222, 222), 9)
            cv2.imshow('jx', mediu)
            mediu = mediu[y:y + h, x:x + w]
            cv2.imshow("last",mediu)
            countred = 1
    else:
        #print("wuhongse")
        countred = 0

    if (countred == 1):
        print("stop")
        feedback=1
        cv2.waitKey(100)
        countred == 0
        continue
        # continue
    '''
        x, y, w, h = cv2.boundingRect(cnt)
        cv2.rectangle(mediu, (x, y), (x + w, y + h), (100, 120, 130), 1)

        cv2.imshow('jx', mediu)

        mediu = mediu[y:y + h, x:x + w]
        print(y)
        print(y + h)
        print(x)
        print(x + w)
        zx = (y + y + h) / 2
        zx1 = ((w) / 2)
        zx2 = ((w) / 2) * 1000
        print(zx1)

        cv2.waitKey(1000)

        M = cv2.moments(mediu)  # 计算矩
        cv2.imshow("2", mediu)
        cv2.waitKey(1000)
        print(M)
        print("1")
        if (M['m00'] != 0):
            cx = int(M['m10'] / M['m00'])  # 计算重心
            cy = int(M['m01'] / M['m00'])
            # print (cy)
            print(cx)
            cx2 = cx * 1000
        if zx2 < cx2:
            print("right")
        else:
            print("left")
    '''
    lower_blue = np.array([35, 43, 46])
    upper_blue = np.array([77, 255, 255])
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    res = cv2.bitwise_and(img, img, mask=mask)
    mask = cv2.medianBlur(mask, 25)
    cv2.imshow('hsv', hsv)
    cv2.imshow('mask', mask)
    cv2.imshow('res', res)
    cv2.imshow('img', img)
    cv2.waitKey(100)

    ret, thresh = cv2.threshold(mask, 127, 255, cv2.THRESH_BINARY)
    contours, hierarchy = cv2.findContours(thresh, 1, 2)

    if len(contours):
        # print(len(contours))
        cnt = contours[0]
        if cv2.contourArea(contours[0]) > 300:
            countgreen = 1
    else:
        print("wulvse")
        countgreen = 0
        cv2.waitKey(100)
        continue

        # continue
    if (countgreen == 1):

        x, y, w, h = cv2.boundingRect(cnt)
        cv2.rectangle(mask, (x, y), (x + w, y + h), (100, 120, 130), 1)

        cv2.imshow('jx', mask)

        mask = mask[y:y + h, x:x + w]
        print(y)
        print(y + h)
        print(x)
        print(x + w)
        zx = (y + y + h) / 2
        zx1 = ((w) / 2)
        zx2 = ((w) / 2) * 1000
        print(zx1)

       # cv2.waitKey(1000)

        M = cv2.moments(mask)  # 计算矩
        cv2.imshow("2", mask)
        #cv2.waitKey(1000)
        print(M)
        print("1")
        if (M['m00'] != 0):
            cx = int(M['m10'] / M['m00'])  # 计算重心
            cy = int(M['m01'] / M['m00'])
            # print (cy)
           # print(cx)
            cx2 = cx * 1000
        if zx2 < cx2:
            print("right")
            feedback=2
        else:
            print("left")
            feedback=3
cv2.waitKey(200)
    # mediu = cv2.cvtColor(mediu,cv2.COLOR_BGR2GRAY)

    # print (cx)

'''

contours_green=detect_green(frame)
    contours_red = detect_red(frame)
    flag_green = 0
    flag_red = 0
    for contour in contours_green:
        if cv2.contourArea(contour) > 1000:
            flag_green = 1
            break
    for contour in contours_red:
        if cv2.contourArea(contour) > 1000:
            flag_red = 1
            break
    if flag_green:
        contours = contours_green
    elif flag_red:
        contours = contours_red
    else:
        print('-----------没有检测到------------')
        continue
'''