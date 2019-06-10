"""
High dynamic range
Original url:
https://www.learnopencv.com/high-dynamic-range-hdr-imaging-using-opencv-cpp-python/

The process of combining different images of the same scene acquired under different exposure settings is called High Dynamic Range (HDR) imaging.

Tone Mapping:
    The process of converting a High Dynamic Range (HDR) image to an 8-bit per channel image while preserving as much detail as possible is called Tone mapping.
    Four Functions:
        - Drago Tonemap
        - Durand Tonemap
        - Reinhard Tonemap
        - Mantiuk Tonemap

Since cv2.createTonemapDurand has moved into opencv_contrib under NONFREE build flag in OpenCV 4, you need to change the virtual environment:
pip uninstall opencv-contrib-python
pip uninstall opencv-python
pip install opencv-contrib-python==3.3.0.10
pip install opencv-python==3.4.2.16

"""

# Import the packages
import cv2
import numpy as np


def readImagesAndTimes():

    times = np.array([1/30.0, 0.25, 2.5, 15.0], dtype=np.float32)

    filenames = ["./images/HDR/img_0.033.jpg", "./images/HDR/img_0.25.jpg",
                 "./images/HDR/img_2.5.jpg", "./images/HDR/img_15.jpg"]
    images = []
    for filename in filenames:
        im = cv2.imread(filename)
        images.append(im)

    return images, times


if __name__ == '__main__':
    # Read images and exposure times
    print("Reading images ... ")

    images, times = readImagesAndTimes()

    # Align input images
    print("Aligning images ... ")
    alignMTB = cv2.createAlignMTB()
    alignMTB.process(images, images)

    # Obtain Camera Response Function (CRF)
    print("Calculating Camera Response Function (CRF) ... ")
    calibrateDebevec = cv2.createCalibrateDebevec()
    responseDebevec = calibrateDebevec.process(images, times)

    # Merge images into an HDR linear image
    print("Merging images into one HDR image ... ")
    mergeDebevec = cv2.createMergeDebevec()
    hdrDebevec = mergeDebevec.process(images, times, responseDebevec)
    # Save HDR image.
    cv2.imwrite("./images/HDR/hdrDebevec.hdr", hdrDebevec)
    print("saved hdrDebevec.hdr ")

    # Tonemap using Drago's method to obtain 24-bit color image
    print("Tonemaping using Drago's method ... ")
    tonemapDrago = cv2.createTonemapDrago(1.0, 0.7)
    ldrDrago = tonemapDrago.process(hdrDebevec)
    # The final output is multiplied by 3 just because it gave the most pleasing results.
    ldrDrago = 3 * ldrDrago  
    cv2.imwrite("./images/HDR/ldr-Drago.jpg", ldrDrago * 255)
    print("saved ldr-Drago.jpg")

    # Tonemap using Durand's method obtain 24-bit color image
    print("Tonemaping using Durand's method ... ")
    tonemapDurand = cv2.createTonemapDurand(1.5, 4, 1.0, 1, 1)
    ldrDurand = tonemapDurand.process(hdrDebevec)
    ldrDurand = 3 * ldrDurand
    cv2.imwrite("./images/HDR/ldr-Durand.jpg", ldrDurand * 255)
    print("saved ldr-Durand.jpg")

    # Tonemap using Reinhard's method to obtain 24-bit color image
    print("Tonemaping using Reinhard's method ... ")
    tonemapReinhard = cv2.createTonemapReinhard(1.5, 0, 0, 0)
    ldrReinhard = tonemapReinhard.process(hdrDebevec)
    cv2.imwrite("./images/HDR/ldr-Reinhard.jpg", ldrReinhard * 255)
    print("saved ldr-Reinhard.jpg")

    # Tonemap using Mantiuk's method to obtain 24-bit color image
    print("Tonemaping using Mantiuk's method ... ")
    tonemapMantiuk = cv2.createTonemapMantiuk(2.2, 0.85, 1.2)
    ldrMantiuk = tonemapMantiuk.process(hdrDebevec)
    ldrMantiuk = 3 * ldrMantiuk
    cv2.imwrite("./images/HDR/ldr-Mantiuk.jpg", ldrMantiuk * 255)
    print("saved ldr-Mantiuk.jpg")
