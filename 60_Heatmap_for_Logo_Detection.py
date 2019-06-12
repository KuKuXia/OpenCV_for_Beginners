"""
Heatmap for logo detection

Download the data from the original url:
https://www.learnopencv.com/heatmap-for-logo-detection-using-opencv-python/

Copyright 2018 Orpix Inc.

This script will iterate through a file "labels.txt" which specifies the images and object annotations to
compute an object exposure heatmap saved as heatmap.png in the location of this script.
It will highlight the labels on each annotated image and save a copy in the output folder.
"""

# Import the packages
import matplotlib.pyplot as plt
import os
import os.path

# we require numpy, opencv, and matplotlib
import numpy as np
import cv2
import matplotlib

# this disables GUI windows from popping up
matplotlib.use('Agg')


# set working directory to location of script:
abspath = os.path.abspath(__file__)
dir_name = os.path.dirname(abspath)
os.chdir(dir_name)

# helper function that parses the line
# returns the frame, along with an array of array of point pairs representing detected logos


def parse_line(line):

    # format of a line is space delineated in the following format
    #
    # image_file_path number_of_labels x1 y1 x2 y2 x3 y3 x4 y4 x1 y1 x2 y2 x3 y3 x4 y4 ... etc
    #
    # Note: We use 4 x,y coordinates to denote a detection label
    # since Orpix logo detection outputs a quadrilateral as opposed to a rectangle
    label_data = line.split(' ')

    frame_path = label_data[0]
    label_count = int(label_data[1])

    # getting points only, casting to int
    pts = label_data[2:]
    pts = [int(x) for x in pts]

    labels = []
    for i in range(label_count):

        # get the 8 points for the current label
        label_pts = pts[i*8:i*8+8]

        # reshape to array of 4 tuples
        pt_pairs = []
        for point_index in range(0, 8, 2):
            pt_pairs.append([label_pts[point_index], label_pts[point_index+1]])

        #a dd this label to the list of labels we return
        pt_pairs = np.array(pt_pairs)
        labels.append(pt_pairs)

    return frame_path, np.array(labels)

# help function to highlight the labels in each input frame
# by interpolating the background with white
def highlight_labels(img, labels, mask_image=None):

    # create a copy of the image so we can draw on it
    image_copy = img.copy()

    # draw a quadrilateral for each label in red
    cv2.polylines(image_copy, labels, True, (0, 0, 255), thickness=2)

    # a mask needs to be created from the labels so we can properly highlight.
    # if the mask isn't passed in, we create it
    if type(mask_image) == type(None):
        mask_image = np.zeros(image_copy.shape, dtype=np.float)
        for label in labels:
            #this sets all pixels inside the label to 1
            cv2.fillConvexPoly(mask_image, label, (1))

    # create a rgb version of the mask by setting each channel to the mask we created
    mask_image = (mask_image > 0).astype(np.uint8)
    mask_rgb = np.zeros(image_copy.shape, np.uint8)
    mask_rgb[:, :, 0] = mask_image
    mask_rgb[:, :, 1] = mask_image
    mask_rgb[:, :, 2] = mask_image

    # interpolate image with white using a weighted sum
    background_image = .5*255*np.ones(image_copy.shape, np.float) + .5*image_copy.astype(np.float)
    # mask out the background
    background_image = (1-mask_rgb)*background_image
    # cast to uint8 image
    background_image = np.round(background_image).astype(np.uint8)

    #g et foreground unchanged
    foreground_image = mask_rgb*image_copy

    # add white tinted background with unchanged foreground
    image_copy = background_image + foreground_image.astype(np.uint8)

    return image_copy


def main():

    # keeps track of exposure time per pixel.  Accumulates for each image
    accumulated_exposures = None

    # frames were sampled at one second per frame.  If you sampled frames from a video at a different rate, change this value
    # if you sampled frames at 10 frames per second, this value would be 0.1
    seconds_per_frame = 1.0

    # we open the labels file and will iterate through each line.
    # each line contains a reference to the image and the corresponding polygon lables (4 points per label)
    # each frame in the labels file was extracted from one video
    with open('./images/Example_Heatmap_Data/labels.txt') as f:
        lines = f.readlines()
        for line in lines:

            #parse the line using helper function
            frame_path, labels = parse_line(line)

            print("processing %s" % frame_path)

            # load the image
            frame = cv2.imread('./images/Example_Heatmap_Data/' + frame_path)

            # this is where the highlighted images will go
            if not os.path.exists('./images/Example_Heatmap_Data/output'):
                os.mkdir('./images/Example_Heatmap_Data/output')

            # if the heatmap is None we create it with same size as frame, single channel
            if type(accumulated_exposures) == type(None):
                accumulated_exposures = np.zeros(
                    (frame.shape[0], frame.shape[1]), dtype=np.float)

            # we create a mask where all pixels inside each label are set to number of seconds per frame that the video was sampled at
            # so as we accumulate the exposure heatmap counts, each pixel contained inside a label contributes the seconds_per_frame
            # to the overall accumulated exposure values
            mask_image = np.zeros(accumulated_exposures.shape, dtype=np.float)
            for label in labels:
                cv2.fillConvexPoly(mask_image, label, (seconds_per_frame))

            # highlight the labels on the image and save.
            # comment out the 2 lines below if you only want to compute the heatmap
            highlighted_image = highlight_labels(frame, labels, mask_image)
            cv2.imwrite('./images/Example_Heatmap_Data/output/%s' %
                        os.path.basename(frame_path), highlighted_image)

            # accumulate the heatmap object exposure time
            accumulated_exposures = accumulated_exposures + mask_image

    #
    # create final heatmap using matplotlib
    #

    data = np.array(accumulated_exposures)
    # create the figure
    fig, axis = plt.subplots()
    # set the colormap - there are many options for colormaps - see documentation
    # we will use cm.jet
    hm = axis.pcolor(data, cmap=plt.cm.jet)
    # set axis ranges
    axis.set(xlim=[0, data.shape[1]], ylim=[0, data.shape[0]], aspect=1)
    # need to invert coordinate for images
    axis.invert_yaxis()
    # remove the ticks
    axis.set_xticks([])
    axis.set_yticks([])

    # fit the colorbar to the height
    shrink_scale = 1.0
    aspect = data.shape[0]/float(data.shape[1])
    if aspect < 1.0:
        shrink_scale = aspect
    clb = plt.colorbar(hm, shrink=shrink_scale)
    # set title
    clb.ax.set_title('Exposure (seconds)', fontsize=10)
    # saves image to same directory that the script is located in (our working directory)
    plt.savefig('./images/Example_Heatmap_Data/heatmap.png', bbox_inches='tight')
    # close objects
    plt.close('all')


if __name__ == '__main__':

    main()
