"""
Please download the images from: 
https://pysource.com/2018/08/04/fourier-transform-opencv-3-4-with-python-3-tutorial-35/
"""

import cv2
import numpy as np
import glob

list_images = glob.iglob("./images/letters/*")

for image_title in list_images:
    img = cv2.imread(image_title, cv2.IMREAD_GRAYSCALE)
    f = np.fft.fft2(img)
    fshift = np.fft.fftshift(f)
    magnitude_spectrum = 20*np.log(np.abs(fshift))
    magnitude_spectrum = np.asarray(magnitude_spectrum, dtype=np.uint8)
    img_and_magnitude = np.concatenate((img, magnitude_spectrum), axis=1)

    cv2.imshow(image_title, img_and_magnitude)

cv2.waitKey(0)
cv2.destroyAllWindows()
