import cv2

img = cv2.imread("0001.png", 1)

cv2.imshow("img", img)

cv2.waitKey(1000)
