"""
Color spaces in OpenCV

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
import cv2
import numpy as np

# Define the callback function


def nothing(x):
    pass


# Create a window to contain the image
cv2.namedWindow("Tracking", cv2.WINDOW_NORMAL)
cv2.createTrackbar("LH", "Tracking", 0, 179, nothing)
cv2.createTrackbar("LS", "Tracking", 0, 255, nothing)
cv2.createTrackbar("LV", "Tracking", 0, 255, nothing)
cv2.createTrackbar("UH", "Tracking", 250, 255, nothing)
cv2.createTrackbar("US", "Tracking", 250, 255, nothing)
cv2.createTrackbar("UV", "Tracking", 250, 255, nothing)

while True:
    # Read the image
    frame = cv2.imread('./images/smarties.png')

    # Change the image color space from BGR -> HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Get the current positions of trackerbar
    l_h = cv2.getTrackbarPos("LH", "Tracking")
    l_s = cv2.getTrackbarPos("LS", "Tracking")
    l_v = cv2.getTrackbarPos("LV", "Tracking")

    u_h = cv2.getTrackbarPos("UH", "Tracking")
    u_s = cv2.getTrackbarPos("US", "Tracking")
    u_v = cv2.getTrackbarPos("UV", "Tracking")

    lower_threshold = np.array([l_h, l_s, l_v])
    upper_threshold = np.array([u_h, u_s, u_v])

    mask = cv2.inRange(hsv, lower_threshold, upper_threshold)

    # Extract the object
    res = cv2.bitwise_and(frame, frame, mask=mask)

    # Show the image
    cv2.imshow("frame", frame)
    cv2.imshow("mask", mask)
    cv2.imshow("res", res)
    cv2.imshow("HSV", hsv)

    # Wait until a key pressed
    key = cv2.waitKey(1)
    if key == 27:
        break

# Destroy all the windows opened before
cv2.destroyAllWindows()
