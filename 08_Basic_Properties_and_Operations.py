import numpy as np
import cv2
img = cv2.imread('./messi5.jpg')
img2 = cv2.imread('./opencv-logo.png')
# img.shape returns a tuple of number of rows, columns, and channels
print("Shape is: ", img.shape)

# img.size returns Total number of pixels is accessed
print("Size is: ", img.size)

# img.dtype returns Image datatype is obtained
print("Data type is: ", img.dtype)

# Spliting and merging channels
# cv2.split(img) - output vector of arrays the arrays themselves are reallocated, if needed.
b, g, r = cv2.split(img)

# cv2.merge((b, g, r)) - The number of channels will be the total number of channels in the matrix array.
img = cv2.merge((b, g, r))

# Y,X
ball = img[280:340, 330:390]
img[273:333, 100:160] = ball
img[73:133, 100:160] = ball

# cv2.resize - resize the image
img = cv2.resize(img, (512, 512))
img2 = cv2.resize(img2, (512, 512))
print("After resize the shape of img is: ", img.shape)

# dst = cv2.add(img, img2) - Calculates the per-element sum of two arrays or an array and a scalar.
add_img = cv2.add(img2, img)

# dst = cv2.addWeighted(img, .2, img2, .8, 0) - Calculates the weighted sum of two arrays.
add_img_weighted = cv2.addWeighted(img, 0.5, img2, 0.5, 0)

cv2.imshow('Messi', img)
cv2.imshow('OpenCV Logo', img2)
cv2.imshow('Added Image', add_img)
cv2.imshow('Added Weighted Image', add_img_weighted)
cv2.waitKey(0)
cv2.destroyAllWindows()
