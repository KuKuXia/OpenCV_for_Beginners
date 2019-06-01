import cv2
import numpy as np

img = cv2.imread('./images/simpsons.jpg')

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
template = cv2.imread('./images/barts_face.jpg', cv2.IMREAD_GRAYSCALE)

W, H = template.shape[::-1]

result = cv2.matchTemplate(gray_img, template, cv2.TM_CCOEFF_NORMED)
loc = np.where(result > 0.4)

for pt in zip(*loc[::-1]):
    cv2.rectangle(img, pt, (pt[0] + W, pt[1] + H), (0, 255, 0), 3)

cv2.imshow('img', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
