import cv2
import numpy as np

path = "C:\\Users\\syc\\Desktop\\red.png"
img = cv2.imread(path)
# Convert BGR to HSV
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
cv2.imshow('image', img)
cv2.imshow('mask_red', mask_red)
image = cv2.cvtColor(mask_red, cv2.COLOR_GRAY2BGR)





cv2.waitKey(0)