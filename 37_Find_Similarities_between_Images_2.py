"""
For some reason, the SURF and SIFT algorithms are protected and not install into the opencv-python package since OpenCV 3.x. They are included in opencv-contrib-python, so in order to run this file, you need run the following command:
pip uninstall opencv-contrib-python
pip uninstall opencv-python
pip install opencv-contrib-python==3.3.0.10
pip install opencv-python==3.4.2.16

Please download the images from:
https: // pysource.com/2018/07/27/check-if-a-set-of-images-match-the-original-one-with-opencv-and-python/
"""

import cv2
import numpy as np
import glob

original = cv2.imread(
    "./images/original_golden_bridge.jpg")
# Sift and Flann
original = cv2.resize(original, dsize=None, fx=1/3, fy=1/3)

sift = cv2.xfeatures2d.SIFT_create()
kp_1, desc_1 = sift.detectAndCompute(original, None)
index_params = dict(algorithm=0, trees=15)
search_params = dict()
flann = cv2.FlannBasedMatcher(index_params, search_params)

# Load all the images
all_images_to_compare = []
titles = []
for f in glob.iglob("./images/Golden_Bridge/*.jpg"):
    image = cv2.imread(f)
    titles.append(f)
    all_images_to_compare.append(image)

for image_to_compare, title in zip(all_images_to_compare, titles):
    image_to_compare = cv2.resize(
        image_to_compare, dsize=None, fx=1 / 3, fy=1 / 3)

    # 1) Check if 2 images are equals
    if original.shape == image_to_compare.shape:
        print("The images have same size and channels")
        difference = cv2.subtract(original, image_to_compare)
        b, g, r = cv2.split(difference)
        if cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0:
            print("Similarity: 100% (equal size and channels)")
            continue

    # 2) Check for similarities between the 2 images
    kp_2, desc_2 = sift.detectAndCompute(image_to_compare, None)
    matches = flann.knnMatch(desc_1, desc_2, k=2)
    good_points = []
    for m, n in matches:
        if m.distance < 0.7*n.distance:
            good_points.append(m)
    number_keypoints = 0

    if len(kp_1) >= len(kp_2):
        number_keypoints = len(kp_1)
    else:
        number_keypoints = len(kp_2)

    print("Title: " + title)
    percentage_similarity = len(good_points) / number_keypoints * 100
    print("Similarity: {:.3f} \n".format(percentage_similarity))

    result = cv2.drawMatches(
        original, kp_1, image_to_compare, kp_2, good_points, None)

    cv2.imshow(
        title+" Similarity: {:.3f}".format(percentage_similarity), result)
cv2.waitKey(0)
cv2.destroyAllWindows()
