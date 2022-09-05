from gameobj import *

class brick(gameobj):
    DEFAULT_BRICK_COLOR = color.COLOR_BROWN
    DEFAULT_OUTLINE_COLOR = color.COLOR_GREY
    shape = [20, 70]
    brickcolor = DEFAULT_BRICK_COLOR
    outlinecolor = DEFAULT_OUTLINE_COLOR
    def __init__(self):
        img_t1 = [[self.brickcolor] * self.shape[1]] * self.shape[0]
        img_t = np.asarray(img_t1, np.uint8)
        cv.rectangle(img_t, [0, 0], [x-1 for x in self.shape], self.outlinecolor, 2, cv.LINE_AA)
        self.setImg(img_t)
        self.id = self.instanceCount(self.__class__)
        self.displayImg()