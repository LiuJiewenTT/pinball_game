import numpy as np

from gameobj import *

class ball(gameobj):
    DEFAULT_BALL_COLOR = color.COLOR_RED
    scale = 20
    ballcolor = DEFAULT_BALL_COLOR
    def __init__(self):
        # self.ballcolor = self.DEFAULT_BALL_COLOR
        img_t1 = [[color.TRANSPARENT_WHITE] * self.scale,] * self.scale
        img_t = np.asarray(img_t1, np.uint8)
        # img_t = np.asmatrix(img_t1, np.uint8) 图片是三维的，因为每个像素颜色一个维度，矩阵是二维的，所以此处不能用
        cv.circle(img_t, [self.scale//2, ]*2, self.scale//2 - 1, self.ballcolor, -1, cv.LINE_AA)
        self.setImg(img_t)
        self.id = self.instanceCount(self.__class__)
        self.displayImg()
