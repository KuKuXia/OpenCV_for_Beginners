"""
Draw rectangle and circle using callback function
"""

# Import the packages
import cv2
import numpy as np

# true if mouse is pressed
drawing = False

# if True, draw rectangle. Press 'm' to toggle to curve
mode = True
ix, iy = -1, -1


# Define the callback function
def draw_circle(event, x, y, flags, param):
    global ix, iy, drawing, mode

    # Set the first point
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y

    # Add the points
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            if mode == True:
                # thickness: -1 fill the shape with the color
                # cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), thickness=2)
                pass
            else:
                cv2.circle(img, (x, y), 5, (0, 0, 255), thickness=-1)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        if mode == True:
            # thickness: -1 fill the shape with the color
            cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), thickness=2)
        else:
            cv2.circle(img, (x, y), 5, (0, 0, 255), thickness=-1)


img = np.zeros((512, 512, 3), np.uint8)

# Create a window to contain the image
cv2.namedWindow('Image')
cv2.setMouseCallback('Image', draw_circle)

while(1):
    # Show the image
    cv2.imshow('Image', img)

    # Wait 1ms until a button pressed
    k = cv2.waitKey(1) & 0xFF

    # Switch the mode: rectangle or circle
    if k == ord('m'):
        mode = not mode
    elif k == 27:
        break

# Destory all the windows opened before
cv2.destroyAllWindows()
