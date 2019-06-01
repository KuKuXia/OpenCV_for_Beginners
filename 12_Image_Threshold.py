import cv2
import numpy as np

img = cv2.imread('./images/gradient.png', cv2.IMREAD_GRAYSCALE)


def nothing(x):
    print(x)

cv2.namedWindow("Control", cv2.WINDOW_NORMAL)
cv2.createTrackbar('Threshold Value', 'Control', 128, 255, nothing) 
    
while True:

    threshold = cv2.getTrackbarPos('Threshold Value', 'Control')
    # pixel value lower than threshold -> 0 black, higher than threshold -> 255 white
    _, th1 = cv2.threshold(img, threshold, 255, cv2.THRESH_BINARY)

    # pixel value lower than threshold -> 255 white, higher than threshold -> 0 black
    _, th2 = cv2.threshold(img, threshold, 255, cv2.THRESH_BINARY_INV)

    # pixel value lower than threshold remain the same, higher than threshold -> threshold
    _, th3 = cv2.threshold(img, threshold, 255,
                           cv2.THRESH_TRUNC)

    # pixel value lower than threshold -> 0 black, higher than threshold -> remain the same
    _, th4 = cv2.threshold(img, threshold, 255, cv2.THRESH_TOZERO)

    # pixel value lower than threshold remain the same, higher than threshold -> 0 black
    _, th5 = cv2.threshold(img, threshold, 255, cv2.THRESH_TOZERO_INV)

    cv2.imshow('Image', img)
    cv2.imshow('th1', th1)
    cv2.imshow('th2', th2)
    cv2.imshow('th3', th3)
    cv2.imshow('th4', th4)
    cv2.imshow('th5', th5)

    # Wait 2 ms until press the key, can't be 0 
    k = cv2.waitKey(2) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
