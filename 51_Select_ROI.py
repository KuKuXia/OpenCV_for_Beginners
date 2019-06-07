"""
Select region of interest
"""

# Import the packages
import numpy as np
import cv2


# Select single ROI
def single_roi(im):
    # Select multiple ROI
    roi = cv2.selectROI("Image", im, 0, 0)

    # Crop images
    im_crop = im[int(roi[1]):int(roi[1] + roi[3]),
                 int(roi[0]): int(roi[0] + roi[2])]

    # Show the image
    cv2.imshow("Cropped Image", im_crop)


# Select multi ROIs
def multi_rois(im):
    # Select multiple ROI
    roi = cv2.selectROIs("Image", im, 0, 0)

    for i in range(len(roi)):
        # Crop image
        im_crop = im[int(roi[i][1]):int(roi[i][1] + roi[i][3]),
                     int(roi[i][0]): int(roi[i][0] + roi[i][2])]

        # Show the image
        cv2.imshow("Cropped Image: "+str(i), im_crop)


if __name__ == "__main__":
    # Read the image
    im = cv2.imread("./images/robot.jpg")

    # Single ROI
    # single_roi(im)

    # Multi ROIs
    multi_rois(im)

    # Wait until a key pressed
    cv2.waitKey(0)

    # Destroy all the windows opened before
    cv2.destroyAllWindows()
