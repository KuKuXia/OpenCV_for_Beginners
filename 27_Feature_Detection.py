"""
For some reason, the SURF and SIFT algorithms are protected and not install into the opencv-python package since OpenCV 3.x. They are included in opencv-contrib-python, so in order to run this file, you need run the following command:
pip uninstall opencv-contrib-python
pip uninstall opencv-python
pip install opencv-contrib-python==3.3.0.10
pip install opencv-python==3.4.2.16
"""

import cv2
import numpy as np
img = cv2.imread("./images/the_book_thief.jpg", cv2.IMREAD_GRAYSCALE)

sift = cv2.xfeatures2d.SIFT_create()
surf = cv2.xfeatures2d.SURF_create()
orb = cv2.ORB_create(nfeatures=1500)

keypoints_sift, descriptors = sift.detectAndCompute(img, None)
keypoints_surf, descriptors = surf.detectAndCompute(img, None)
keypoints_orb, descriptors = orb.detectAndCompute(img, None)

sift_img = cv2.drawKeypoints(img, keypoints_sift, None)
surf_img = cv2.drawKeypoints(img, keypoints_surf, None)
orb_img = cv2.drawKeypoints(img, keypoints_orb, None)

cv2.imshow("SIFT Image", sift_img)
cv2.imshow("SURF Image", surf_img)
cv2.imshow("ORB Image", orb_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
