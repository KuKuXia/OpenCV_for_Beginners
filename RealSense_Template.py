import cv2
import numpy as np
import pyrealsense2 as rs
import sys
from realsense_opencv import Realsense, DEVICE_ONE, DEVICE_TWO

cv2.namedWindow("Video", cv2.WINDOW_NORMAL)

camera_num = 1
camera = Realsense(camera_num=camera_num, device_id=[
    DEVICE_ONE, DEVICE_TWO], color_resolution=[1280, 720], depth_resolution=[1280, 720])

try:
    while True:
        color_images, depth_images, depth_colormaps = camera.get_images()
        color_image = color_images[0]
        gray = cv2.cvtColor(color_image, cv2.COLOR_RGB2GRAY)

        cv2.imshow("Video", color_image)

        key = cv2.waitKey(2)
        if key == ord('q') or key == 27:
            cv2.destroyAllWindows()
            break
finally:

    # Stop streaming
    camera.stop()
