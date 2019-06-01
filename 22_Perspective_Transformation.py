import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(cap.isOpened()):
    _, frame = cap.read()

    # Draw the four points in the frame
    cv2.circle(frame, (155, 120), 5, (0, 0, 255), -1)
    cv2.circle(frame, (480, 120), 8, (0, 0, 255), -1)
    cv2.circle(frame, (20, 475), 11, (0, 0, 255), -1)
    cv2.circle(frame, (620, 475), 13, (0, 0, 255), -1)

    # Choose the source points and destination points.
    pts1 = np.float32([[155, 120], [480, 120], [20, 475], [620, 475]])
    pts2 = np.float32([[0, 0], [500, 0], [0, 600], [500, 600]])

    matrix = cv2.getPerspectiveTransform(pts1, pts2)
    result = cv2.warpPerspective(frame, matrix, (500, 600))
    # print(result.shape)
    # Write (x,y), print (y,x)
    cv2.imshow("Frame", frame)
    cv2.imshow("Perspective transformation", result)

    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
