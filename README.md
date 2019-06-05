# OpenCV

OpenCV is an image processing library created by Intel and later supported by Willow Garage and now maintained by Itseez. It is available on Mac, Windows, Linux. Works in C, C++, and Python.

The most important thing is that it's **Open Source** and **free**.

For more image processing basics, please check my Image_Processing_100_Questions repository:

- English Version: [Image_Processing_100_Questions](https://github.com/KuKuXia/Image_Processing_100_Questions)
- Original Japanese Version by yoyoyo-yo:
[Gasyori 100knock](https://github.com/yoyoyo-yo/Gasyori100knock)

This repository contains some code files copied from some online courses and web tutorials. I modified these files so that it's more clear and easy for beginners to learn. The original links are listed below:

1. [OpenCV Python Tutorials](https://opencv-python-tutroals.readthedocs.io/en/latest/index.html)

2. [OpenCV Python Tutorial For Beginners](https://www.youtube.com/watch?v=kdLM6AOd2vc&list=PLS1QulWo1RIa7D1O6skqDQ-JZ1GGHKK-K)

3. [Pysource](https://pysource.com/)

   

## Installation

1. Download this repository and extract it：

    ```bash
    git clone git@github.com:KuKuXia/OpenCV_for_Beginners.git
    ```

2. Download the [anaconda](https://www.anaconda.com/downloads) and install it.

3. Create a virtual environment:

    ```bash
    conda create -n CV python=3.6
    ```

4. Install the packages:

   ```bash
   cd OpenCV_for_Beginners/
   pip install -r requirements.txt
   ```

5. Open one file and enjoy your journey.

## Note

1. Python scalar operations are faster than Numpy scalar operations. So for operations including one or two elements, Python scalar is better than Numpy arrays. Numpy takes advantage when size of array is a little bit bigger.
2. Normally, OpenCV functions are faster than Numpy functions. So for same operation, OpenCV functions are preferred. But, there can be exceptions, especially when Numpy works with views instead of copies.



## Content

The fully documented files are listed below. I'm working on adding more comments to my codes.

| Name                                                         | Note                                              |
| :----------------------------------------------------------- | :------------------------------------------------ |
| [01_Basics_Read_and_Write_Image](./01_Basics_Read_and_Write_Image.py) | Read and write image                              |
| [01_Color_Spaces_in_OpenCV](./01_Color_Spaces_in_OpenCV.py)  | Using RealSense to learn the color space          |
| [02_Read_and_Write_Images_from_Camera](./02_Read_and_Write_Images_from_Camera.py) | Read and write images from a camera               |
| [03_Draw_Geometric_Shapes_on_Image](./03_Draw_Geometric_Shapes_on_Image.py) | Draw draw geometric shapes on image               |
| [04_Set_Camera_Properties](./04_Set_Camera_Properties.py)    | Set the properties of the camera                  |
| [05_Show_Date_and_Time_on_Videos](./05_Show_Date_and_Time_on_Videos.py) | Show date and time on videos                      |
| [06_Show_Pixel_Details_using_Mouse](./06_Show_Pixel_Details_using_Mouse.py) | Show pixel details by callback function           |
| [07_Draw_Lines_using_Mouse](./07_Draw_Lines_using_Mouse.py)  | Draw lines using callback function                |
| [07_Draw_Shapes_using_Mouse](./07_Draw_Shapes_using_Mouse.py) | Draw rectangle and circle using callback function |
| [08_Basic_Properties_and_Operations](./08_Basic_Properties_and_Operations.py) | Basic properties and operations on images         |
| [09_Arithmetic_Operations](./09_Arithmetic_Operations.py)    | Arithmetic operation on images                    |
| [10_Trackerbar_RGB_Chanels](./10_Trackerbar_RGB_Chanels.py)  | Learn RGB channels with trackerbar                |
| [10_Trackerbar_Switch_and _Text](./10_Trackerbar_Switch_and _Text.py) | Trackerbar with switch and text                   |
|                                                              |                                                   |

