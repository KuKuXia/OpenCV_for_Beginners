"""
Adaptive thresholding
In the last file, we used a global value as fthreshold value. But it may not be good in all the conditions where image has different lighting conditions in different areas. In that case, we go for adaptive thresholding. In this, the algorithm calculate the threshold for a small regions of the image. So we get different thresholds for different regions of the same image and it gives us better results for images with varying illumination.

cv2.adaptiveThreshold(​img, maxValue, adaptiveMethod, thresholdType, blockSize, C, dst)

Adaptive Method - It decides how thresholding value is calculated.
    - cv2.ADAPTIVE_THRESH_MEAN_C : threshold value is the mean of neighborhood area.
    - cv2.ADAPTIVE_THRESH_GAUSSIAN_C : threshold value is the weighted sum of neighborhood values where weights are a gaussian window.

Block Size - It decides the size of neighbourhood area.

C - It is just a constant which is subtracted from the mean or weighted mean calculated.
"""

# Import the packages
import cv2
import numpy as np

# Read the image
img = cv2.imread('./images/sudoku.png', 0)
# img = cv2.imread('./images/book_page.jpg', 0)

# Simple threshold method
_, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

# Adaptive threshold method
th2 = cv2.adaptiveThreshold(
    img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 10)
th3 = cv2.adaptiveThreshold(
    img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 10)

# Smoothing
average_smoothed_1 = cv2.blur(th2, (5, 5))
average_smoothed_2 = cv2.blur(th3, (5, 5))
median_smoothed_1 = cv2.medianBlur(th2, 5)
median_smoothed_2 = cv2.medianBlur(th3, 5)

# Show the image
cv2.imshow("Image", img)
cv2.imshow("THRESH_BINARY", th1)
cv2.imshow("ADAPTIVE_THRESH_MEAN_C", th2)
cv2.imshow("ADAPTIVE_THRESH_GAUSSIAN_C", th3)
cv2.imshow('ADAPTIVE_THRESH_MEAN_C_Median_Smoothed', median_smoothed_1)
cv2.imshow('ADAPTIVE_THRESH_GAUSSIAN_Median_Smoothed', median_smoothed_2)
cv2.imshow('ADAPTIVE_THRESH_MEAN_C_Average_Smoothed', average_smoothed_1)
cv2.imshow('ADAPTIVE_THRESH_GAUSSIAN_C_Average_Smoothed', average_smoothed_2)

# Wait until a key pressed
cv2.waitKey(0)

# Destroy all the windows opened before
cv2.destroyAllWindows()
