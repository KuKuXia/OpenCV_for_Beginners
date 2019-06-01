import cv2
import numpy as np

img = cv2.imread("./images/red_panda.jpg")
rows, cols, ch = img.shape
print("Height: ", rows)
print("Width: ", cols)

scaled_img = cv2.resize(img, None, fx=1/2, fy=1/2)
matrix_t = np.float32([[1, 0, -100], [0, 1, -30]])
translated_img = cv2.warpAffine(img, matrix_t, (cols, rows))
matrix_r = cv2.getRotationMatrix2D((cols / 2, rows / 2), 90, 0.5)
rotated_img = cv2.warpAffine(img, matrix_r, (cols, rows))


cv2.imshow("Original image", img)
cv2.imshow("Scaled image", scaled_img)
cv2.imshow("Translated image", translated_img)
cv2.imshow("Rotated image", rotated_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
