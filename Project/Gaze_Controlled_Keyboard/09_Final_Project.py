import cv2
import numpy as np
import dlib
from math import hypot
from utilities import *
import pyglet
import time

if __name__ == "__main__":

    # Load sounds
    sound = pyglet.media.load(
        "./Project/Gaze_Controlled_Keyboard/sound.wav", streaming=False)
    left_sound = pyglet.media.load(
        "./Project/Gaze_Controlled_Keyboard/left.wav", streaming=False)
    right_sound = pyglet.media.load(
        "./Project/Gaze_Controlled_Keyboard/right.wav", streaming=False)

    board = np.zeros((300, 1400), np.uint8)
    board[:] = 255

    cap = cv2.VideoCapture(0)

    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor(
        "./Project/Gaze_Controlled_Keyboard/shape_predictor_68_face_landmarks.dat")

    keys_set_1 = {0: "Q", 1: "W", 2: "E", 3: "R", 4: "T",
                  5: "A", 6: "S", 7: "D", 8: "F", 9: "G",
                  10: "Z", 11: "X", 12: "C", 13: "V", 14: "<"}
    keys_set_2 = {0: "Y", 1: "U", 2: "I", 3: "O", 4: "P",
                  5: "H", 6: "J", 7: "K", 8: "L", 9: "_",
                  10: "V", 11: "B", 12: "N", 13: "M", 14: "<"}
    keyboard = Keyboard(keys_set_1, keys_set_2)

    # Counters
    frames = 0
    letter_index = 0
    blinking_frames = 0
    frames_to_blink = 6
    frames_active_letter = 9

    # Text and keyboard settings
    text = ""
    keyboard_selected = "left"
    last_keyboard_selected = "left"
    select_keyboard_menu = True
    keyboard_selection_frames = 0

    while(cap.isOpened()):
        _, frame = cap.read()
        frame = cv2.resize(frame, None, fx=0.5, fy=0.5)
        rows, cols, _ = frame.shape
        keyboard.set_background_color((255, 0, 255))
        frames += 1
        new_frame = np.zeros((500, 500, 3), np.uint8)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        font = cv2.FONT_HERSHEY_PLAIN

        # Draw a white space for loading bar
        frame[rows - 50: rows, 0: cols] = (255, 255, 255)

        if select_keyboard_menu:
            draw_menu(keyboard.keyboard, font)

        # Keyboard selected
        if keyboard_selected == "left":
            keys_set = keys_set_1
        else:
            keys_set = keys_set_2
        # Face Detection
        faces = detector(gray)
        for face in faces:
            #x, y = face.left(), face.top()
            #x1, y1 = face.right(), face.bottom()
            #cv2.rectangle(frame, (x, y), (x1, y1), (0, 255, 0), 2)

            landmarks = predictor(gray, face)

            # Eye points
            left_eye, right_eye = eyes_contour_points(landmarks)
            # Eyes color
            cv2.polylines(frame, [left_eye], True, (0, 0, 255), 2)
            cv2.polylines(frame, [right_eye], True, (0, 0, 255), 2)

            # Detect blinking
            left_eye_ratio = get_blinking_ratio(frame,
                                                [36, 37, 38, 39, 40, 41], landmarks)
            right_eye_ratio = get_blinking_ratio(frame,
                                                 [42, 43, 44, 45, 46, 47], landmarks)
            blinking_ratio = (left_eye_ratio + right_eye_ratio) / 2

            if select_keyboard_menu is True:
                # Detecting gaze to select Left or Right keyboard
                gaze_ratio_left_eye = get_gaze_ratio(frame, gray,
                                                     [36, 37, 38, 39, 40, 41], landmarks)
                gaze_ratio_right_eye = get_gaze_ratio(frame, gray,
                                                      [42, 43, 44, 45, 46, 47], landmarks)
                gaze_ratio = (gaze_ratio_right_eye + gaze_ratio_left_eye) / 2

                if gaze_ratio < 0.7:
                    print(
                        "Detected Right. Gaze ratio is: {:.3f}.".format(gaze_ratio))
                    keyboard_selected = "right"
                    keyboard_selection_frames += 1
                    # If Kept gaze on one side more than 15 frames, move to keyboard
                    if keyboard_selection_frames == 15:
                        select_keyboard_menu = False
                        right_sound.play()
                        # Set frames count to 0 when keyboard selected
                        frames = 0
                        keyboard_selection_frames = 0
                    if keyboard_selected != last_keyboard_selected:
                        last_keyboard_selected = keyboard_selected
                        keyboard_selection_frames = 0
                elif 0.7 <= gaze_ratio <= 1.0:
                    print(
                        "Detected Center. Gaze ratio is: {:.3f}.".format(gaze_ratio))
                else:
                    print(
                        "Detected Left. Gaze ratio is: {:.3f}.".format(gaze_ratio))
                    keyboard_selected = "left"
                    keyboard_selection_frames += 1
                    # If Kept gaze on one side more than 15 frames, move to keyboard
                    if keyboard_selection_frames == 15:
                        select_keyboard_menu = False
                        left_sound.play()
                        # Set frames count to 0 when keyboard selected
                        frames = 0
                    if keyboard_selected != last_keyboard_selected:
                        last_keyboard_selected = keyboard_selected
                        keyboard_selection_frames = 0

            else:
                 # Detect the blinking to select the key that is lighting up
                if blinking_ratio > 5:
                    # cv2.putText(frame, "BLINKING", (50, 150), font, 4, (255, 0, 0), thickness=3)
                    blinking_frames += 1
                    frames -= 1

                    # Show green eyes when closed
                    cv2.polylines(frame, [left_eye], True, (0, 255, 0), 2)
                    cv2.polylines(frame, [right_eye], True, (0, 255, 0), 2)

                    # Typing letter
                    active_letter = keyboard.keys_set_1[letter_index]
                    if blinking_frames == frames_to_blink:
                        if active_letter != "<" and active_letter != "_":
                            text += active_letter
                        if active_letter == "_":
                            text += " "
                        sound.play()
                        select_keyboard_menu = True
                        # time.sleep(1)

                else:
                    blinking_frames = 0

        # Display letters on the keyboard
        if select_keyboard_menu is False:
            if frames == frames_active_letter:
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

        cv2.putText(board, text, (80, 100), font, 9, 0, 3)
        # Blinking loading bar
        percentage_blinking = blinking_frames / frames_to_blink
        loading_x = int(cols * percentage_blinking)
        cv2.rectangle(frame, (0, rows - 50),
                      (loading_x, rows), (51, 51, 51), -1)

        keyboard.show_keyboard()
        cv2.imshow("Frame", frame)
        cv2.imshow("New frame", new_frame)
        cv2.imshow("Board", board)

        key = cv2.waitKey(1) & 0xFF
        if key == 27:
            break

    cap.release()
    cv2.destroyAllWindows()
