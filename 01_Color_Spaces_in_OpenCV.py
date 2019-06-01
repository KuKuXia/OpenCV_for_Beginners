import cv2

number = 0
for filename in dir(cv2):
    if filename.startswith('COLOR_'):
        number += 1
        print(filename)
    
print("There are {} kinds of color methods in OpenCV.".format(str(number)))
