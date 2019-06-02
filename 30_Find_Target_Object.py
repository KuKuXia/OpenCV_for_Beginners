import matplotlib.pyplot as plt
import cv2

cap = cv2.VideoCapture(0)
while (cap.isOpened()):
    ret, frame = cap.read()
    cv2.imshow('Camera', frame)
    key = cv2.waitKey(1) & 0xFF
    if key == 27:
        break
cap.release()
cv2.destroyAllWindows()
cv2.imwrite("./images/object.jpg", frame)

img = cv2.imread('./images/object.jpg')
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
print(img_rgb.shape)

# img_object = img_rgb[215:310, 200:260, :]
# plt.imshow(img_object)
plt.imshow(img_rgb)
plt.show()

