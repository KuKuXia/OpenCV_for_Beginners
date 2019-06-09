import cv2
import numpy as np

from utilities import Keyboard


if __name__ == "__main__":
    keyboard = Keyboard()
    for i in range(15):
        if i == 5:
            light = True
        else:
            light = False
        keyboard.letter(i, light)
    keyboard.show_keyboard()

    cv2.waitKey(0)
    cv2.destroyAllWindows()
