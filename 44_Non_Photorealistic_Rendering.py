"""
Non-Photorealistic Rendering using domain transform for edge-aware filtering

Copyright 2015 by Satya Mallick <spmallick@gmail.com>

Original tutorial url:
https://www.learnopencv.com/non-photorealistic-rendering-using-opencv-python-c/

Original paper url: 
http://www.inf.ufrgs.br/~eslgastal/DomainTransform/Gastal_Oliveira_SIGGRAPH2011_Domain_Transform.pdf

Four functions:
    - Edge Preserving Filter (edgePreservingFilter) 
    - Detail Enhancing Filter (detailEnhance) 
    - Pencil Sketch Filter (pencilSketch)
    - Stylization Filter (stylization)
"""

# Import the packages
import cv2

# Read the image
im = cv2.imread("./images/non-photorealistic_rendering/cow.jpg")

# Edge preserving filter with two different flags.
image_out = cv2.edgePreservingFilter(im, flags=cv2.RECURS_FILTER)
cv2.imwrite(
    "./images/non-photorealistic_rendering/edge-preserving-recursive-filter-example.jpg", image_out)

image_out = cv2.edgePreservingFilter(im, flags=cv2.NORMCONV_FILTER)
cv2.imwrite(
    "./images/non-photorealistic_rendering/edge-preserving-normalized-convolution-filter-example.jpg", image_out)

# Detail enhance filter
image_out = cv2.detailEnhance(im)
cv2.imwrite(
    "./images/non-photorealistic_rendering/detail-enhance-example.jpg", image_out)

# Pencil sketch filter
image_out_gray, image_out = cv2.pencilSketch(
    im, sigma_s=60, sigma_r=0.07, shade_factor=0.05)
cv2.imwrite(
    "./images/non-photorealistic_rendering/pencil-sketch-example.jpg", image_out_gray)
cv2.imwrite(
    "./images/non-photorealistic_rendering/pencil-sketch-color-example.jpg", image_out)

# Stylization filter
cv2.stylization(im, image_out)
cv2.imwrite(
    "./images/non-photorealistic_rendering/stylization-example.jpg", image_out)
