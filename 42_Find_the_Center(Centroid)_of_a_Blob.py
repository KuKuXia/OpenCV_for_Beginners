"""
Find the center(centroid) of a blob using moment
Original url:
https://www.learnopencv.com/find-center-of-blob-centroid-using-opencv-cpp-python/

Centroid
    The centroid of a shape is the arithmetic mean (i.e. the average) of all the points in a shape. In the context of image processing and computer vision, each shape is made of pixels, and the centroid is simply the weighted average of all the pixels constituting the shape.

To find the center of the blob, we will perform the following steps:

    1. Convert the Image to grayscale.
    2. Perform Binarization on the Image.
    3. Find the center of the image after calculating the moments.

"""


# Import the packages
import argparse
import cv2
import numpy as np


def single_blob():
    # read image through command line
    img = cv2.imread("./images/circle.png")

    # convert image to grayscale image
    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # convert the grayscale image to binary image
    ret, thresh = cv2.threshold(gray_image, 127, 255, 0)

    # calculate moments of binary image
    M = cv2.moments(thresh)

    # calculate x,y coordinate of center
    cX = int(M["m10"] / M["m00"])
    cY = int(M["m01"] / M["m00"])

    # put text and highlight the center
    cv2.circle(img, (cX, cY), 5, (255, 255, 255), -1)
    cv2.putText(img, "centroid", (cX - 25, cY - 25),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

    # display the image
    cv2.imshow("Single Blob", img)


def multi_blob():
    # read image through command line
    img = cv2.imread("./images/multiple-blob.png")

    # convert the image to grayscale
    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # img = cv2.imread("./images/blob.jpg", 0)

    # convert the grayscale image to binary image
    ret, thresh = cv2.threshold(img, 127, 255, 0)

    # find contour in the binary image
    contours, _ = cv2.findContours(
        thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for c in contours:
        # calculate moments for each contour
        M = cv2.moments(c)
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])

        # calculate x,y coordinate of center
        cv2.circle(img, (cX, cY), 5, (255, 255, 255), -1)
        cv2.putText(img, "centroid", (cX - 25, cY - 25),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

        # display the image
        cv2.imshow("Multi Blob", img)


single_blob()
multi_blob()

# Wait until a key pressed
cv2.waitKey(0)

# Destroy all the windows opened before
cv2.destroyAllWindows()
