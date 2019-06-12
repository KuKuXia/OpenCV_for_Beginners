"""
Convex Hull
original url:
https://www.learnopencv.com/convex-hull-using-opencv-in-python-and-c/

Convex
    A Convex object is one with no interior angles greater than 180 degrees. A shape that is not convex is called Non-Convex or Concave.

Hull
    it means the exterior or the shape of the object.

Convex Hull
    The Convex Hull of a shape or a group of points is a tight fitting convex boundary around the points or the shape.

Applications of Convex Hull
    - Boundary from a set of points
    - Collision Avoidance
"""

# Import the packages
import cv2
import numpy as np
import sys

if __name__ == "__main__":
    if(len(sys.argv)) < 2:
        file_path = "./images/sample.jpg"
    else:
        file_path = sys.argv[1]

    # read image
    src = cv2.imread(file_path, 1)

    # show source image
    cv2.imshow("Source", src)

    # convert image to gray scale
    gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

    # blur the image
    blur = cv2.blur(gray, (3, 3))

    # binary thresholding of the image
    ret, thresh = cv2.threshold(blur, 200, 255, cv2.THRESH_BINARY)

    # find contours
    contours, _ = cv2.findContours(thresh, cv2.RETR_TREE,
                                   cv2.CHAIN_APPROX_SIMPLE)

    # create hull array for convexHull points
    hull = []

    # calculate points for each contour
    for i in range(len(contours)):
        hull.append(cv2.convexHull(contours[i], False))

    # create an empty black image
    drawing = np.zeros((thresh.shape[0], thresh.shape[1], 3), np.uint8)

    # draw contours and hull points
    for i in range(len(contours)):
        color_contours = (0, 255, 0)  # color for contours
        color = (255, 255, 255)  # color for convex hull
        # draw contours
        cv2.drawContours(drawing, contours, i, color_contours, 2, 8)
        # draw convex hull
        cv2.drawContours(drawing, hull, i, color, 2, 8)

    # Show the image
    cv2.imshow("Output", drawing)

    # Wait until a key pressed
    cv2.waitKey(0)

    # Destroy all the windows opened before
    cv2.destroyAllWindows()
