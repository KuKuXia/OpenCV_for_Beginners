"""
Filling holes in an image
Original url:
https://www.learnopencv.com/filling-holes-in-an-image-using-opencv-python-c/
"""

# Import the packages
import cv2
import numpy as np


# Read the image
image_in = cv2.imread("./images/nickel.jpg", cv2.IMREAD_GRAYSCALE)

# Threshold
# Set values equal to or above 220 to 0
# Set values below 220 to 255

_, image_thresholded = cv2.threshold(image_in, 220, 255, cv2.THRESH_BINARY_INV)

# Copy the threshold image
image_floodfill = image_thresholded.copy()

# Mask used to flood filling
# Notice the size needs to be 2 pixels than the image
h, w = image_thresholded.shape[:2]
mask = np.zeros((h+2, w+2), np.uint8)

# Floodfill from point (0,0)
cv2.floodFill(image_floodfill, mask, (0, 0), 255)

# Invert floodfilled image
image_floodfill_inv = cv2.bitwise_not(image_floodfill)

# Combine the two images to get the foreground
image_out = cv2.bitwise_or(image_thresholded, image_floodfill_inv)

# Show the image
cv2.imshow("Thresholded Image", image_thresholded)
cv2.imshow("Floodfilled Image", image_floodfill)
cv2.imshow("Inverted Floodfilled Image", image_floodfill_inv)
cv2.imshow("Foreground", image_out)

# Wait until a key pressed
cv2.waitKey(0)

# Destroy all the windows opened before
cv2.destroyAllWindows()
