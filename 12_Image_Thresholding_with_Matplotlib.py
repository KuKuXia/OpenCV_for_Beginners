"""
Image thresholding with matplotlib
Please check out the 12_Image_Thresholding.py firstly.

Color image loaded by OpenCV is in BGR mode. But Matplotlib displays in RGB mode. 
"""

# Import the packages
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

# Read the image
img = cv.imread('./images/gradient.png', 0)

#  Different thresholding methods_
_, th1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY)
_, th2 = cv.threshold(img, 127, 255, cv.THRESH_BINARY_INV)
_, th3 = cv.threshold(img, 127, 255, cv.THRESH_TRUNC)
_, th4 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO)
_, th5 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO_INV)

titles = ['Original Image', 'BINARY',
          'BINARY_INV', 'TRUNC', 'TOZERO', 'TOZERO_INV']
images = [img, th1, th2, th3, th4, th5]

# Using matplotlib to plot the images
for i in range(6):
    plt.subplot(2, 3, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

# Show the image
plt.show()
