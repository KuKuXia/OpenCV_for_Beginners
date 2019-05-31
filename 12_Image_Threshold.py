import cv2
import numpy as np

img = cv2.imread('./images/gradient.png', 0)

# pixel value lower than 127 -> 0 black, higher than 127 -> 255 white
_, th1 = cv2.threshold(img, 127, 200, cv2.THRESH_BINARY)

# pixel value lower than 127 -> 255 white, higher than 127 -> 0 black
_, th2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)

# pixel value lower than 127 remain the same, higher than 127 -> 127
_, th3 = cv2.threshold(img, 127, 255,
                       cv2.THRESH_TRUNC)

# pixel value lower than 127 -> 0 black, higher than 127 -> remain the same
_, th4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)

# pixel value lower than 127 remain the same, higher than 127 -> 0 black
_, th5 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)


cv2.imshow('Image', img)
cv2.imshow('th1', th1)
cv2.imshow('th2', th2)
cv2.imshow('th3', th3)
cv2.imshow('th4', th4)
cv2.imshow('th5', th5)


cv2.waitKey(0)
cv2.destroyAllWindows()
