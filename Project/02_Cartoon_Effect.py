"""
A cartoon has 2 important characteristics:
- Really clear edges
- Homogeneous colours
"""

import cv2
import numpy as np

img = cv2.imread("./images/adventure.jpeg")
img = cv2.resize(img, dsize=None, fx=1/2, fy=1/2)
# 1) Edges
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.medianBlur(gray, 5)
edges = cv2.adaptiveThreshold(
    gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)

# 2) Color
color = cv2.bilateralFilter(img, 9, 300, 300)

# 3) Cartoon
cartoon_or = cv2.bitwise_or(color, color, mask=edges)
cartoon_and = cv2.bitwise_and(color, color, mask=edges)

cv2.imshow("Image", img)
cv2.imshow("Cartoon_or", cartoon_or)
cv2.imshow("Cartoon_and", cartoon_and)
cv2.imshow("color", color)
cv2.imshow("edges", edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
