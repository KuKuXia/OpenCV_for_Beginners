"""
The Canny edge detector is an edge detection operator that uses a multi-stage algorithm to detect a wide range of edges in images. It was developed by John F. Canny in 1986.

The Process of Canny edge detection algorithm can be broken down to 5 different steps:
- Apply Gaussian filter to smooth the image in order to remove the noise
- Find the intensity gradients of the image
- Apply non-maximum suppression to get rid of spurious response to edge detection
- Apply double threshold to determine potential edges
- Track edge by hysteresis: Finalize the detection of edges by suppressing all the other edges that are weak and not connected to strong edges.

"""
import cv2
import numpy as np
from matplotlib import pyplot as plt


def nothing(x):
    pass


# Create a black image, a window
cv2.namedWindow('image')

cv2.createTrackbar('Lower Threshold', 'image', 10, 254, nothing)
cv2.createTrackbar('Higher Threshold', 'image', 10, 254, nothing)

img = cv2.imread("./images/lena.jpg")

while (1):
    lower_threshold = cv2.getTrackbarPos('Lower Threshold', 'image')
    higher_threshold = cv2.getTrackbarPos('Higher Threshold', 'image')

    canny = cv2.Canny(img, lower_threshold, higher_threshold)

    titles = ['image', 'canny']
    images = [img, canny]

    cv2.imshow('Original_image', images[0])
    cv2.imshow('image', images[1])

    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
