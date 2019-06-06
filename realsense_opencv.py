# License: Apache 2.0. See LICENSE file in root directory.
# Copyright(c) 2015-2017 Intel Corporation. All Rights Reserved.

###############################################
##      Open CV and Numpy integration        ##
###############################################

import cv2
import numpy as np
import pyrealsense2 as rs
import sys

DEVICE_ONE = '831612073761'  # Tag
DEVICE_TWO = '831612073809'  # No tag


class Realsense(object):
    def __init__(self, camera_num=1, device_id=None, depth_resolution=[640, 480], color_resolution=[640, 480]):
        """
        Initialize the RealSense Camera.

        Args:
                        - multi_camera (int, optional): number of the camera to initialize, default is 1, if greater than 1, it should be less or equal than len(device_id).
                        - device_id (list, optional): the device id to use.
                        - depth_resolution(list, optional): the depth image resolution.
                        - color_resolution(list, optional): the color image resolution.
        """

        self.devices = self.check_device()
        self.num_device = len(self.devices)

        if self.num_device == 0:
            print("No RealSense found. Please connect at least one to your PC.")
            sys.exit()

        elif camera_num < 1 or camera_num > self.num_device:
            print("The camera_num should be in range: [{},{}]".format(
                1, self.num_device))

        else:
            self.show_connected_devices()
            self.pipeline = []
            if device_id is not None:
                self.device_id = device_id
                for i in range(camera_num):
                    self.pipeline.append(rs.pipeline())

                    # Set the config for camera
                    config = rs.config()
                    config.enable_device(self.device_id[i])
                    config.enable_stream(
                        rs.stream.depth, depth_resolution[0], depth_resolution[1], rs.format.z16, 30)
                    config.enable_stream(
                        rs.stream.color, color_resolution[0], color_resolution[1], rs.format.bgr8, 30)

                    # Start streaming from camera
                    self.pipeline[i].start(config)
                    print("Initialized RealSense pipeline {}. Device ID is: {}.".format(
                        i, self.device_id[i]))
            else:
                for i in range(camera_num):
                    self.pipeline[i] = rs.pipeline()

                    # Set the config for camera
                    config = rs.config()
                    config.enable_device(self.devices[i])
                    config.enable_stream(
                        rs.stream.depth, depth_resolution[0], depth_resolution[1], rs.format.z16, 30)
                    config.enable_stream(
                        rs.stream.color, color_resolution[0], color_resolution[1], rs.format.bgr8, 30)

                    # Start streaming from camera
                    self.pipeline[i].start(config)
                    print("Initialized RealSense pipeline {}. Device ID is: {}.".format(
                        i, self.devices[i]))

    def show_connected_devices(self):
        """

        Show the connected RealSense devices.

        Args:
                        None

        Returns:
                        The number of connected RealSense devices.
        """
        print("There are %d RealSense connected in this PC. The device ID is: " %
              self.num_device)
        for i in range(self.num_device):
            print(self.devices[i])

    def check_device(self):
        """
        Check the connected RealSense devices.

        Args:
                        None

        Returns:
                        the connected RealSense devices.

        """

        ctx = rs.context()
        devices = ctx.query_devices()
        return devices

    def stop(self):
        """
        Stop the RealSense devices.

        Args:
                        None

        Returns:
                        None

        """
        try:
            for i in range(len(self.pipeline)):
                self.pipeline[i].stop()
            print("Stopped the devices successfully.")
        except:
            print("Failed to stop the devices. Please reconnect it.")

    def get_images(self):
        """
        Get the color and depth images.

        Args:
                        None

        Returns:
                        - color_images(list): all the color images from the camera
                        - depth_images(list): all the depth images from the camera
                                                                        - depth_colormap(list): all the depth colormaps from the camera
        """

        color_images = [[] for i in range(len(self.pipeline))]
        depth_images = [[] for i in range(len(self.pipeline))]
        depth_colormaps = [[] for i in range(len(self.pipeline))]
        for i in range(len(self.pipeline)):

            # Wait for a coherent pair of frames: depth and color
            frames = self.pipeline[i].wait_for_frames()
            depth_frame = frames.get_depth_frame()
            color_frame = frames.get_color_frame()
            if not depth_frame or not color_frame:
                continue

            # Convert images to numpy arrays
            depth_image = np.asanyarray(depth_frame.get_data())
            color_image = np.asanyarray(color_frame.get_data())
            # Apply colormap on depth image (image must be converted to 8-bit per pixel first)
            depth_colormap = cv2.applyColorMap(cv2.convertScaleAbs(
                depth_image, alpha=0.5), cv2.COLORMAP_JET)

            # Stack all images horizontally
            color_images[i] = color_image
            depth_images[i] = depth_image
            depth_colormaps[i] = depth_colormap

        return color_images, depth_images, depth_colormaps


if __name__ == "__main__":
    camera_num = 1
    camera = Realsense(camera_num=camera_num, device_id=[
        DEVICE_ONE, DEVICE_TWO], color_resolution=[1280, 720], depth_resolution=[1280, 720])

    try:
        while True:
            color_images, depth_images, depth_colormaps = camera.get_images()
            # print(color_images[0].shape)
            # Show images from both cameras
            for i in range(camera_num):

                cv2.namedWindow('RealSense Color, ID: ' +
                                str(i), cv2.WINDOW_NORMAL)
                cv2.imshow('RealSense Color, ID: ' + str(i), depth_images[i])

                combined_color_depth_colormap = np.hstack(
                    (color_images[i], depth_colormaps[i]))
                combined_color_depth_colormap = cv2.resize(
                    combined_color_depth_colormap, dsize=None, fx=1/2, fy=1/2)
                cv2.namedWindow('RealSense Color & Depth Colormaps, ID: ' +
                                str(i), cv2.WINDOW_NORMAL)
                cv2.imshow('RealSense Color & Depth Colormaps, ID: ' +
                           str(i), combined_color_depth_colormap)

            # Save images and depth maps from both cameras by pressing 's'
            key = cv2.waitKey(5) & 0xFF
            if key == 115:
                cv2.imwrite("./images/my_image_image.jpg", color_images[0])
                cv2.imwrite("./images/my_depth_image.jpg", depth_images[0])
                cv2.imwrite("./images/my_depth_colormap.jpg",
                            depth_colormaps[0])
                print("Save")
            elif key == ord('q') or key == 27:
                cv2.destroyAllWindows()
                break
    finally:

        # Stop streaming
        camera.stop()
