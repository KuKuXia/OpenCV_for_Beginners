import cv2
import numpy as np

# img = cv2.imread('./images/sudoku.png', 0)
img = cv2.imread('./images/book_page.jpg', 0)
_, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

th2 = cv2.adaptiveThreshold(
    img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 10)
th3 = cv2.adaptiveThreshold(
    img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 10)

# Smoothing
average_smoothed_1 = cv2.blur(th2, (5, 5))
average_smoothed_2 = cv2.blur(th3, (5, 5))
median_smoothed_1 = cv2.medianBlur(th2, 5)
median_smoothed_2 = cv2.medianBlur(th3, 5)


cv2.imshow("Image", img)
cv2.imshow("THRESH_BINARY", th1)
cv2.imshow("ADAPTIVE_THRESH_MEAN_C", th2)
cv2.imshow("ADAPTIVE_THRESH_GAUSSIAN_C", th3)
cv2.imshow('ADAPTIVE_THRESH_MEAN_C_Median_Smoothed', median_smoothed_1)
cv2.imshow('ADAPTIVE_THRESH_GAUSSIAN_Median_Smoothed', median_smoothed_2)
cv2.imshow('ADAPTIVE_THRESH_MEAN_C_Average_Smoothed', average_smoothed_1)
cv2.imshow('ADAPTIVE_THRESH_GAUSSIAN_C_Average_Smoothed', average_smoothed_2)
cv2.waitKey(0)
cv2.destroyAllWindows()
