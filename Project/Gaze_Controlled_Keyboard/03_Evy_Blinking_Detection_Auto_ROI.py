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

        left_eye_ratio = get_blinking_ratio(frame,
            [36, 37, 38, 39, 40, 41], landmarks)
        right_eye_ratio = get_blinking_ratio(frame,
            [42, 43, 44, 45, 46, 47], landmarks)
        blinking_ratio = (left_eye_ratio + right_eye_ratio) / 2

        if blinking_ratio > 7:
            cv2.putText(frame, "BLINKING", (50, 150), font, 7, (255, 0, 0))

    cv2.imshow("Frame", frame)

    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
