"""
Trackerbar with switch and text
"""

# Import the packages
import numpy as np
import cv2 as cv


# Define the callback function
def nothing(x):
    print(x)


# Create a window to contain the image
cv.namedWindow('image', cv.WINDOW_NORMAL)
cv.createTrackbar('CP', 'image', 10, 400, nothing)

# Create the switch button
switch = 'color/gray'
cv.createTrackbar(switch, 'image', 0, 1, nothing)

while (1):
    # Read the image
    img = cv.imread('./images/lena.jpg')

    # Get the current positions of trackerbar
    pos = cv.getTrackbarPos('CP', 'image')

    # Add the text to the image
    font = cv.FONT_HERSHEY_SIMPLEX
    cv.putText(img, str(pos), (50, 150), font, 5, (0, 0, 255), 5)

    # Wait until a key pressed
    k = cv.waitKey(1) & 0xFF
    if k == 27:
        break

    # Get the current positions of trackerbar
    gray_bit = cv.getTrackbarPos(switch, 'image')

    # Switch the mode according to the button value
    if gray_bit == 0:
        pass
    else:
        img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    # Show the image
    img = cv.imshow('image', img)

# Destroy all the windows opened before
cv.destroyAllWindows()
