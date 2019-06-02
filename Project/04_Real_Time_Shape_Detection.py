import cv2
import numpy as np


def nothing(x):
    pass


cap = cv2.VideoCapture(0)

cv2.namedWindow("Trackbars")
cv2.createTrackbar("LH", "Trackbars", 0, 180, nothing)
cv2.createTrackbar("UH", "Trackbars", 180, 180, nothing)
cv2.createTrackbar("LS", "Trackbars", 66, 255, nothing)
cv2.createTrackbar("US", "Trackbars", 255, 255, nothing)
cv2.createTrackbar("LV", "Trackbars", 134, 255, nothing)
cv2.createTrackbar("UV", "Trackbars", 243, 255, nothing)

font = cv2.FONT_HERSHEY_COMPLEX

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret:
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        l_h = cv2.getTrackbarPos("LH", "Trackbars")
        l_s = cv2.getTrackbarPos("LS", "Trackbars")
        l_v = cv2.getTrackbarPos("LV", "Trackbars")
        u_h = cv2.getTrackbarPos("UH", "Trackbars")
        u_s = cv2.getTrackbarPos("US", "Trackbars")
        u_v = cv2.getTrackbarPos("UV", "Trackbars")

        lower_red = np.array([l_h, l_s, l_v])
        upper_red = np.array([u_h, u_s, u_v])

        mask = cv2.inRange(hsv, lower_red, upper_red)
        kernel = np.ones((5, 5), np.uint8)
        mask = cv2.erode(mask, kernel)

        # Contours detection
        contours, _ = cv2.findContours(
            mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        for cnt in contours:
            area = cv2.contourArea(cnt)
            approx = cv2.approxPolyDP(cnt, 0.02*cv2.arcLength(cnt, True), True)
            x = approx.ravel()[0]
            y = approx.ravel()[1]

            if area > 400:
                cv2.drawContours(frame, [approx], 0, (0, 0, 0), 5)

                if len(approx) == 3:
                    cv2.putText(frame, "Triangle", (x, y), font, 1, (0, 0, 0))
                elif len(approx) == 4:
                    cv2.putText(frame, "Rectangle", (x, y), font, 1, (0, 0, 0))
                elif 10 < len(approx) < 20:
                    cv2.putText(frame, "Circle", (x, y), font, 1, (0, 0, 0))

        cv2.imshow("Trackbars", frame)
        cv2.imshow("Mask", mask)

    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
