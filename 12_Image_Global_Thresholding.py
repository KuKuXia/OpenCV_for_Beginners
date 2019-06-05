"""
Image thresholding
If pixel value is greater than a threshold value, it is assigned one value (may be white), else it is assigned another value (may be black). 

cv2.threshold(img, threshold, maxVal, threshold_type):
    threshold_type:
        - cv2.THRESH_BINARY
        - cv2.THRESH_BINARY_INV
        - cv2.THRESH_TRUNC
        - cv2.THRESH_TOZERO
        - cv2.THRESH_TOZERO_INV
"""

# Import the packages
import cv2
import numpy as np

# Read the image
img = cv2.imread('./images/gradient.png', cv2.IMREAD_GRAYSCALE)


# Define the callback function
def nothing(x):
    print(x)


# Create a window to contain the image
cv2.namedWindow("Control", cv2.WINDOW_NORMAL)

# Create a button to determine the threshold value
cv2.createTrackbar('Threshold Value', 'Control', 128, 255, nothing)

while True:
    # Get the current positions of trackerbar
    threshold = cv2.getTrackbarPos('Threshold Value', 'Control')

    # pixel value lower than threshold -> 0 black, higher than threshold -> 255 white
    _, th1 = cv2.threshold(img, threshold, 255, cv2.THRESH_BINARY)

    # pixel value lower than threshold -> 255 white, higher than threshold -> 0 black
    _, th2 = cv2.threshold(img, threshold, 255, cv2.THRESH_BINARY_INV)

    # pixel value lower than threshold remain the same, higher than threshold -> threshold
    _, th3 = cv2.threshold(img, threshold, 255, cv2.THRESH_TRUNC)

    # pixel value lower than threshold -> 0 black, higher than threshold -> remain the same
    _, th4 = cv2.threshold(img, threshold, 255, cv2.THRESH_TOZERO)

    # pixel value lower than threshold remain the same, higher than threshold -> 0 black
    _, th5 = cv2.threshold(img, threshold, 255, cv2.THRESH_TOZERO_INV)

    cv2.imshow('Image', img)
    cv2.imshow('THRESH_BINARY', th1)
    cv2.imshow('THRESH_BINARY_INV', th2)
    cv2.imshow('THRESH_TRUNC', th3)
    cv2.imshow('THRESH_TOZERO', th4)
    cv2.imshow('THRESH_TOZERO_INV', th5)

    # Wait 2 ms until press the key, can't be 0
    k = cv2.waitKey(2) & 0xFF
    if k == 27:
        break

# Destroy all the windows opened before
cv2.destroyAllWindows()
