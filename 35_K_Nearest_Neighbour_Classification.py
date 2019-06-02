import cv2
import numpy as np


def mouse_pos(event, x, y, flags, params):
    global color, new_element
    if event == cv2.EVENT_LBUTTONDOWN:
        if color == "b":
            blue_squares.append([x, y])
        elif color == "r":
            red_squares.append([x, y])
        else:
            new_element = [x, y]


# Create Window and Set mouse events
cv2.namedWindow("Frame", cv2.WINDOW_NORMAL)
cv2.setMouseCallback("Frame", mouse_pos)

# Create an empty image
img = np.zeros([500, 700, 3], dtype=np.uint8)
img[:] = (255, 255, 255)


# Load KNN algorithm
knn = cv2.ml.KNearest_create()

# Store all the elements
blue_squares = []
red_squares = []
new_element = []
new_comer = False
color = "b"

# Text Data
font = cv2.FONT_HERSHEY_SIMPLEX
result = "None"
k = 1
neighbors = "None"
dist = "None"

while True:
    img[:] = (255, 255, 255)

    cv2.putText(img, "Result: " + str(result),
                (10, 400), font, 1, (0, 0, 0), 2)
    cv2.putText(img, "K: " + str(k), (10, 440), font, 1, (0, 0, 0), 2)
    cv2.putText(img, "Neighbors: " + str(neighbors),
                (10, 470), font, 0.5, (0, 0, 0), 1)
    cv2.putText(img, "Distance: " + str(dist),
                (10, 490), font, 0.5, (0, 0, 0), 1)

    cv2.putText(img, "Commands:", (400, 360), font, 0.5, (0, 0, 0), 1)
    cv2.putText(img, "B: select blu square",
                (400, 380), font, 0.5, (0, 0, 0), 1)
    cv2.putText(img, "R: select red square",
                (400, 400), font, 0.5, (0, 0, 0), 1)
    cv2.putText(img, "G: select target square",
                (400, 420), font, 0.5, (0, 0, 0), 1)
    cv2.putText(img, "1, 3, 5, 7, 9: change K",
                (400, 440), font, 0.5, (0, 0, 0), 1)
    cv2.putText(img, "C: calculate result",
                (400, 460), font, 0.5, (0, 0, 0), 1)
    cv2.putText(img, "D: delete everything",
                (400, 480), font, 0.5, (0, 0, 0), 1)

    # Show the Squares
    for s in blue_squares:
        cv2.rectangle(img, (s[0] - 5, s[1] - 5),
                      (s[0] + 5, s[1] + 5), (255, 0, 0), -1)
    for s in red_squares:
        cv2.rectangle(img, (s[0] - 5, s[1] - 5),
                      (s[0] + 5, s[1] + 5), (0, 0, 255), -1)
    if new_element != []:
        cv2.rectangle(img, (new_element[0] - 5, new_element[1] - 5),
                      (new_element[0] + 5, new_element[1] + 5), (0, 255, 0), -1)

    # Create element to show

    cv2.imshow("Frame", img)

    # Key events to break the loop and to select the color of the squares
    key = cv2.waitKey(25)
    if key == 27:
        break
    elif key == ord("b"):
        color = "b"
    elif key == ord("r"):
        color = "r"
    elif key == ord("g"):
        color = "g"
        new_comer = True
    elif key == ord("1"):
        k = 1
    elif key == ord("2"):
        k = 2
    elif key == ord("3"):
        k = 3
    elif key == ord("4"):
        k = 4
    elif key == ord("5"):
        k = 5
    elif key == ord("6"):
        k = 6
    elif key == ord("7"):
        k = 7
    elif key == ord("8"):
        k = 8
    elif key == ord("9"):
        k = 9
    elif key == ord("d"):
        blue_squares = []
        red_squares = []
        new_element = []
    elif key == ord("c"):
        train_data = np.array(blue_squares + red_squares, dtype=np.float32)
        blue_responses = np.zeros(len(blue_squares), dtype=np.float32)
        red_respones = np.ones(len(red_squares), dtype=np.float32)
        responses = np.concatenate((blue_responses, red_respones))

        knn.train(train_data, cv2.ml.ROW_SAMPLE, responses)

        if new_comer:
            green_square = np.array([new_element], dtype=np.float32)

            ret, results, neighbors, dist = knn.findNearest(green_square, k)

            print(results[0][0])
            if results[0][0] > 0:
                result = "Red"
            else:
                result = "Blue"

cv2.destroyAllWindows()
