import cv2
import numpy as np

video = cv2.VideoCapture(0)
first_frame = cv2.imread('./images/object.jpg')

x = 200
y = 215
width = 60
height = 95
roi = first_frame[y: y + height, x: x + width]

hsv_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
roi_hist = cv2.calcHist([hsv_roi], [0], None, [180], [0, 180])

cap = cv2.VideoCapture(0)

term_criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1)

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret:
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        mask = cv2.calcBackProject([hsv], [0], roi_hist, [0, 180], 1)

        # # Filtering remove noise
        # kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))

        # mask = cv2.filter2D(mask, -1, kernel)
        # _, mask = cv2.threshold(mask, 150, 255, cv2.THRESH_BINARY)

        ret, track_window = cv2.CamShift(
            mask, (x, y, width, height), term_criteria)

        pts = cv2.boxPoints(ret)
        pts = np.int64(pts)
        cv2.polylines(frame, [pts], True, (255, 0, 0), 2)

        cv2.imshow("mask", mask)
        cv2.imshow("Frame", frame)
    key = cv2.waitKey(1)
    if key == 27:
        break
cap.release()
cv2.destroyAllWindows()
