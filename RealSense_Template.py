"""
RealSense Template

"""

# Import the packages
import cv2
import numpy as np
import pyrealsense2 as rs

from realsense_opencv import DEVICE_ONE, DEVICE_TWO, Realsense

# Create a window to contain the image
cv2.namedWindow("Video", cv2.WINDOW_NORMAL)

# Register the camera
camera_num = 1
camera = Realsense(camera_num=camera_num, device_id=[
    DEVICE_ONE, DEVICE_TWO], color_resolution=[1280, 720], depth_resolution=[1280, 720])

try:
    while True:
        # Read the image
        color_images, depth_images, depth_colormaps = camera.get_images()

        # Choose the first camera image
        color_image = color_images[0]

        gray = cv2.cvtColor(color_image, cv2.COLOR_RGB2GRAY)

        # Show the image
        cv2.imshow("Video", color_image)

        # Wait until a key pressed
        key = cv2.waitKey(2)

        if key == ord('q') or key == 27:
            # Destroy all the windows opened before
            cv2.destroyAllWindows()
            break
finally:

    # Stop streaming
    camera.stop()
