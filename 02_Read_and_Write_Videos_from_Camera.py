"""
Read images from a camera
Check this wiki for FOURCC: https://www.wikiwand.com/en/FourCC
"""

# import the package
import cv2

# Register the camera object
cap = cv2.VideoCapture(0)

# Print the video frame properties
print("Width: ", cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print("Height: ", cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Create the video writer
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('./images/out.avi', fourcc, 20.0, (640, 480))

while (cap.isOpened()):
    # Capture frame-by-frame
    ret, frame = cap.read()

    if ret:

        # Change the image color space, BGR -> GRAY
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Show the frame
        cv2.imshow('frame', gray)

        # Write the frame to the video writer
        out.write(frame)

        # Wait 1 ms, press q to quit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# When everything done, release the capture
cap.release()

# Release the video writer object.
out.release()

# Destory all the windows
cv2.destroyAllWindows()
