import time
from datetime import datetime
import cv2
import numpy as np
import pandas as pd

first_frame = None
status_list = [None, None]
times = []
# Store the time values
df = pd.DataFrame(columns=["Start", "End"])
# Create the camera object
cap = cv2.VideoCapture(0)

# Read the image and process it
while(cap.isOpened()):
    ret, frame = cap.read()

    # Status at the beginning of the recording is zero as the object is not visible
    status = 0
    if ret:
        # Reading the image as gray scale image
        gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        gray_img = cv2.GaussianBlur(gray_img, (21, 21), 0)

        # This is used to store the first frame as the initial image
        if first_frame is None:
            first_frame = gray_img
            continue
        # Calculates the differences between the first frame and other frames
        delta_frame = cv2.absdiff(first_frame, gray_img)

        # Converts the difference value less than 30 to black, other wise white
        thresh_delta = cv2.threshold(
            delta_frame, 30, 255, cv2.THRESH_BINARY)[1]

        # Dilation
        kernal = np.ones((5, 5), np.uint8)
        thresh_delta = cv2.dilate(thresh_delta, None, iterations=0)

        # Define the contour area. Basically, add the borders
        contours, _ = cv2.findContours(
            thresh_delta.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        for contour in contours:
            # Remove the noises and shadows. Basically, it will keep only the white part, which has greater than 10000 pixels
            if cv2.contourArea(contour) < 5000:
                continue

            # Status is 1 when the object is being detected
            status = 1
            # print(cv2.contourArea(contour))
            # Create a rectangular box around the object in the frame
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # List of status of every frame
        status_list.append(status)
        status_list = status_list[-2:]

        # Record datetime in a list when change occurs
        if status_list[-1] == 1 and status_list[-2] == 0:
            times.append(datetime.now())
        if status_list[-1] == 0 and status_list[-2] == 1:
            times.append(datetime.now())

    if (cv2.waitKey(1) & 0xFF) == ord('q'):
        break

    cv2.imshow('Original', frame)
    cv2.imshow('Gray', gray_img)
    cv2.imshow('Difference', delta_frame)
    cv2.imshow('Thresh', thresh_delta)

print(status_list)
print(times)
# Store time values in a DataFrame
for i in range(0, len(times)-1, 2):
    df = df.append(
        {"Start": times[i], "End": times[i + 1]}, ignore_index=True)
# Write the DataFrame to a csv file
df.to_csv("Times.csv")
cap.release()
cv2.destroyAllWindows()
