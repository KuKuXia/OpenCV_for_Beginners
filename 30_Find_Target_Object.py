import matplotlib.pyplot as plt
import cv2

img = cv2.imread('object.jpg')
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
print(img_rgb.shape)

img_object = img_rgb[215:310, 200:260, :]
plt.imshow(img_object)
# plt.imshow(img_rgb)
plt.show()
