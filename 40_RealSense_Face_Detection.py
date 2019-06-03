"""
conda install -c conda-forge dlib
"""
import cv2
import numpy as np
import pyrealsense2 as rs
import dlib
import sys
from realsense_opencv import Realsense, DEVICE_ONE, DEVICE_TWO

cv2.namedWindow("Video", cv2.WINDOW_NORMAL)

camera_num = 1
camera = Realsense(camera_num=camera_num, device_id=[
    DEVICE_ONE, DEVICE_TWO], color_resolution=[1280, 720], depth_resolution=[1280, 720])

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(
    "./Project/Gaze_Controlled_Keyboard/shape_predictor_68_face_landmarks.dat")

try:
    while True:
        color_images, depth_images, depth_colormaps = camera.get_images()
        color_image = color_images[0]
        gray = cv2.cvtColor(color_image, cv2.COLOR_RGB2GRAY)
        faces = detector(gray)

        for face in faces:
            x1 = face.left()
            y1 = face.top()
            x2 = face.right()
            y2 = face.bottom()
            cv2.rectangle(color_image, (x1, y1), (x2, y2), (0, 255, 0), 3)

            landmarks = predictor(gray, face)

            for n in range(0, 68):
                x = landmarks.part(n).x
                y = landmarks.part(n).y
                cv2.circle(color_image, (x, y), 4, (255, 0, 0), -1)

        cv2.imshow("Video", color_image)

        key = cv2.waitKey(2)
        if key == ord('q') or key == 27:
            cv2.destroyAllWindows()
            break
finally:

    # Stop streaming
    camera.stop()
