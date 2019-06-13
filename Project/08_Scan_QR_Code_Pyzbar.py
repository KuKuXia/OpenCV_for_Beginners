"""
Online QR Code generator: https://tool.oschina.net/qr
"""

# Import the packages
import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar


# Display barcode and QR code location
def display(im, decodedObjects):

    # Loop over all decoded objects
    for decodedObject in decodedObjects:
        points = decodedObject.polygon

        # If the points do not form a quad, find convex hull
        if len(points) > 4:
            hull = cv2.convexHull(
                np.array([point for point in points], dtype=np.float32))
            hull = list(map(tuple, np.squeeze(hull)))
        else:
            hull = points

        # Number of points in the convex hull
        n = len(hull)

        # Draw the convex hull
        for j in range(0, n):
            cv2.line(im, hull[j], hull[(j+1) % n], (255, 0, 0), 3)


# Read the image
image = cv2.imread("../images/qr_code.png")

decodeObjects = pyzbar.decode(image)
for obj in decodeObjects:
    print("Type: {}, Data: {}.\n".format(obj.type, obj.data))

display(image, decodeObjects)

# Show the image
cv2.imshow("Image", image)

# Wait until a key pressed
key = cv2.waitKey(0) & 0xFF
if key == 27:
    # Destroy all the windows opened before
    cv2.destroyAllWindows()
