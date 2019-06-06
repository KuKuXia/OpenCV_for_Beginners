"""
Using mouse callback to determine four source points, then get the homography matrix and apply it to source image.
Original url:
https://www.learnopencv.com/homography-examples-using-opencv-python-c/
"""

import cv2
import numpy as np
from utils import get_four_points


if __name__ == '__main__':

    # Read in the image.
    im_src = cv2.imread("./images/book1.jpg")

    # Destination image
    size = (300, 400, 3)

    im_dst = np.zeros(size, np.uint8)

    # Set the destination points
    pts_dst = np.array(
        [
            [0, 0],
            [size[0] - 1, 0],
            [size[0] - 1, size[1] - 1],
            [0, size[1] - 1]
        ], dtype=float
    )

    print('''
        Click on the four corners of the book -- top left first and
        bottom left last -- and then hit ENTER
        ''')

    # Show image and wait for 4 clicks.
    cv2.imshow("Image", im_src)
    pts_src = get_four_points(im_src)

    # Calculate the homography
    h, status = cv2.findHomography(pts_src, pts_dst)

    # Warp source image to destination
    im_dst = cv2.warpPerspective(im_src, h, size[0:2])

    # Show the image
    cv2.imshow("Image Wrapped", im_dst)

    # Wait until a key pressed
    cv2.waitKey(0)

    # Destroy all the windows opened before
    cv2.destroyAllWindows()
