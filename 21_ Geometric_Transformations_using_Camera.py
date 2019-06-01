import cv2
import numpy as np

cap = cv2.VideoCapture(0)

# Git first frame to take the size of frame
_, frame = cap.read()
rows, cols, ch = frame.shape

print("Height: ", rows)
print("Width: ", cols)

while(cap.isOpened()):
    _, frame = cap.read()
    scaled_img = cv2.resize(frame, None, fx=1 / 2, fy=1 / 2)

    matrix_t = np.float32([[1, 0, -100], [0, 1, -100]])
    translated_img = cv2.warpAffine(frame, matrix_t, (cols, rows))

    matrix_r = cv2.getRotationMatrix2D((cols / 2, rows / 2), 90, 0.5)
    rotated_img = cv2.warpAffine(frame, matrix_r, (cols, rows))

    cv2.imshow("Original image", frame)
    cv2.imshow("Scaled image", scaled_img)
    cv2.imshow("Translated image", translated_img)
    cv2.imshow("Rotated image", rotated_img)
        
    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
