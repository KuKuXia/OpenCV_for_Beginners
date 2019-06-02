from math import hypot
import cv2
import numpy as np
import dlib
from utilities import *

cap = cv2.VideoCapture(0)

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(
    "./Project/Gaze_Controlled_Keyboard/shape_predictor_68_face_landmarks.dat")


font = cv2.FONT_HERSHEY_PLAIN


while(cap.isOpened()):
    _, frame = cap.read()
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
        left_eye_region = np.array([(landmarks.part(36).x, landmarks.part(36).y),
                                    (landmarks.part(37).x, landmarks.part(37).y),
                                    (landmarks.part(38).x, landmarks.part(38).y),
                                    (landmarks.part(39).x, landmarks.part(39).y),
                                    (landmarks.part(40).x, landmarks.part(40).y),
                                    (landmarks.part(41).x, landmarks.part(41).y)], np.int32)
        cv2.polylines(frame, [left_eye_region], True, (0, 0, 255), 2)

        height, width, _ = frame.shape
        mask = np.zeros((height, width), np.uint8)
        cv2.polylines(mask, [left_eye_region], True, 255, 2)
        cv2.fillPoly(mask, [left_eye_region], 255)
        left_eye = cv2.bitwise_and(gray, gray, mask=mask)

        min_x = np.min(left_eye_region[:, 0])
        max_x = np.max(left_eye_region[:, 0])
        min_y = np.min(left_eye_region[:, 1])
        max_y = np.max(left_eye_region[:, 1])

        gray_eye = left_eye[min_y: max_y, min_x: max_x]
        _, threshold_eye = cv2.threshold(gray_eye, 60, 255, cv2.THRESH_BINARY)

        threshold_eye = cv2.resize(threshold_eye, None, fx=5, fy=5)
        eye = cv2.resize(gray_eye, None, fx=20, fy=20)
        cv2.imshow("Eye", eye)
        cv2.imshow("Threshold", threshold_eye)
        cv2.imshow("Left eye", left_eye)

    cv2.imshow("Frame", frame)

    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
