# To show the difference between normal_clone and mixed_clone, use the images bellow
import numpy as np
import cv2

# Read images : src image will be cloned into dst
im = cv2.imread("images/seamless_cloning/wood-texture.jpg")
obj = cv2.imread("images/seamless_cloning/iloveyouticket.jpg")

# Create an all white mask
mask = 255 * np.ones(obj.shape, obj.dtype)

# The location of the center of the src in the dst
width, height, channels = im.shape
center = (height//2, width//2)

# Seamlessly clone src into dst and put the results in output
normal_clone = cv2.seamlessClone(obj, im, mask, center, cv2.NORMAL_CLONE)
mixed_clone = cv2.seamlessClone(obj, im, mask, center, cv2.MIXED_CLONE)

# Write results
cv2.imwrite("images/opencv-normal-clone-example.jpg", normal_clone)
cv2.imwrite("images/opencv-mixed-clone-example.jpg", mixed_clone)
# Show the image
cv2.imshow("Seamless Cloning Normal", normal_clone)
cv2.imshow("Seamless Cloning Mixed", mixed_clone)

# Wait until a key pressed
cv2.waitKey(0)

# Destroy all the windows opened before
cv2.destroyAllWindows()
