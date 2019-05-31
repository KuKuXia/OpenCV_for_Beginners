"""
Pyramid, or pyramid representation, is a type of multi-scale signal representation, in which a signal or an image is subject to repeated smoothing and subsampling. Pyramid representation is a predecessor to scale-space representation and multiresolution analysis.
Gaussian pyramid: subsequent images are weighted down using a Gaussian average (Gaussian blur) and scaled down. Each pixel containing a local average that corresponds to a pixel neighborhood on a lower level of the pyramid.
Laplacian pyramid: A level in Laplacian Pyramid is formed by the difference between that level in Gaussian Pyramid and expanded version of its upper level in Gaussian Pyramid.
More details: https://www.wikiwand.com/en/Pyramid_(image_processing)
"""
import cv2
import numpy as np
img = cv2.imread("./images/lena.jpg")
layer = img.copy()
gaussian_pyramid_list = [layer]

for i in range(6):
    # Decrease the image resolution by 2 times
    layer = cv2.pyrDown(layer)
    print("After the {}th pyramid down, the image shape is: {}".format(i, layer.shape))
    gaussian_pyramid_list.append(layer)
    #cv2.imshow(str(i), layer)

layer = gaussian_pyramid_list[5]
cv2.imshow('upper level Gaussian Pyramid', layer)
laplacian_pyramid_list = [layer]

for i in range(5, 0, -1):
    # Extend the image resolution by 2 times
    gaussian_extended = cv2.pyrUp(gaussian_pyramid_list[i])
    print("After the {}th pyramid up, the image shape is: {}".format(
        5-i, gaussian_extended.shape))

    laplacian = cv2.subtract(gaussian_pyramid_list[i-1], gaussian_extended)
    cv2.imshow(str(i), laplacian)

cv2.imshow("Original image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
