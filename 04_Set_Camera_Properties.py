"""
Set the properties of the camera

Check this link for all properties:
https://docs.opencv.org/2.4/modules/highgui/doc/reading_and_writing_images_and_video.html#videocapture-get
"""

# Import the packages
import cv2

# Register the camera
cap = cv2.VideoCapture(0)

# Show the frame properties
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Set the camera properties
cap.set(3, 1280)
cap.set(4, 720)

print(cap.get(3))
print(cap.get(4))

while (cap.isOpened()):
    # Read the frame
    ret, frame = cap.read()
    if ret == True:

        # Change the frame color space: BGR -> GRAY
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Show the frame
        cv2.imshow('frame', gray)

        # Wait until a key pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
# Destroy all the windows opened before
cv2.destroyAllWindows()
