"""
Alpha Blending
Original url:
https://www.learnopencv.com/alpha-blending-using-opencv-cpp-python/

Alpha blending is the process of overlaying a foreground image with transparency over a background image. The transparency is often the fourth channel of an image ( e.g. in a transparent PNG), but it can also be a separate image. This transparency mask is often called the alpha mask or the alpha matte.

 The value of \\alpha used in the equation is actually the pixel value in the alpha mask divided by 255. So, in the equation below, 0 \leq \alpha \leq 1

I = \\alpha F + (1 - \\alpha) B

From the equation above, you can make the following observations.

When \\alpha = 0, the output pixel color is the background.
When \\alpha = 1, the output pixel color is simply the foreground.
When 0 < \\alpha < 1 the output pixel color is a mix of the background and the foreground. For realistic blending, the boundary of the alpha mask usually has pixels that are between 0 and 1.

"""

# Import the packages
import cv2

# Read the foreground image with alpha channel
# foreGroundImage = cv2.imread("./images/foreGroundAsset.png", -1)
foreGroundImage = cv2.imread("./images/foreGroundAssetLarge.png", -1)

# Split png foreground image
b, g, r, a = cv2.split(foreGroundImage)

# Save the foreground RGB content into a single object
foreground = cv2.merge((b, g, r))

# Save the alpha information into a single Mat
alpha = cv2.merge((a, a, a))

# Read background image
# background = cv2.imread("./images/backGround.jpg")
background = cv2.imread("./images/backGroundLarge.jpg")

# Convert uint8 to float
foreground = foreground.astype(float)
background = background.astype(float)
alpha = alpha.astype(float)/255

# Perform alpha blending
foreground = cv2.multiply(alpha, foreground)
background = cv2.multiply(1.0 - alpha, background)
outImage = cv2.add(foreground, background)

# Show the image
cv2.imshow("Blended Image", outImage / 255)

# Wait until a key pressed
cv2.waitKey(0)

# Destroy all the windows opened before
cv2.destroyAllWindows()
