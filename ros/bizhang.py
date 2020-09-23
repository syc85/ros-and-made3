# -*- coding: utf-8 -*-
import cv2
import numpy as np


#ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
#cap = cv2.VideoCapture(0)  # 创建一个 VideoCapture 对象

path = "C:\\Users\\syc\\Desktop\\ros\\red2.png"
img = cv2.imread(path)
# Convert BGR to HSV
while (1):
    countred = 0
    countgreen = 0
    #ret, img = cap.read()
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

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
    # cv2.imshow('image', img)
    # cv2.imshow('mask_red', mask_red)
    image = cv2.cvtColor(mask_red, cv2.COLOR_GRAY2BGR)

    # cv2.waitKey(100)
    mediu = cv2.medianBlur(mask_red, 19)
    # cv2.imshow('1', mediu)
    # cv2.waitKey(1000)

    ret, thresh = cv2.threshold(mediu, 127, 255, cv2.THRESH_BINARY)
    ret, contours, hierarchy = cv2.findContours(thresh, 1, 2)
    cv2.imshow('mediu1', mediu)
    if len(contours):
        # print(len(contours))
        cnt = contours[0]
        if cv2.contourArea(contours[0]) > 300:
            countred = 1
    else:
        countred = 0
        #ser.write('w'.encode())
        #response = ser.readall()
        #print(response)
        print("tz")
        continue
    if (countred == 1):
        M = cv2.moments(mediu)  # 计算矩
        if (M['m00'] != 0):
            cx = int(M['m10'] / M['m00'])  # 计算重心
            cy = int(M['m01'] / M['m00'])
            print(cx)
            # print(cy)
            size = mediu.shape
            (h, w) = size
            print(w / 2)
        cv2.waitKey(100)
        countred == 0
        if (cx - w / 2 > 100):
            #ser.write('r'.encode())
            #response = ser.readall()
            #print(response)
            print("turnleft(wei)")
        elif (cx - w / 2 < -100):
            #ser.write('l'.encode())
            #response = ser.readall()
            #print(response)
            print("turn rightwei)")
        else:
            #ser.write('f'.encode())
            #response = ser.readall()
            #print(response)
            print("tzhizou")
        countred = 0
        continue

    #############################################################################################################################33
'''
    lower_blue = np.array([35, 43, 46])
    upper_blue = np.array([77, 255, 255])
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    res = cv2.bitwise_and(img, img, mask=mask)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    mask = cv2.medianBlur(mask, 19)
    cv2.imshow('hsv', hsv)
    cv2.imshow('mask', mask)
    cv2.imshow('res', res)
    cv2.imshow('img', img)
    cv2.waitKey(100)

    ret, thresh = cv2.threshold(mask, 127, 255, cv2.THRESH_BINARY)
    ret, contours, hierarchy = cv2.findContours(thresh, 1, 2)

    if len(contours):
        #ser.write('g'.encode())
        #response = ser.readall()

        # print(len(contours))

    else:
        print("wulvse")
        countgreen = 0
        cv2.waitKey(100)
        continue
'''
        # continue
'''
    if (countgreen == 1):

        x, y, w, h = cv2.boundingRect(cnt)
        cv2.rectangle(mask, (x, y), (x + w, y + h), (100, 120, 130), 1)

'''
