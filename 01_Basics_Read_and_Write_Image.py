"""
Read and write image using OpenCV

- cv2.imread("imageName", flag): Reade the image
    Color image loaded by OpenCV is in BGR mode
    flag:
        - cv2.IMREAD_COLOR : Loads a color image. Any transparency of image will be neglected. It is the default flag.
        - cv2.IMREAD_GRAYSCALE : Loads image in grayscale mode
        - cv2.IMREAD_UNCHANGED : Loads image as such including alpha channel
    Instead of these three flags, you can simply pass integers 1, 0 or -1 respectively.
- cv2.imshow("windowName", image): Show the image
    The window automatically fits to the image size
"""

# Import the package
import cv2

# Create a window to contain the image
cv2.namedWindow("Image", cv2.WINDOW_NORMAL)

# Read the image
img = cv2.imread("./images/lena.jpg", 1)

# Show the image
cv2.imshow('Image', img)

# Wait until a key pressed
k = cv2.waitKey(0) & 0xFF
print(k)

# If button 's' pressed, save the image
if k == ord('s'):
    cv2.imwrite('lena_copy.png', img)

# Destory all the windows opened before
cv2.destroyAllWindows()
