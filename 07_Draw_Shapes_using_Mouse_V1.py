"""
Draw shapes using mouse version one

"""

# Import the packages
import numpy as np
import cv2

# Define the callback function


def click_event(event, x, y, flags, param):
    # Left button down: draw the line
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x, y), 3, (0, 0, 255), -1)
        points.append((x, y))
        if len(points) >= 2:
            cv2.line(img, points[-1], points[-2], (255, 0, 0), 5)
        # Show the image
        cv2.imshow('image', img)

    # Right button down： show the image color of the clicked point (b, g, r)
    if event == cv2.EVENT_RBUTTONDOWN:
        blue = img[x, y, 0]
        green = img[x, y, 1]
        red = img[x, y, 2]
        my_color_Image = np.zeros((200, 200, 3), np.uint8)
        my_color_Image[:] = [blue, green, red]
        cv2.imshow('color', my_color_Image)


# Read the image
img = cv2.imread('./images/lena.jpg')
cv2.imshow('image', img)

# Define the points list
points = []

# Set the callback function
cv2.setMouseCallback('image', click_event)

# Wait until a button pressed
cv2.waitKey(0)

# Destory all the windows opened before
cv2.destroyAllWindows()
