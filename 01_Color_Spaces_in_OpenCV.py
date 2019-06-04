"""
Using RealSense to learn the color space.
"""

import sys

import cv2
import numpy as np

import pyrealsense2 as rs
from realsense_opencv import DEVICE_ONE, DEVICE_TWO, Realsense

number = 0
for filename in dir(cv2):
    if filename.startswith('COLOR_'):
        number += 1
        print(filename)

print("There are {} kinds of color methods in OpenCV.".format(str(number)))


def nothing(x):
    pass


cv2.namedWindow("Video", cv2.WINDOW_NORMAL)

cv2.namedWindow("Tracking", cv2.WINDOW_NORMAL)
cv2.createTrackbar("LH", "Tracking", 0, 255, nothing)
cv2.createTrackbar("LS", "Tracking", 0, 255, nothing)
cv2.createTrackbar("LV", "Tracking", 0, 255, nothing)
cv2.createTrackbar("UH", "Tracking", 250, 255, nothing)
cv2.createTrackbar("US", "Tracking", 250, 255, nothing)
cv2.createTrackbar("UV", "Tracking", 250, 255, nothing)

camera_num = 1
camera = Realsense(camera_num=camera_num, device_id=[
                   DEVICE_TWO], color_resolution=[1280, 720], depth_resolution=[1280, 720])
try:
    while True:
        color_images, depth_images, depth_colormaps = camera.get_images()
        frame = color_images[0]
        hsv_frame = cv2.cvtColor(frame, cv2.COLOR_RGB2HSV)

        l_h = cv2.getTrackbarPos("LH", "Tracking")
        l_s = cv2.getTrackbarPos("LS", "Tracking")
        l_v = cv2.getTrackbarPos("LV", "Tracking")

        u_h = cv2.getTrackbarPos("UH", "Tracking")
        u_s = cv2.getTrackbarPos("US", "Tracking")
        u_v = cv2.getTrackbarPos("UV", "Tracking")

        l_b = np.array([l_h, l_s, l_v])
        u_b = np.array([u_h, u_s, u_v])

        mask = cv2.inRange(hsv_frame, l_b, u_b)
        res = cv2.bitwise_and(frame, frame, mask=mask)

        # Red color
        low_red = np.array([110, 154, 55])
        high_red = np.array([141, 218, 119])
        red_mask = cv2.inRange(hsv_frame, low_red, high_red)
        red = cv2.bitwise_and(frame, frame, mask=red_mask)

        # Blue color
        low_blue = np.array([0, 64, 38])
        high_blue = np.array([28, 203, 128])
        blue_mask = cv2.inRange(hsv_frame, low_blue, high_blue)
        blue = cv2.bitwise_and(frame, frame, mask=blue_mask)

        # Green color
        low_green = np.array([36, 103, 56])
        high_green = np.array([85, 212, 211])
        green_mask = cv2.inRange(hsv_frame, low_green, high_green)
        green = cv2.bitwise_and(frame, frame, mask=green_mask)

        # Every color except white
        low = np.array([0, 42, 0])
        high = np.array([179, 255, 255])
        mask = cv2.inRange(hsv_frame, low, high)
        result = cv2.bitwise_and(frame, frame, mask=mask)

        cv2.imshow("Video", frame)
        cv2.imshow("Red", red)
        cv2.imshow("Blue", blue)
        cv2.imshow("Green", green)
        cv2.imshow("Result", result)

        key = cv2.waitKey(2)
        if key == ord('q') or key == 27:
            cv2.destroyAllWindows()
            break
finally:
    # Stopped streaming
    camera.stop()
