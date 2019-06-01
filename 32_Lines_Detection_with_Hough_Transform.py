import cv2
import numpy as np

# Read and convert the image
img = cv2.imread("./images/lines.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Using Canny to detect edges
edges = cv2.Canny(gray, 75, 150)

# Using hough transform to detect lines
# lines = cv2.HoughLinesP(edges, 1, np.pi/180, 200, maxLineGap=250)  # Both vertical and horizontal lines
lines = cv2.HoughLinesP(edges, 1, np.pi/180, 50, maxLineGap=250) # Only the horizontal lines

print(lines)
for line in lines:
    x1, y1, x2, y2 = line[0]
    cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 3)

cv2.imshow('Gray', gray)
cv2.imshow('Edges', edges)
cv2.imshow('Image Plus Lines', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
