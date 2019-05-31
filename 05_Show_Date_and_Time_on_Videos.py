import datetime

import cv2

cap = cv2.VideoCapture(0)

cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:

        font = cv2.FONT_HERSHEY_SIMPLEX
        text = 'Width: ' + str(int(cap.get(3))) + \
            ' Height:' + str(int(cap.get(4)))
        datet = str(datetime.datetime.now())
        frame = cv2.putText(frame, text, (10, 50), font, 1,
                            (0, 255, 255), 2, cv2.LINE_AA)
        frame = cv2.putText(frame, datet, (10, 100), font, 1,
                            (0, 255, 255), 2, cv2.LINE_AA)
        cv2.imshow('frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
print("Closing the camera.")
cap.release()
cv2.destroyAllWindows()
