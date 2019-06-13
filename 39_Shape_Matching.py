"""
Shape matching using Hu moments
Original url:
https://www.learnopencv.com/shape-matching-using-hu-moments-c-python/

1. Image moments are a weighted average of image pixel intensities.
2. Image moments capture information about the shape of a blob in a binary image because they contain information about the intensity I(x,y), as well as position x and y of the pixels.
3.Central moments are translations invariant, and normalized central moments are both translation and scale invariant.
4.Hu Moments ( or rather Hu moment invariants ) are a set of 7 numbers calculated using central moments that are invariant to image transformations. The first 6 moments have been proved to be invariant to translation, scale, and rotation, and reflection. While the 7th moment’s sign changes for image reflection.

"""

# Import the packages
import cv2
import sys
import os
from math import copysign, log10


def show_hu_moments():
    showLogTransfromedHuMoments = True

    filename = os.listdir('./images/hu_moments/')
    for i in range(0, len(filename)):
        # Read the image
        image = cv2.imread('./images/hu_moments/' +
                           filename[i], cv2.IMREAD_GRAYSCALE)
        print(image.shape)
        # Threshold image
        _, im = cv2.threshold(image, 128, 255, cv2.THRESH_BINARY)

        # Calculate Moments
        moment = cv2.moments(image)

        # Calculate Hu Moments
        hu_moments = cv2.HuMoments(moment)

        # Print Hu Moments
        print("{}: ".format(filename[i], end=''))

        for i in range(0, 7):
            if showLogTransfromedHuMoments:
                # Log transform Hu Moments to make
                # squash the range
                print("{:.5f}".format(-1*copysign(1.0,
                                                  hu_moments[i])*log10(abs(hu_moments[i]))),
                      end=' ')
            else:
                # Hu Moments without log transform
                print("{:.5f}".format(hu_moments[i]), end='')
        print()


def shape_matcher():
    im1 = cv2.imread("images/hu_moments/S0.png", cv2.IMREAD_GRAYSCALE)
    im2 = cv2.imread("images/hu_moments/K0.png", cv2.IMREAD_GRAYSCALE)
    im3 = cv2.imread("images/hu_moments/S4.png", cv2.IMREAD_GRAYSCALE)

    m1 = cv2.matchShapes(im1, im1, cv2.CONTOURS_MATCH_I2, 0)
    m2 = cv2.matchShapes(im1, im2, cv2.CONTOURS_MATCH_I2, 0)
    m3 = cv2.matchShapes(im1, im3, cv2.CONTOURS_MATCH_I2, 0)

    print("Shape Distances Between \n-------------------------")

    print("S0.png and S0.png : {}".format(m1))
    print("S0.png and K0.png : {}".format(m2))
    print("S0.png and S4.png : {}".format(m3))


show_hu_moments()
shape_matcher()
