"""
Using RealSense to do realtime object tracking and detection

To change the color space, use cv2.cvtColor(img,flags).
    flags:
    The most widely used color-space conversion methods are: 
    - BGR <-> GRAY: cv2.COLOR_BGR2GRAY
    - BGR <-> HSV: cv2.COLOR_BGR2HSV

HSV: (Hue, Saturation, Value)
    - Hue: corresponds to the color components (base pigment), hence just by selecting a range of Hue you can select any color. (0-360)
    - Saturation: the amount of color. (depth of the pigment, dominance of Hue) (0-100%)
    - Value: the brightness of the color. (0-100%)

Note: For HSV:
    - Hue range is [0,179]
    - Saturation range is [0,255]
    - Value range is [0,255]
    Different softwares use different scales. So if you are comparing OpenCV values with them, you need to normalize these ranges.
"""

# Import the packages
import sys

import cv2
import numpy as np
import pyrealsense2 as rs

from realsense_opencv import DEVICE_ONE, DEVICE_TWO, Realsense

# Print the color spaces methods
number = 0
for filename in dir(cv2):
    if filename.startswith('COLOR_'):
        number += 1
        print(filename)

print("There are {} kinds of methods about color spaces in OpenCV.".format(str(number)))


# Define the callback function
def nothing(x):
    pass


# Create windows to contain the image
cv2.namedWindow("Video", cv2.WINDOW_NORMAL)
cv2.namedWindow("Tracking", cv2.WINDOW_NORMAL)
cv2.createTrackbar("LH", "Tracking", 0, 179, nothing)
cv2.createTrackbar("LS", "Tracking", 0, 255, nothing)
cv2.createTrackbar("LV", "Tracking", 0, 255, nothing)
cv2.createTrackbar("UH", "Tracking", 20, 179, nothing)
cv2.createTrackbar("US", "Tracking", 250, 255, nothing)
cv2.createTrackbar("UV", "Tracking", 250, 255, nothing)

# Register the RealSense camera
camera_num = 1
camera = Realsense(camera_num=camera_num, device_id=[
                   DEVICE_TWO], color_resolution=[1280, 720], depth_resolution=[1280, 720])
try:
    while True:
        # Read the image, realsense are
        color_images, depth_images, depth_colormaps = camera.get_images()
        frame = color_images[0]
        # Change the image color space from RGB -> HSV
        hsv_frame = cv2.cvtColor(frame, cv2.COLOR_RGB2HSV)

        # Get the current positions of trackbars
        l_h = cv2.getTrackbarPos("LH", "Tracking")
        l_s = cv2.getTrackbarPos("LS", "Tracking")
        l_v = cv2.getTrackbarPos("LV", "Tracking")

        u_h = cv2.getTrackbarPos("UH", "Tracking")
        u_s = cv2.getTrackbarPos("US", "Tracking")
        u_v = cv2.getTrackbarPos("UV", "Tracking")

        lower_threshold = np.array([l_h, l_s, l_v])
        upper_threshold = np.array([u_h, u_s, u_v])

        # Define range of color in HSV
        mask = cv2.inRange(hsv_frame, lower_threshold, upper_threshold)
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

        # Show the image
        cv2.imshow("Video", frame)
        cv2.imshow("Red", red)
        cv2.imshow("Blue", blue)
        cv2.imshow("Green", green)
        cv2.imshow("Result", result)

        # Wait until a key pressed
        key = cv2.waitKey(2)
        if key == ord('q') or key == 27:
            cv2.destroyAllWindows()
            break
finally:
    # Stopped streaming
    camera.stop()
