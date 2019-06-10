"""
Exposure Fusion 
Please download the images from the original url into the ./images/Exposure_Fusion/ folder:
https://www.learnopencv.com/exposure-fusion-using-opencv-cpp-python/

    - It is a method for combining images taken with different exposure settings into one image that looks like a tone mapped High Dynamic Range (HDR) image.
    - It computes the desired image by keeping only the “best” parts in the multi-exposure image sequence.
"""

# Import the packages
import cv2
import numpy as np
import sys

# Read images


def readImages():

    filenames = [
        "images/Exposure_Fusion/memorial0061.jpg",
        "images/Exposure_Fusion/memorial0062.jpg",
        "images/Exposure_Fusion/memorial0063.jpg",
        "images/Exposure_Fusion/memorial0064.jpg",
        "images/Exposure_Fusion/memorial0065.jpg",
        "images/Exposure_Fusion/memorial0066.jpg",
        "images/Exposure_Fusion/memorial0067.jpg",
        "images/Exposure_Fusion/memorial0068.jpg",
        "images/Exposure_Fusion/memorial0069.jpg",
        "images/Exposure_Fusion/memorial0070.jpg",
        "images/Exposure_Fusion/memorial0071.jpg",
        "images/Exposure_Fusion/memorial0072.jpg",
        "images/Exposure_Fusion/memorial0073.jpg",
        "images/Exposure_Fusion/memorial0074.jpg",
        "images/Exposure_Fusion/memorial0075.jpg",
        "images/Exposure_Fusion/memorial0076.jpg"
    ]

    images = []
    for filename in filenames:
        im = cv2.imread(filename)
        images.append(im)

    return images


if __name__ == '__main__':

        # Read images
    print("Reading images ... ")

    if len(sys.argv) > 1:
        # Read images from the command line
        images = []
        for filename in sys.argv[1:]:
            im = cv2.imread(filename)
            images.append(im)
        needsAlignment = False
    else:
        # Read example images
        images = readImages()
        needsAlignment = False

    # Align input images
    if needsAlignment:
        print("Aligning images ... ")
        alignMTB = cv2.createAlignMTB()
        alignMTB.process(images, images)
    else:
        print("Skipping alignment ... ")

    # Merge using Exposure Fusion
    print("Merging using Exposure Fusion ... ")
    mergeMertens = cv2.createMergeMertens()
    exposureFusion = mergeMertens.process(images)

    # Show the image
    cv2.imshow("Exposure Fusion Image", exposureFusion)

    # Save output image
    print("Saving output ... exposure-fusion.jpg")
    cv2.imwrite("./images/Exposure_Fusion/exposure-fusion.jpg",
                exposureFusion * 255)

    # Wait until a key pressed
    cv2.waitKey(0)
    # Destroy all the windows opened before
    cv2.destroyAllWindows()
