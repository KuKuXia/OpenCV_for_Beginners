"""
Basic properties and operations on images
    - Access pixel values and modify them
    - Access image properties
    - Setting Region of Image (ROI)
    - Splitting and Merging images
"""
# Import the packages
import numpy as np
import cv2
import matplotlib.pyplot as plt

# Read the image
img = cv2.imread('./images/messi5.jpg')
img1 = cv2.imread('./images/opencv-logo.png')

# img.shape returns a tuple of number of rows, columns, and channels
print("Shape is: ", img.shape)

# img.size returns Total number of pixels is accessed
print("Size is: ", img.size)

# img.dtype returns Image datatype is obtained
print("Data type is: ", img.dtype)

# Accessing B, G, R channel values:
b = img[::, 0]
g = img[::, 1]
r = img[::, 2]

# Spliting and merging channels
# cv2.split(img): It's a costly operation (in terms of time), so only use it if necessary. Numpy indexing is much more efficient and should be used if possible.
b, g, r = cv2.split(img)

# cv2.merge((b, g, r)) - The number of channels will be the total number of channels in the matrix array
img = cv2.merge((b, g, r))

# Region of Interest(ROI), copy the ball to anther region
ball = img[280:340, 330:390]
img[273:333, 100:160] = ball
img[73:133, 100:160] = ball

# Better pixel accessing and editing method
# Accessing RED value
print("The pixel value of point: (10,10,2) is ", img.item(10, 10, 2))

# Modifying RED value
img.itemset((10, 10, 2), 100)
print("After modifying the pixel value of the point (10,10, 2), the value is:",
      img.item(10, 10, 2))


# cv2.resize - resize the image
img = cv2.resize(img, (512, 512))
img1 = cv2.resize(img1, (512, 512))
print("After resize the shape of img is: ", img.shape)

# Change the image color space from BGR -> RGB
rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Show the RGB image using OpenCV
cv2.imshow("RGB Image Shown in BGR mode", rgb_img)

# Show other image
cv2.imshow('Messi', img)
cv2.imshow('OpenCV Logo', img1)

# Wait until a key pressed
cv2.waitKey(0)

# Destroy all the windows opened before
cv2.destroyAllWindows()

# Making borders of the image
BLUE = [255, 0, 0]
# Matplotlib use RGB channels, so need to change the color space: BGR -> RGB
img1 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
replicate = cv2.copyMakeBorder(img1, 10, 10, 10, 10, cv2.BORDER_REPLICATE)
reflect = cv2.copyMakeBorder(img1, 10, 10, 10, 10, cv2.BORDER_REFLECT)
reflect101 = cv2.copyMakeBorder(img1, 10, 10, 10, 10, cv2.BORDER_REFLECT_101)
wrap = cv2.copyMakeBorder(img1, 10, 10, 10, 10, cv2.BORDER_WRAP)
constant = cv2.copyMakeBorder(
    img1, 10, 10, 10, 10, cv2.BORDER_CONSTANT, value=BLUE)

plt.subplot(231), plt.imshow(img1, 'gray'), plt.title('ORIGINAL')
plt.subplot(232), plt.imshow(replicate, 'gray'), plt.title('REPLICATE')
plt.subplot(233), plt.imshow(reflect, 'gray'), plt.title('REFLECT')
plt.subplot(234), plt.imshow(reflect101, 'gray'), plt.title('REFLECT_101')
plt.subplot(235), plt.imshow(wrap, 'gray'), plt.title('WRAP')
plt.subplot(236), plt.imshow(constant, 'gray'), plt.title('CONSTANT')

# Note: This will block the program
plt.show()
