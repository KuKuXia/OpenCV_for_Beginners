"""
Seamless cloning
Original url: 
https://www.learnopencv.com/seamless-cloning-using-opencv-python-cpp/
"""

# Standard imports
import cv2
import numpy as np

# Read images
src = cv2.imread("images/seamless_cloning/airplane.jpg")
dst = cv2.imread("images/seamless_cloning/sky.jpg")

# Create a rough mask around the airplane.
src_mask = np.zeros(src.shape, src.dtype)
poly = np.array([[4, 80], [30, 54], [151, 63], [254, 37], [
                298, 90], [272, 134], [43, 122]], np.int32)
cv2.fillPoly(src_mask, [poly], (255, 255, 255))

# This is where the CENTER of the airplane will be placed
center = (800, 100)

# Clone seamlessly.
output_normal = cv2.seamlessClone(src, dst, src_mask, center, cv2.NORMAL_CLONE)
output_mixed = cv2.seamlessClone(src, dst, src_mask, center, cv2.MIXED_CLONE)

# Save result
cv2.imwrite(
    "images/seamless_cloning/opencv-seamless-cloning-normal-example.jpg", output_normal)
cv2.imwrite(
    "images/seamless_cloning/opencv-seamless-cloning-mixed-example.jpg", output_mixed)

# Show the image
cv2.imshow("Seamless Cloning Normal", output_normal)
cv2.imshow("Seamless Cloning Mixed", output_mixed)

# Wait until a key pressed
cv2.waitKey(0)

# Destroy all the windows opened before
cv2.destroyAllWindows()
