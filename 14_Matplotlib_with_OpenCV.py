import cv2
import matplotlib.pyplot as plt

img = cv2.imread('./images/lena.jpg', -1)
cv2.imshow('Image', img)

img_plt = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

plt.imshow(img_plt)
plt.xticks([])
plt.yticks([])
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
