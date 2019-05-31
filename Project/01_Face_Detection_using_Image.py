import cv2
# Create a CascadeClassifier object
face_cascade = cv2.CascadeClassifier(
    ".\Project\haarcascade_frontalface_default.xml")

# Reading the image as it is
img = cv2.imread('.\images\lena.jpg')
print(img.shape)
# Reading the image as gray scale image
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Image', img)
# Search the co-ordinates of the image
# Decreased the shape value by 5%, until the face is found. Smaller this value, the greater is the accuracy.
faces = face_cascade.detectMultiScale(gray_img, scaleFactor=1.05,
                                      minNeighbors=1, minSize=(1, 1))

print(type(faces))
print(faces)

# Draw the rectangle box around the detected faces
if len(faces) > 0:
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.imshow('Image', img)

else:
    print("No faces detected in the image!")

while(1):
    if (cv2.waitKey(0) & 0xFF) == ord('q'):
        break
cv2.destroyAllWindows()
