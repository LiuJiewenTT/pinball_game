import numpy as np

from gameobj import *

class woodhold(gameobj):
    DEFAULT_HOLD_COLOR = color.COLOR_BROWN
    shape = [10, 90]
    holdcolor = DEFAULT_HOLD_COLOR
    def __init__(self):
        img_t1 = [[self.holdcolor] * self.shape[1]] * self.shape[0]
        img_t = np.asarray(img_t1, np.uint8)
        self.setImg(img_t)
        self.id = self.instanceCount(self.__class__)
        self.displayImg()
