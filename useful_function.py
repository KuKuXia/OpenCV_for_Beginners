
# Import the packages
import cv2
import numpy as np


# Select single ROI
def single_roi(im):
    # Select multiple ROI
    roi = cv2.selectROI("Image", im, 0, 0)

    # Crop image
    im_crop = im[int(roi[1]):int(roi[1] + roi[3]),
                 int(roi[0]): int(roi[0] + roi[2])]

    # Show the image
    cv2.imshow("Cropped Image", im_crop)


# Select multi ROIs
def multi_rois(im):
    # Select multiple ROI
    roi = cv2.selectROIs("Image", im, 0, 0)

    for i in range(len(roi)):
        # Crop images
        im_crop = im[int(roi[i][1]):int(roi[i][1] + roi[i][3]),
                     int(roi[i][0]): int(roi[i][0] + roi[i][2])]

        # Show the image
        cv2.imshow("Cropped Image: "+str(i), im_crop)


def combine_two_image(image1, image2, low_threshold, area=[100, 200], show_mask=False):
    """
    Add the second image to the area of the first image

    Args:
        - image1(np.array): the first image
        - image2(np.areray): the second image
        - low_threshold:(np.array) the threshold used to extract the ROI
        - area(list, optional): the area wanted to be added
        - show_mask: for debug purpose, whether to show the mask or not
    Return:
        combined_image: the combined image

    """
    shape1 = np.array(image1.shape)
    shape2 = np.array(image2.shape)
    if (shape1 >= shape2).all():
        combined_image = image1.copy()
        roi = image1[0: area[0], 0: area[1]]

        # Create af mask of ROI and create its inverse mask also
        img2gray = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
        ret, mask = cv2.threshold(img2gray, low_threshold,
                                  255, cv2.THRESH_BINARY)
        mask_inv = cv2.bitwise_not(mask)

        # Black-out the area of ROI
        image1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)

        # Take only region of logo from logo image.
        image2_fg = cv2.bitwise_and(image2, image2, mask=mask)

        # Put logo in ROI and modify the main image
        dst = cv2.add(image1_bg, image2_fg)
        combined_image[0:rows, 0:cols] = dst

        # Show the image
        if show_mask:
            cv2.imshow("ROI", roi)
            cv2.imshow("Mask", mask)
    else:
        print("The shape of the image1 are smaller than the image2.")
        return None
    return combined_image


if __name__ == "__main__":

    # Read the image
    img1 = cv2.imread('./images/messi5.jpg')
    img2 = cv2.imread('./images/opencv-logo-white.png')

    # I want to put logo on top-left corner, So I create a ROI
    rows, cols, channels = img2.shape

    # Add the second image to first image
    combined_image = combine_two_image(
        img1, img2, 12, area=[rows, cols], show_mask=False)

    # Show the image
    cv2.imshow("Image 1", img1)
    cv2.imshow("Image 2", img2)
    cv2.imshow("Combined Image", combined_image)

    # Wait until a key pressed
    cv2.waitKey(0)

    # Destroy all the windows opened before
    cv2.destroyAllWindows()
