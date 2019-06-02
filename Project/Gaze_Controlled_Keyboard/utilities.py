from math import hypot
import cv2
import numpy as np


class Keyboard(object):

    def __init__(self, key_set_1=None, key_set_2=None):

        self.keyboard = np.zeros((600, 1000, 3), np.uint8)
        if not key_set_1:
            self.keys_set_1 = {0: "Q", 1: "W", 2: "E", 3: "R", 4: "T",
                               5: "A", 6: "S", 7: "D", 8: "F", 9: "G",
                               10: "Z", 11: "X", 12: "C", 13: "V", 14: "B"}
        else:
            self.keys_set_1 = key_set_1
        if key_set_2:
            self.keys_set_2 = key_set_2
        else:
            self.keys_set_2 = None

    def set_background_color(self, color):
        self.keyboard[:] = color

    def letter(self, letter_index, letter_light):
        # Keys
        if letter_index == 0:
            x = 0
            y = 0
        elif letter_index == 1:
            x = 200
            y = 0
        elif letter_index == 2:
            x = 400
            y = 0
        elif letter_index == 3:
            x = 600
            y = 0
        elif letter_index == 4:
            x = 800
            y = 0
        elif letter_index == 5:
            x = 0
            y = 200
        elif letter_index == 6:
            x = 200
            y = 200
        elif letter_index == 7:
            x = 400
            y = 200
        elif letter_index == 8:
            x = 600
            y = 200
        elif letter_index == 9:
            x = 800
            y = 200
        elif letter_index == 10:
            x = 0
            y = 400
        elif letter_index == 11:
            x = 200
            y = 400
        elif letter_index == 12:
            x = 400
            y = 400
        elif letter_index == 13:
            x = 600
            y = 400
        elif letter_index == 14:
            x = 800
            y = 400

        width = 200
        height = 200
        th = 3  # thickness
        if letter_light is True:
            cv2.rectangle(self.keyboard, (x + th, y + th), (x + width -
                                                            th, y + height - th), (255, 255, 255), -1)
        else:
            cv2.rectangle(self.keyboard, (x + th, y + th),
                          (x + width - th, y + height - th), (255, 0, 0), th)

        # Text settings
        font_letter = cv2.FONT_HERSHEY_PLAIN
        font_scale = 10
        font_th = 4
        text = self.keys_set_1[letter_index]
        text_size = cv2.getTextSize(text, font_letter, font_scale, font_th)[0]
        width_text, height_text = text_size[0], text_size[1]
        text_x = int((width - width_text) / 2) + x
        text_y = int((height + height_text) / 2) + y
        cv2.putText(self.keyboard, text, (text_x, text_y),
                    font_letter, font_scale, (255, 0, 0), font_th)

    def show_keyboard(self):
        cv2.imshow("keyboard", self.keyboard)


def draw_menu(keyboard, font):
    rows, cols, _ = keyboard.shape
    th_lines = 4  # thickness lines
    cv2.line(keyboard, (int(cols/2) - int(th_lines/2), 0), (int(cols/2) - int(th_lines/2), rows),
             (51, 51, 51), th_lines)
    cv2.putText(keyboard, "LEFT", (80, 300), font, 6, (255, 255, 255), 5)
    cv2.putText(keyboard, "RIGHT", (80 + int(cols/2), 300),
                font, 6, (255, 255, 255), 5)


def eyes_contour_points(facial_landmarks):
    left_eye = []
    right_eye = []
    for n in range(36, 42):
        x = facial_landmarks.part(n).x
        y = facial_landmarks.part(n).y
        left_eye.append([x, y])
    for n in range(42, 48):
        x = facial_landmarks.part(n).x
        y = facial_landmarks.part(n).y
        right_eye.append([x, y])
    left_eye = np.array(left_eye, np.int32)
    right_eye = np.array(right_eye, np.int32)
    return left_eye, right_eye


def midpoint(p1, p2):
    return int((p1.x + p2.x)/2), int((p1.y + p2.y)/2)


def get_blinking_ratio(frame, eye_points, facial_landmarks):
    """
      1 2 
    0     3
      4 5 
    """
    left_point = (facial_landmarks.part(
        eye_points[0]).x, facial_landmarks.part(eye_points[0]).y)
    right_point = (facial_landmarks.part(
        eye_points[3]).x, facial_landmarks.part(eye_points[3]).y)
    center_top = midpoint(facial_landmarks.part(
        eye_points[1]), facial_landmarks.part(eye_points[2]))
    center_bottom = midpoint(facial_landmarks.part(
        eye_points[5]), facial_landmarks.part(eye_points[4]))

    hor_line = cv2.line(frame, left_point, right_point, (0, 255, 0), 2)
    ver_line = cv2.line(frame, center_top, center_bottom, (0, 255, 0), 2)

    hor_line_length = hypot(
        (left_point[0] - right_point[0]), (left_point[1] - right_point[1]))
    ver_line_length = hypot(
        (center_top[0] - center_bottom[0]), (center_top[1] - center_bottom[1]))

    # In case of zero
    ratio = hor_line_length / (ver_line_length + 0.001)
    return ratio


"""
Currently only used one eye.
"""


def get_gaze_ratio(frame, gray, eye_points, facial_landmarks):
    left_eye_region = np.array([
        (facial_landmarks.part(eye_points[0]).x,
         facial_landmarks.part(eye_points[0]).y),
        (facial_landmarks.part(eye_points[1]).x,
         facial_landmarks.part(eye_points[1]).y),
        (facial_landmarks.part(eye_points[2]).x,
         facial_landmarks.part(eye_points[2]).y),
        (facial_landmarks.part(eye_points[3]).x,
         facial_landmarks.part(eye_points[3]).y),
        (facial_landmarks.part(eye_points[4]).x,
         facial_landmarks.part(eye_points[4]).y),
        (facial_landmarks.part(eye_points[5]).x,
         facial_landmarks.part(eye_points[5]).y)], np.int32)
    # cv2.polylines(frame, [left_eye_region], True, (0, 0, 255), 2)

    height, width, _ = frame.shape
    mask = np.zeros((height, width), np.uint8)
    cv2.polylines(mask, [left_eye_region], True, 255, 2)
    cv2.fillPoly(mask, [left_eye_region], 255)
    eye = cv2.bitwise_and(gray, gray, mask=mask)

    min_x = np.min(left_eye_region[:, 0])
    max_x = np.max(left_eye_region[:, 0])
    min_y = np.min(left_eye_region[:, 1])
    max_y = np.max(left_eye_region[:, 1])

    # Divide the eye into two parts, one is black, one is white, compute the ratio
    gray_eye = eye[min_y: max_y, min_x: max_x]
    ret, threshold_eye = cv2.threshold(gray_eye, 60, 255, cv2.THRESH_BINARY)
    if ret:
        height, width = threshold_eye.shape

        left_side_threshold = threshold_eye[0: height, 0: int(width / 2)]
        left_side_white = cv2.countNonZero(left_side_threshold)

        right_side_threshold = threshold_eye[0: height, int(width / 2): width]
        right_side_white = cv2.countNonZero(right_side_threshold)

        if left_side_white < 10:
            gaze_ratio = 0.5
        elif right_side_white < 10:
            gaze_ratio = 5
        else:
            gaze_ratio = left_side_white / (right_side_white+0.001)
        return gaze_ratio
    else:
        return 0
