"""
Image alignment using Enhanced Correlation Coefficient (ECC) Maximization

Original url:
https://www.learnopencv.com/image-alignment-ecc-in-opencv-c-python/

Motion models:
    - Translation
    - Euclidean
    - Affine
    - Homography

cv2.findTransformECC():
    - Read the images.
    - Convert them to grayscale.
    - Pick a motion model you want to estimate.
    - Allocate space (warp_matrix) to store the motion model.
    - Define a termination criteria that tells the algorithm when to stop.
    - Estimate the warp matrix using findTransformECC.
    - Apply the warp matrix to one of the images to align it with the other image.

"""

# Import the packages
import cv2
import numpy as np


if __name__ == '__main__':

    # Read the images to be aligned
    im1 = cv2.imread("images/alignment/image1.jpg")
    im2 = cv2.imread("images/alignment/image2.jpg")

    # Convert images to grayscale
    im1_gray = cv2.cvtColor(im1, cv2.COLOR_BGR2GRAY)
    im2_gray = cv2.cvtColor(im2, cv2.COLOR_BGR2GRAY)

    # Find size of image1
    sz = im1.shape

    # Define the motion model
    warp_mode = cv2.MOTION_EUCLIDEAN

    # Define 2x3 or 3x3 matrices and initialize the matrix to identity
    if warp_mode == cv2.MOTION_HOMOGRAPHY:
        warp_matrix = np.eye(3, 3, dtype=np.float32)
    else:
        warp_matrix = np.eye(2, 3, dtype=np.float32)

    # Specify the number of iterations.
    number_of_iterations = 5000

    # Specify the threshold of the increment
    # in the correlation coefficient between two iterations
    termination_eps = 1e-10

    # Define termination criteria
    criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT,
                number_of_iterations,  termination_eps)

    # Run the ECC algorithm. The results are stored in warp_matrix.
    (cc, warp_matrix) = cv2.findTransformECC(
        im1_gray, im2_gray, warp_matrix, warp_mode, criteria, inputMask=None, gaussFiltSize=5)

    if warp_mode == cv2.MOTION_HOMOGRAPHY:
        # Use warpPerspective for Homography
        im2_aligned = cv2.warpPerspective(
            im2, warp_matrix, (sz[1], sz[0]), flags=cv2.INTER_LINEAR + cv2.WARP_INVERSE_MAP)
    else:
        # Use warpAffine for Translation, Euclidean and Affine
        im2_aligned = cv2.warpAffine(
            im2, warp_matrix, (sz[1], sz[0]), flags=cv2.INTER_LINEAR + cv2.WARP_INVERSE_MAP)

    # Show the image
    cv2.imshow("Image 1", im1)
    cv2.imshow("Image 2", im2)
    cv2.imshow("Aligned Image 2", im2_aligned)

    # Wait until a key pressed
    cv2.waitKey(0)

    # Destroy all the windows opened before
    cv2.destroyAllWindows()
