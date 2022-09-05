from gameobj import *

class border(gameobj):
    DEFAULT_BORDER_COLOR = color.COLOR_BLACK
    shape = [10, 90]
    bordercolor = DEFAULT_BORDER_COLOR
    def __init__(self, borderShape, ifAutoSetID=True):
        self.shape = borderShape
        img_t1 = [[self.bordercolor] * self.shape[1]] * self.shape[0]
        img_t = np.asarray(img_t1, np.uint8)
        self.setImg(img_t)
        if ifAutoSetID is True:
            self.id = self.instanceCount(self.__class__)
        self.displayImg()

    def reInit(self):
        self.__init__(self.shape, ifAutoSetID=False)