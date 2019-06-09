"""
Online QR Code generator: https://tool.oschina.net/qr
"""

import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar

image = cv2.imread("./images/qr_code.png")

decodeObjects = pyzbar.decode(image)
for obj in decodeObjects:
    print("Type: {}, Data: {}.\n".format(obj.type, obj.data))

cv2.imshow("Frame", image)
key = cv2.waitKey(0) & 0xFF
if key == 27:
    cv2.destroyAllWindows()
