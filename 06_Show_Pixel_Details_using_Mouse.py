"""
Show pixel details using mouse by callback function
"""

# Import the packages
import numpy as np
import cv2

# Print the available events
events = [i for i in dir(cv2) if 'EVENT' in i]
print(events)

# Callback functions


def click_event(event, x, y, flags, param):
    # Left button down: show the cooridnates of the clicked points (x, y)
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x, ', ', y)
        font = cv2.FONT_HERSHEY_SIMPLEX
        strXY = str(x) + ', ' + str(y)
        cv2.putText(img, strXY, (x, y), font, .5, (255, 255, 0), 2)
        cv2.imshow('image', img)

    # Right button down: show the image channels of the clicked points (b, g, r)
    if event == cv2.EVENT_RBUTTONDOWN:
        blue = img[y, x, 0]
        green = img[y, x, 1]
        red = img[y, x, 2]
        font = cv2.FONT_HERSHEY_SIMPLEX
        strBGR = str(blue) + ', ' + str(green) + ', ' + str(red)
        cv2.putText(img, strBGR, (x, y), font, .5, (0, 255, 255), 2)
        cv2.imshow('image', img)


# Read the image
img = cv2.imread('./images/lena.jpg')

# Show the image
cv2.imshow('image', img)

# Set the callback function
cv2.setMouseCallback('image', click_event)

# Wait until a button pressed
cv2.waitKey(0)
cv2.destroyAllWindows()
