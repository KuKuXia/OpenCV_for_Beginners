import cv2
import numpy as np

cap = cv2.VideoCapture("./video/highway.mp4")

"""
- History: is the number of the last frame that are taken into consideretion (by default 120).
- Threshold: is the value used when computing the difference to extract the background. A lower threshold will find more differences with the advantage of a more noisy image.
- Detectshadows: is a function of the algorythm that can remove the shadows if enabled.
"""
subtractor = cv2.createBackgroundSubtractorMOG2(
    history=100, varThreshold=10, detectShadows=True)

while(cap.isOpened()):
    ret, frame = cap.read()
    if not ret:
        cap = cv2.VideoCapture("./video/highway.mp4")
        continue
    mask = subtractor.apply(frame)

    mask = cv2.GaussianBlur(mask, (5, 5), 0)

    cv2.imshow("Frame", frame)
    cv2.imshow("mask", mask)

    key = cv2.waitKey(30)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
