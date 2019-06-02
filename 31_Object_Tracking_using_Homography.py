"""
For some reason, the SURF and SIFT algorithms are protected and not install into the opencv-python package since OpenCV 3.x. They are included in opencv-contrib-python, so in order to run this file, you need run the following command:
pip uninstall opencv-contrib-python
pip uninstall opencv-python
pip install opencv-contrib-python==3.3.0.10
pip install opencv-python==3.4.2.16
"""

import cv2
import numpy as np

img = cv2.imread("./images/object.jpg",
                 cv2.IMREAD_GRAYSCALE)  # object image
img = cv2.resize(img, (int(img.shape[0]/2), int(img.shape[1]/2)))
# cv2.imwrite('green_object.jpg',img)
cap = cv2.VideoCapture(0)

# Features
sift = cv2.xfeatures2d.SIFT_create()
kp_image, desc_image = sift.detectAndCompute(img, None)

# Feature matching
index_params = dict(algorithm=0, trees=5)
search_params = dict()
flann = cv2.FlannBasedMatcher(index_params, search_params)

while(cap.isOpened()):
    _, frame = cap.read()
    grayframe = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # trainimage

    kp_grayframe, desc_grayframe = sift.detectAndCompute(grayframe, None)
    matches = flann.knnMatch(desc_image, desc_grayframe, k=2)

    good_points = []
    for m, n in matches:
        if m.distance < 0.6*n.distance:
            good_points.append(m)

    img_3 = cv2.drawMatches(img, kp_image, grayframe,
                            kp_grayframe, good_points, grayframe)

    # Homograph
    if len(good_points) > 10:
        query_pts = np.float32(
            [kp_image[m.queryIdx].pt for m in good_points]).reshape(-1, 1, 2)
        train_pts = np.float32(
            [kp_grayframe[m.trainIdx].pt for m in good_points]).reshape(-1, 1, 2)

        matrix, mask = cv2.findHomography(
            query_pts, train_pts, cv2.RANSAC, 5.0)
        matches_mask = mask.ravel().tolist()

        # Perspective transform
        h, w = img.shape
        pts = np.float32([[0, 0], [0, h], [w, h], [w, 0]]).reshape(-1, 1, 2)
        dst = cv2.perspectiveTransform(pts, matrix)

        homograph = cv2.polylines(
            frame, [np.int32(dst)], True, (255, 0, 0), 3)

        cv2.imshow("Homography", homograph)
    else:
        cv2.imshow("Homography", frame)

    cv2.imshow("Image", frame)
    cv2.imshow("grayFrame", grayframe)
    cv2.imshow("img3", img_3)

    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
