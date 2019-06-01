"""
Morphological transformations are normally performed on binary images. 

A kernal tells you how to change the value of any given pixel by combining it with different amounts of the nighboring pixels.

"""
import cv2
import numpy as np


def nothing(x):
    pass


cap = cv2.VideoCapture(0)
cv2.namedWindow("Trackbars", cv2.WINDOW_NORMAL)
cv2.createTrackbar("LH", "Trackbars", 0, 179, nothing)
cv2.createTrackbar("LS", "Trackbars", 0, 255, nothing)
cv2.createTrackbar("LV", "Trackbars", 0, 255, nothing)
cv2.createTrackbar("UH", "Trackbars", 179, 179, nothing)
cv2.createTrackbar("US", "Trackbars", 255, 255, nothing)
cv2.createTrackbar("UV", "Trackbars", 255, 255, nothing)

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret:

        l_h = cv2.getTrackbarPos("LH", "Trackbars")
        l_s = cv2.getTrackbarPos("LS", "Trackbars")
        l_v = cv2.getTrackbarPos("LV", "Trackbars")
        u_h = cv2.getTrackbarPos("UH", "Trackbars")
        u_s = cv2.getTrackbarPos("US", "Trackbars")
        u_v = cv2.getTrackbarPos("UV", "Trackbars")

        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        lower_blue = np.array([l_h, l_s, l_v])
        upper_blue = np.array([u_h, u_s, u_v])
        mask = cv2.inRange(hsv, lower_blue, upper_blue)
        kernel = np.ones((5, 5), np.uint8)
        erosion = cv2.erode(mask, kernel)
        dilation = cv2.dilate(mask, kernel)
        opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel, iterations=2)
        closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
        result = cv2.bitwise_and(frame, frame, mask=mask)

        object = cv2.add(frame, frame, mask=erosion)
        cv2.imshow("frame", frame)
        cv2.imshow("Object", object)
        cv2.imshow("mask", mask)
        cv2.imshow("erosion", erosion)
        cv2.imshow("dilation", dilation)
        cv2.imshow("Opening", opening)
        cv2.imshow("Closing", closing)

    key = cv2.waitKey(1)
    if key == 27:
        break
cap.release()
cv2.destroyAllWindows()
