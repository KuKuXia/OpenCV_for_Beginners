"""
Draw draw geometric shapes on image

Some common arguments as given below:

    - img : The image where you want to draw the shapes
    - color : Color of the shape. for BGR, pass it as a tuple, eg: (255,0,0) for blue. For grayscale, just pass the scalar value.
    - thickness : Thickness of the line or circle etc. If -1 is passed for closed figures like circles, it will fill the shape. default thickness = 1
    - lineType : Type of line, whether 8-connected, anti-aliased line etc. By default, it is 8-connected. cv2.LINE_AA gives anti-aliased line which looks great for curves.

"""

# Import the packages
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
img = cv2.ellipse(img, (256, 256), (100, 50), 0, 0, 270, 255, -1)

# Draw polylines
"""
cv2.polylines() can be used to draw multiple lines. Just create a list of all the lines you want to draw and pass it to the function. All lines will be drawn individually. It is more better and faster way to draw a group of lines than calling cv2.line() for each line.
"""
pts = np.array([[10, 5], [20, 30], [70, 20], [50, 10]], np.int32)
pts = pts.reshape((-1, 1, 2))
img = cv2.polylines(img, [pts], True, (0, 255, 255))

cv2.imshow('image', img)

# Wait until a key pressed
cv2.waitKey(0)

# Destroy all the windows opened before
cv2.destroyAllWindows()
