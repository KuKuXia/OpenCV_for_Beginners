
"""
Read camera frame rate

For video files, just register the video object and call the function:
video.get(cv2.CAP_PROP_FPS)
"""

# Import the packages
import cv2
import time
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

        # Number of frames to capture
        num_frames = 120

        print("Capturing {0} frames".format(num_frames))

        # Start time
        start = time.time()

        # Grab a few frames
        for i in range(0, num_frames):
            color_images, depth_images, depth_colormaps = camera.get_images()
        # End time
        end = time.time()

        color_image = color_images[0]
        cv2.imshow("Video", color_image)

        # Time elapsed
        seconds = end - start
        print("Time taken : {0} seconds".format(seconds))

        # Calculate frames per second
        fps = num_frames / seconds
        print("Estimated frames per second : {0}".format(fps))

        # Wait until a key pressed
        key = cv2.waitKey(2)

        if key == ord('q') or key == 27:
            # Destroy all the windows opened before
            cv2.destroyAllWindows()
            break
finally:

    # Stop streaming
    camera.stop()
