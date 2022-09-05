import numpy as np

import corefunc
from gameobj import *

class grid(gameobj):
    rc = []
    cpont_list = []
    cover_cpont_list = []
    cellShape = []
    shape = []

    def __init__(self, rc=[1,1], cellShape=[1,1]):
        self.cellShape = cellShape
        self.createBlankCellObj()
        self.setRC(rc)
        # self.cover_cpont_list.append(self.img)  # Now is None, just taking the position for latter object.
        self.id = self.instanceCount(self.__class__)

    def createBlankCellObj(self):
        try:
            grid.blankGameobj = grid.blankGameobj
            return
        except AttributeError as e:
            print(e)
            print('Now Create grid.blankGameobj')
        grid.blankGameobj = gameobj()
        grid.blankGameobj.name = 'grid.blankGameobj'
        grid.blankGameobj.id = 0
        img_t1 = [[color.TRANSPARENT_WHITE] * self.cellShape[1]] * self.cellShape[0]
        img_t = np.asarray(img_t1, np.uint8)
        grid.blankGameobj.setImg(img_t)

    def setRC(self, rc):
        self.rc = rc
        try:
            obj = grid.blankGameobj
        except AttributeError as e:
            print(e)
            print('Now run createBlankCellObj()')
            self.createBlankCellObj()
            obj = grid.blankGameobj
        self.cpont_list = [[obj] * rc[1]] * rc[0]

    def getRC(self):
        return self.rc

    def getCpont(self, r, c):
        ret = None
        try:
            ret = self.cpont_list[r][c]
        except IndexError as e:
            print(e)
            print(f'rc index{r, c} is out of range.')
        return ret

    def setCpont(self, obj:gameobj, r, c):
        if 0 <= r <= self.rc[0]:
            pass
        else:
            print('Row index is out of the permitted range')
        if 0 <= c <= self.rc[1]:
            pass
        else:
            print('Column index is out of the permitted range')
        try:
            self.cpont_list[r][c] = obj
        except Exception as e:
            print(e)
            print('This Exception occurs in class grid.')

    def CombineImg(self):
        h, w = self.getShape()
        cs_h, cs_w = self.cellShape
        r, c = self.rc
        img_t1 = [[color.TRANSPARENT_WHITE] * w] * h
        img_t = np.asarray(img_t1, np.uint8)
        # Here is a better draw method. But it is exclusive.
        for j in range(0, r):
            for i in range(0, c):
                cell = self.cpont_list[j][i].getImg()
                for y1 in range(0, cs_h):
                    y = y1 + j * cs_h
                    for x1 in range(0, cs_w):
                        x = x1 + i * cs_w
                        img_t[y][x] = cell[y1][x1]
        self.setImgRaw(img_t)

    def calcShape(self):
        cs_h, cs_w = self.cellShape
        h = cs_h * self.rc[0]
        w = cs_w * self.rc[1]
        self.shape = [h, w]
        return [h, w]

    # Override that of class gameobj
    def getShape_hw(self):
        if self.shape == []:
            self.calcShape()
        return self.shape

    def getImg(self):
        if self.img is None:
            print('grid, self.img is None')
            self.CombineImg()
            self.draw()
        return self.img

    def getImgRaw(self):
        try:
            if self.imgRaw is None:
                self.CombineImg()
        except AttributeError as e:
            print(e)
            print(f'Does not exist imgRaw in grid, now create')
            self.CombineImg()
        return self.imgRaw

    def draw(self):
        img_t2 = self.getImgRaw().copy()
        if self.cover_cpont_list is not []:
            for x in self.cover_cpont_list:
                print(f'grid, cover_cpont_list, x: {type(x)}')
                x:gameobj
                tl = x.getPos()
                img_t = x.getImg()
                # img_t2 = corefunc.lapTIMG( img_t2, img_t, corefunc.TRANSPARENCY_AUTO, pos=tl)
                corefunc.simpleLap(img_t2, img_t, pos=tl)
        self.setImg(img_t2) # Refresh for displaying

    def RefreshImg(self):
        self.CombineImg()  # get imgRaw
        self.draw()  # get img

    def getRefreshedImg(self):
        self.RefreshImg()
        return self.img

    # def setImg(self, img_r=None):
    #     raise AttributeError('Cannot set img for class grid.')
    #
    # def setImgRaw(self, imgRaw=None):
    #     raise AttributeError('Cannot set imgRaw for class grid.')

    def getCpontList(self):
        return self.cpont_list

    def setCpontList(self, cpont_list,ifChangeRC=False):
        cpont_list:list
        Valid = False
        errorr = cpont_list.__len__()
        errorc = -1
        ercidx = -1
        if cpont_list.__len__() == self.rc[0]:
            Valid = True
            for i in range(0, cpont_list.__len__()):
                if cpont_list[i].__len__() == self.rc[1]:
                    pass
                else:
                    Valid = False
                    errorc = cpont_list[i].__len__()
                    ercidx = i
                    break
        if ifChangeRC is False:
            if Valid is False:
                if ercidx != 0:
                    raise IndexError(f'Shape of list is not acceptable: Require {self.rc} while {errorr, errorc} founded. Array length varies at row {ercidx}')
                else:
                    raise IndexError(f'Shape of list is not acceptable: Require {self.rc} while {errorr, errorc} founded.')
            else:
                self.cpont_list = cpont_list
        else:
            self.cpont_list = cpont_list
            self.setRC([errorr, errorc])

    # No CellShape Check So Far

    def getCoverCpontList(self):
        return self.cover_cpont_list
        # return self.cover_cpont_list[1:]

    def setCoverCpontList(self, coverCpontList):
        self.cover_cpont_list = coverCpontList
        # self.cover_cpont_list = [self.getImg()]
        # self.cover_cpont_list.extend(coverCpontList)
