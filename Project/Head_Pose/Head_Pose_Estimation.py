"""
Head Pose Estimation
Original url:
https://www.learnopencv.com/head-pose-estimation-using-opencv-and-dlib/

A 3D rigid object has only two kinds of motions with respect to a camera.

Translation : Moving the camera from its current 3D location (X, Y, Z) to a new 3D location (X', Y', Z') is called translation. As you can see translation has 3 degrees of freedom — you can move in the X, Y or Z direction. Translation is represented by a vector \mathbf{t} which is equal to ( X' - X, Y' - Y, Z' - Z ).
Rotation : You can also rotate the camera about the X, Y and Z axes. A rotation, therefore, also has three degrees of freedom. There are many ways of representing rotation. You can represent it using Euler angles ( roll, pitch and yaw ), a 3\times3 rotation matrix, or a direction of rotation (i.e. axis ) and angle.

In OpenCV the function 
    - solvePnP 
    - solvePnPRansac 
can be used to estimate pose.
"""

# Import the packages
import cv2
import numpy as np

# Read Image
im = cv2.imread("../../images/headPose.jpg")
size = im.shape

# 2D image points. If you change the image, you need to change vector
image_points = np.array([
    (359, 391),     # Nose tip
    (399, 561),     # Chin
    (337, 297),     # Left eye left corner
    (513, 301),     # Right eye right corne
    (345, 465),     # Left Mouth corner
    (453, 469)      # Right mouth corner
], dtype="double")

# 3D model points.
model_points = np.array([
    (0.0, 0.0, 0.0),             # Nose tip
    (0.0, -330.0, -65.0),        # Chin
    (-225.0, 170.0, -135.0),     # Left eye left corner
    # Right eye right corner
    (225.0, 170.0, -135.0),
    (-150.0, -150.0, -125.0),    # Left Mouth corner
    (150.0, -150.0, -125.0)      # Right mouth corner

])


# Camera internals
focal_length = size[1]
center = (size[1]/2, size[0]/2)
camera_matrix = np.array(
    [[focal_length, 0, center[0]],
     [0, focal_length, center[1]],
     [0, 0, 1]], dtype="double"
)

print("Camera Matrix :\n {0}".format(camera_matrix))

dist_coeffs = np.zeros((4, 1))  # Assuming no lens distortion
(success, rotation_vector, translation_vector) = cv2.solvePnP(model_points,
                                                              image_points, camera_matrix, dist_coeffs, flags=cv2.SOLVEPNP_ITERATIVE)

print("Rotation Vector:\n {0}".format(rotation_vector))
print("Translation Vector:\n {0}".format(translation_vector))


# Project a 3D point (0, 0, 1000.0) onto the image plane.
# We use this to draw a line sticking out of the nose


(nose_end_point2D, jacobian) = cv2.projectPoints(np.array(
    [(0.0, 0.0, 1000.0)]), rotation_vector, translation_vector, camera_matrix, dist_coeffs)

for p in image_points:
    cv2.circle(im, (int(p[0]), int(p[1])), 3, (0, 0, 255), -1)


p1 = (int(image_points[0][0]), int(image_points[0][1]))
p2 = (int(nose_end_point2D[0][0][0]), int(nose_end_point2D[0][0][1]))

cv2.line(im, p1, p2, (255, 0, 0), 2)


# Show the image
cv2.imshow("Output", im)

# Wait until a key pressed
cv2.waitKey(0)

# Destroy all the windows opened before
cv2.destroyAllWindows()
