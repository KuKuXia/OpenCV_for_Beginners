"""
Please download the images from:
https://pysource.com/2018/07/27/check-if-a-set-of-images-match-the-original-one-with-opencv-and-python/
"""
import cv2
import numpy as np

original = cv2.imread("./images/original_golden_bridge.jpg")
duplicate = cv2.imread("./images/Golden_Bridge/duplicate.jpg")
original = cv2.resize(original, dsize=None, fx=1/3, fy=1/3)
duplicate = cv2.resize(duplicate, dsize=None, fx=1/3, fy=1/3)

# duplicate = cv2.imread("./images/cartoonized.jpg")
# 1) Check if 2 images are equals
if original.shape == duplicate.shape:
    print("The images have same size and channels")
    difference = cv2.subtract(original, duplicate)
    b, g, r = cv2.split(difference)

    if cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0:
        print("The images are completely Equal")
    else:
        print("The images are different.")
cv2.imshow("Original", original)
cv2.imshow("Duplicate", duplicate)
cv2.waitKey(0)
cv2.destroyAllWindows()
