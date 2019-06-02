import cv2
import numpy as np
import dlib
from math import hypot
from utilities import *

if __name__ == "__main__":

    board = np.zeros((500, 500), np.uint8)
    board[:] = 255

    cap = cv2.VideoCapture(0)

    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor(
        "./Project/Gaze_Controlled_Keyboard/shape_predictor_68_face_landmarks.dat")
    keyboard = Keyboard()

    # Counters
    frames = 0
    letter_index = 0
    blinking_frames = 0
    text = ""
    while(cap.isOpened()):
        _, frame = cap.read()
        frame = cv2.resize(frame, None, fx=0.5, fy=0.5)
        keyboard.set_background_color((255, 0, 255))
        frames += 1
        new_frame = np.zeros((500, 500, 3), np.uint8)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        font = cv2.FONT_HERSHEY_PLAIN

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

            if blinking_ratio > 5.7:
                cv2.putText(frame, "BLINKING", (50, 150), font, 7, (255, 0, 0))
                blinking_frames += 1
                frames -= 1

                if blinking_frames == 5:
                    active_letter = keyboard.keys_set_1[letter_index]
                    text += active_letter
            else:
                blinking_frames = 0

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

        # Letters
        if frames == 15:
            letter_index += 1
            frames = 0
        if letter_index == 15:
            letter_index = 0

        for i in range(15):
            if i == letter_index:
                light = True
            else:
                light = False
            keyboard.letter(i, light)
        cv2.putText(board, text, (10, 100), font, 4, 0, 3)

        keyboard.show_keyboard()
        cv2.imshow("Frame", frame)
        cv2.imshow("New frame", new_frame)
        cv2.imshow("Board", board)

        key = cv2.waitKey(1) & 0xFF
        if key == 27:
            break

    cap.release()
    cv2.destroyAllWindows()
