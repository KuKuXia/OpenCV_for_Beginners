import cv2
import numpy as np

cap = cv2.VideoCapture(0)

# Set the camera properties
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

# Check the setting
print(cap.get(3))
print(cap.get(4))

# WINDOW_NORMAL设置了这个值，用户便可以改变窗口的大小（没有限制)
# INDOW_AUTOSIZE如果设置了这个值，窗口大小会自动调整以适应所显示的图像，并且不能手动改变窗口大小.
# WINDOW_OPENGL 如果设置了这个值的话，窗口创建的时候便会支持OpenG
cv2.namedWindow('Control Panel', cv2.WINDOW_NORMAL)

# Callback function when the trackbar changed the value


def nothing(x):
    pass


# Create the trackbar for the HSV channels
cv2.createTrackbar('LH', 'Control Panel', 0, 179, nothing)
cv2.createTrackbar('UH', 'Control Panel', 179, 179, nothing)

cv2.createTrackbar('LS', 'Control Panel', 0, 255, nothing)
cv2.createTrackbar('US', 'Control Panel', 255, 255, nothing)

cv2.createTrackbar('LV', 'Control Panel', 0, 255, nothing)
cv2.createTrackbar('UV', 'Control Panel', 255, 255, nothing)

# Set the ROI trackbar
cv2.createTrackbar('L Rows', 'Control Panel', 0, 720, nothing)
cv2.createTrackbar('U Rows', 'Control Panel', 720, 720, nothing)

cv2.createTrackbar('L Cols', 'Control Panel', 0, 1280, nothing)
cv2.createTrackbar('U Cols', 'Control Panel', 1280, 1280, nothing)

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret:

        # Get the ROI
        l_r = cv2.getTrackbarPos('L Rows', 'Control Panel')
        u_r = cv2.getTrackbarPos('U Rows', 'Control Panel')
        l_c = cv2.getTrackbarPos('L Cols', 'Control Panel')
        u_c = cv2.getTrackbarPos('U Cols', 'Control Panel')

        roi = frame[l_r:u_r, l_c:u_c]

        # Change the ROI image to HSV channels
        hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)

        l_h = cv2.getTrackbarPos('LH', 'Control Panel')
        u_h = cv2.getTrackbarPos('UH', 'Control Panel')
        l_s = cv2.getTrackbarPos('LS', 'Control Panel')
        u_s = cv2.getTrackbarPos('US', 'Control Panel')
        l_v = cv2.getTrackbarPos('LV', 'Control Panel')
        u_v = cv2.getTrackbarPos('UV', 'Control Panel')
        low_back = np.array([l_h, l_s, l_v])
        high_back = np.array([u_h, u_s, u_v])

        # Get the mask for the background and foreground
        mask = cv2.inRange(hsv, low_back, high_back)
        mask_inv = cv2.bitwise_not(mask)

        # Get the background and foreground image
        background = cv2.bitwise_and(roi, roi, mask=mask)
        foreground = cv2.bitwise_and(roi, roi, mask=mask_inv)

        # Show the images
        cv2.imshow('Background', background)
        cv2.imshow('Foreground', foreground)
        cv2.imshow('Original', frame)

        # ESC to quite
        k = cv2.waitKey(2) & 0xFF
        if k == 27:
            break

cap.release()
cv2.destroyAllWindows()
