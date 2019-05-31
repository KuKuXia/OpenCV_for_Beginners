"""
Homogeneous filter is the most simple filter, each output pixel is the mean of its kernal neighbors. 

Low Pass Filters(LPF): Help in removing noises, blurring the images.
High Pass Filters(HPF): Help in finding the edges in the images
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

# img = cv2.imread('./images/lena.jpg')
img = cv2.imread('./images/Noise_salt_and_pepper.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

kernel = np.ones((5, 5), np.float32) / 25

# 2D Convolutional Filter
dst = cv2.filter2D(img, -1, kernel)

# Averaging filter
blur = cv2.blur(img, (5, 5))

# Gaussian filter
gaussian_blur = cv2.GaussianBlur(img, (5, 5), 0)

# Median filter: replacing each pixel's value with the median of its neighboring pixels. This method is great when dealing with "salt and pepper noise".
median = cv2.medianBlur(img, 5)

# Bilateral filter: a non-linear, edge-preserving, and noise-reducing smoothing filter for images
bilateralFilter = cv2.bilateralFilter(img, 9, 75, 75)

titles = ['image', '2D Convolution', 'blur',
          'GaussianBlur', 'median', 'bilateralFilter']
images = [img, dst, blur, gaussian_blur, median, bilateralFilter]

for i in range(6):
    plt.subplot(2, 3, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()
