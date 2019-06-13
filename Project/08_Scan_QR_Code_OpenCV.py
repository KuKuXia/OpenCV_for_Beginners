"""
Scan QR code using OpenCV
Original url:
https://www.learnopencv.com/opencv-qr-code-scanner-c-and-python/
"""
# Import the packages
import cv2
import numpy as np
import sys
import time

if len(sys.argv) > 1:
    inputImage = cv2.imread(sys.argv[1])
else:
    # inputImage = cv2.imread("../images/qr_code.png")  # Can't detect this image
    inputImage = cv2.imread("../images/qrcode-learnopencv.jpg")

# Display barcode and QR code location


def display(im, bbox):
    n = len(bbox)
    for j in range(n):
        cv2.line(im, tuple(bbox[j][0]), tuple(
            bbox[(j+1) % n][0]), (255, 0, 0), 3)

    # Display results
    cv2.imshow("Results", im)


# Create a qrCodeDetector Object
qrDecoder = cv2.QRCodeDetector()

# Detect and decode the QR code
t = time.time()
data, bbox, rectifiedImage = qrDecoder.detectAndDecode(inputImage)
print("Time Taken for Detect and Decode : {:.3f} seconds".format(
    time.time() - t))
if len(data) > 0:
    print("Decoded Data : {}".format(data))
    display(inputImage, bbox)
    rectifiedImage = np.uint8(rectifiedImage)
    cv2.imshow("Rectified QRCode", rectifiedImage)
else:
    print("QR Code not detected")
    cv2.imshow("Results", inputImage)

# Wait until a key pressed
cv2.waitKey(0)

# Destroy all the windows opened before
cv2.destroyAllWindows()
