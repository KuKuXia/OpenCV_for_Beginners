"""
1. Using the detector function in dlib to detect the face
2. Using the predictor function in dlib to find the landmarkers
3. Using the eye points defined in dlib to extract the eye region
4. Threshold the eye region and divide it into two parts:
    1. Black part
    2. White part
5. Count the nonzero pixel in the eye region and compute the gaze_ratio
6. Output the gaze status according to the gaze_ratio  
"""

from math import hypot

import cv2
import numpy as np

import dlib
from utilities import *

if __name__ == "__main__":

    cap = cv2.VideoCapture(0)

    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor(
        "./Project/Gaze_Controlled_Keyboard/shape_predictor_68_face_landmarks.dat")

    font = cv2.FONT_HERSHEY_PLAIN

    while True:
        _, frame = cap.read()
        new_frame = np.zeros((500, 500, 3), np.uint8)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = detector(gray)
        for face in faces:
            #x, y = face.left(), face.top()
            #x1, y1 = face.right(), face.bottom()
            #cv2.rectangle(frame, (x, y), (x1, y1), (0, 255, 0), 2)

            landmarks = predictor(gray, face)

            # Detect blinking
            left_eye_ratio = get_blinking_ratio(frame,
                                                [36, 37, 38, 39, 40, 41], landmarks)
            right_eye_ratio = get_blinking_ratio(frame,
                                                 [42, 43, 44, 45, 46, 47], landmarks)
            blinking_ratio = (left_eye_ratio + right_eye_ratio) / 2

            if blinking_ratio > 7:
                cv2.putText(frame, "BLINKING", (50, 150), font, 7, (255, 0, 0))

            # Gaze detection
            gaze_ratio_left_eye = get_gaze_ratio(frame, gray,
                                                 [36, 37, 38, 39, 40, 41], landmarks)
            gaze_ratio_right_eye = get_gaze_ratio(frame, gray,
                                                  [42, 43, 44, 45, 46, 47], landmarks)
            gaze_ratio = (gaze_ratio_right_eye + gaze_ratio_left_eye) / 2

            if gaze_ratio < 0.7:
                cv2.putText(frame, "RIGHT", (50, 100), font, 2, (0, 0, 255), 3)
                new_frame[:] = (0, 0, 255)
                print(
                    "Detected Right. Gaze ratio is: {:.3f}.".format(gaze_ratio))
            elif 0.7 <= gaze_ratio <= 1.0:
                cv2.putText(frame, "CENTER", (50, 100),
                            font, 2, (0, 0, 255), 3)
                new_frame[:] = (0, 255, 0)
                print(
                    "Detected Center. Gaze ratio is: {:.3f}.".format(gaze_ratio))
            else:
                new_frame[:] = (255, 0, 0)
                cv2.putText(frame, "LEFT", (50, 100), font, 2, (0, 0, 255), 3)
                print(
                    "Detected Left. Gaze ratio is: {:.3f}.".format(gaze_ratio))
            cv2.imshow("Frame", frame)
            cv2.imshow("New frame", new_frame)

        key = cv2.waitKey(1)
        if key == 27:
            break

    cap.release()
    cv2.destroyAllWindows()
