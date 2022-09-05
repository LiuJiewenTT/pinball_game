import numpy as np

import color
from gameobj import *
import corefunc
import ball
import woodhold
import border
import brick
import grid


class gamebody(gameobj):
    paper = None
    DEFAULT_SHAPE = [600, 800]
    shape = DEFAULT_SHAPE
    DEFAULT_HEIGHTCONTROL_C = 0.5
    heightControl_c = DEFAULT_HEIGHTCONTROL_C
    cpont_list = []
    cstmColorSet = None

    def __init__(self):
        # super().__init__()
        img_t = [[color.COLOR_WHITE,] * self.shape[1]] * self.shape[0]
        self.paper = np.asarray(img_t, np.uint8)
        self.setImg(self.paper)
        self.id = self.instanceCount(self.__class__)
        self.name = 'canvas'
        self.displayImg()

        self.ball = ball.ball()
        self.ball.name = 'ball'
        self.cpont_list.append(self.ball)
        self.woodhold = woodhold.woodhold()
        self.woodhold.name = 'woodhold'
        self.cpont_list.append(self.woodhold)

        self.cstmColorSet = color()

        self.more_init()

    def more_init(self):
        print(f'pos init, paper shape: {self.shape}')
        self.init_ball_pos()
        self.init_woodhold_pos()

        self.borderInit()
        # self.heightControl_c = 0.5
        self.brickInit()

    def init_ball_pos(self):
        t = self.shape
        t = [int(t[0] * 0.70), t[1]//2]
        ttl = [x - self.ball.scale//2 for x in t]   # 左上角坐标
        self.ball.setPos_hw(ttl)
        print(f'ball pos: {self.ball.getPos()}')
        # print(self.cpont_list[0].getPos()) 这是引用的，值有发生改变

    def init_woodhold_pos(self):
        t = self.shape
        t = [int(t[0] * 0.80), t[1] // 2]
        ttl = []
        for i in [0,1]:
            ttl.append(t[i] - self.woodhold.shape[i] // 2)
        self.woodhold.setPos_hw(ttl)
        print(f'woodhold pos: {self.woodhold.getPos()}')

    def borderInit(self):
        h, w = self.shape
        self.border_left = border.border([h, 10])
        self.border_right = border.border([h, 10])
        self.border_top = border.border([5, w])
        self.border_end = border.border([5, w])

        self.border_left.name = 'border_left'
        self.border_right.name = 'border_right'
        self.border_top.name = 'border_top'
        self.border_end.name = 'border_end'

        self.border_end.bordercolor = color.COLOR_RED
        self.border_end.reInit()

        # self.border_left.setPos([0, 0])
        self.border_right.setPos([0, w-10])
        # self.border_top.setPos([0, 0])
        self.border_end.setPos([h-5, 0])

        self.cpont_list.extend([self.border_left, self.border_right, self.border_top, self.border_end])

    def brickInit(self):
        space_left = [self.shape[0] - self.border_top.shape[0] - self.border_end.shape[0], self.shape[1] - self.border_left.shape[1] - self.border_right.shape[1]]
        space_avail = [ int(1.0 * space_left[0] * self.heightControl_c), space_left[1]]
        print(f'space_left: {space_left}')
        print(f'space_avail: {space_avail}')
        brickshape = brick.brick.shape
        rc = [space_avail[i] // brickshape[i] for i in [0,1]]
        print(f'rc = {rc}')
        self.grid = grid.grid(rc, brickshape)
        self.grid.name = 'grid'
        self.grid.draw()
        self.cpont_list.append(self.grid)

    def draw(self):
        img_t2 = self.paper.copy()
        for x in self.cpont_list:
            x:gameobj
            tl = x.getPos()
            img_t = x.getImg()
            img_t2 = corefunc.lapTIMG( img_t2, img_t, corefunc.TRANSPARENCY_AUTO, pos=tl)
        # self.paper = img_t2
        self.setImg(img_t2) # Refresh for displaying