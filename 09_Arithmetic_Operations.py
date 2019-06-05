"""
Arithmetic operation on images
"""

# Import the packages
import cv2
import numpy as np

# Read the image
img1 = cv2.imread("./images/lena.jpg")
H, W, C = img1.shape
# Create a new image with the same shape of img1
img2 = np.zeros((H, W, C), np.uint8)
# Create a white rectangle on img2
img2 = cv2.rectangle(img2, (200, 0), (300, 100), (255, 255, 255), -1)

""" 
There are two methods for image addition, 
    - OpenCV Function: cv2.add(img1, img2) (Recommended)
    - Numpy array: img1 + img2 
Note: 
    - OpenCV addition is a saturated operation: if dtype is np.uint8: 255 + 4 = 255
    - while Numpy addition is a modulo operation. if dtype is np.uint8: 255 + 4 = 4
Check this link for more details:
https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_core/py_image_arithmetics/py_image_arithmetics.html
"""

add_img_numpy = img1 + img2

# Calculates the per-element sum of two arrays or an array and a scalar.
add_img = cv2.add(img1, img2)

"""
Image blending
"""
# Calculates the weighted sum of two arrays.
add_img_weighted = cv2.addWeighted(img1, 0.5, img2, 0.5, 0)


# Bitwise Operations
bitAnd = cv2.bitwise_and(img2, img1)
bitOr = cv2.bitwise_or(img2, img1)
bitXor = cv2.bitwise_xor(img1, img2)
bitNot1 = cv2.bitwise_not(img1)
bitNot2 = cv2.bitwise_not(img2)

# Show the image
cv2.imshow("img1", img1)
cv2.imshow("img2", img2)

cv2.imshow("Added Image using Numpy", add_img_numpy)
cv2.imshow('Added Image', add_img)
cv2.imshow('Added Weighted Image', add_img_weighted)

cv2.imshow('bitAnd', bitAnd)
cv2.imshow('bitOr', bitOr)
cv2.imshow('bitXor', bitXor)
cv2.imshow('bitNot1', bitNot1)
cv2.imshow('bitNot2', bitNot2)

# Wait until a key pressed
cv2.waitKey(0)

# Destroy all the windows opened before
cv2.destroyAllWindows()
