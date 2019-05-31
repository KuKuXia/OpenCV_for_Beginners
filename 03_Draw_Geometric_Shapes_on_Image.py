# encoding:utf-8
import numpy as np
import cv2

# img = np.zeros([512, 512, 3], np.uint8)
img = cv2.imread('./images/lena.jpg', 1)

# Draw a line on the image
img = cv2.line(img, (0, 0), (255, 255), (147, 96, 44), 10)

# Draw an arrowed line on the image
img = cv2.arrowedLine(img, (0, 255), (255, 255), (255, 0, 0), 10)

# Draw a rectangle on the image
img = cv2.rectangle(img, (384, 0), (510, 128), (0, 0, 255), 10)

# Draw a circle on the image
img = cv2.circle(img, (447, 63), 63, (0, 255, 0), -1)

# Print the text on the image
font = cv2.FONT_HERSHEY_SIMPLEX
img = cv2.putText(img, 'Hello OpenCv', (10, 500), font,
                  2, (0, 255, 255), 10, cv2.LINE_AA)

# Draw an ellipse on the image
img = cv2.ellipse(img, (256, 256), (100, 50), 0, 0, 180, 255, -1)

# Draw polylines
pts = np.array([[10, 5], [20, 30], [70, 20], [50, 10]], np.int32)
pts = pts.reshape((-1, 1, 2))
img = cv2.polylines(img, [pts], True, (0, 255, 255))

cv2.imshow('image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
