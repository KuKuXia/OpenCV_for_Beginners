"""
For some reason, the SURF and SIFT algorithms are protected and not install into the opencv-python package since OpenCV 3.x. They are included in opencv-contrib-python, so in order to run this file, you need run the following command:
pip uninstall opencv-contrib-python
pip uninstall opencv-python
pip install opencv-contrib-python==3.3.0.10
pip install opencv-python==3.4.2.16
"""

import cv2
import numpy as np

img1 = cv2.imread("./images/the_book_thief.jpg", cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread("./images/me_holding_book.jpg", cv2.IMREAD_GRAYSCALE)

# ORB Detector
orb = cv2.ORB_create()
kp1, des1 = orb.detectAndCompute(img1, None)
kp2, des2 = orb.detectAndCompute(img2, None)

# Brute Force Matching
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
matches = bf.match(des1, des2)
matches = sorted(matches, key=lambda x: x.distance)
matching_result = cv2.drawMatches(
    img1, kp1, img2, kp2, matches[:50], None, flags=2)

cv2.imshow("Img1", img1)
cv2.imshow("Img2", img2)
cv2.imshow("Matching result", matching_result)
cv2.waitKey(0)
cv2.destroyAllWindows()
