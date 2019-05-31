"""
Morphological transformations are normally performed on binary images. 

A kernal tells you how to change the value of any given pixel by combining it with different amounts of the nighboring pixels.

"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('./images/smarties.png', cv2.IMREAD_GRAYSCALE)
_, mask = cv2.threshold(img, 220, 255, cv2.THRESH_BINARY_INV)

kernal = np.ones((5, 5), np.uint8)

dilation = cv2.dilate(mask, kernal, iterations=5)
erosion = cv2.erode(mask, kernal, iterations=5)

# Opening: erosion followed by dilation
opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernal)

# Closing: dilation followed by erosion
closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernal)

mg = cv2.morphologyEx(mask, cv2.MORPH_GRADIENT, kernal)
th = cv2.morphologyEx(mask, cv2.MORPH_TOPHAT, kernal)

titles = ['image', 'mask', 'dilation',
          'erosion', 'opening', 'closing', 'mg', 'th']
images = [img, mask, dilation, erosion, opening, closing, mg, th]

for i in range(8):
    plt.subplot(2, 4, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()
