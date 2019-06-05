"""
Learn RGB channels with trackerbar
"""

# Import the packages
import cv2 as cv
import numpy as np

# Define the trackbar callback function


def nothing(x):
    print(x)


# Create a black image, a window
img = np.zeros((512, 512, 3), np.uint8)
cv.namedWindow('image', cv.WINDOW_NORMAL)

# Create trackbars for color change
cv.createTrackbar('B', 'image', 0, 255, nothing)
cv.createTrackbar('G', 'image', 0, 255, nothing)
cv.createTrackbar('R', 'image', 0, 255, nothing)

# Create switch for ON/OFF functionality
switch = '0 : OFF, 1 : ON'
cv.createTrackbar(switch, 'image', 0, 1, nothing)

while (1):
    # Show the image
    cv.imshow('image', img)

    # Wait 1ms until the ESC button pressed
    k = cv.waitKey(1) & 0xFF
    if k == 27:
        break
    # Get the current positions of trackbars
    b = cv.getTrackbarPos('B', 'image')
    g = cv.getTrackbarPos('G', 'image')
    r = cv.getTrackbarPos('R', 'image')
    s = cv.getTrackbarPos(switch, 'image')

    # Switch the mode: show color or not
    if s == 0:
        img[:] = 0
    else:
        img[:] = [b, g, r]

# Destory all the windows
cv.destroyAllWindows()
