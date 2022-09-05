import numpy as np
import cv2.cv2 as cv
from color import *

class gameobj:
    id = None
    name = None
    img = None
    pos_topleft = [0, 0]
    def __init__(self):
        pass

    def getShape_hw(self):
        return self.img.shape[:2]
    def getShape_wh(self):
        return self.getShape_hw()[::-1]
    def getShape(self):
        return self.getShape_hw()
    def getPos_hw(self):
        return self.pos_topleft
    def getPos_wh(self):
        return self.getShape_hw()[::-1]
    def getPos(self):
        return self.getPos_hw()
    def getImg(self):
        return self.img
    def getImgRaw(self):
        return self.imgRaw

    def setImg(self, img_r):
        self.img = img_r
    def setImgRaw(self, imgRaw):
        self.imgRaw = imgRaw
    def setPos_hw(self, pos_pair_hw):
        self.pos_topleft = pos_pair_hw
    def setPos_wh(self, pos_pair_wh):
        self.setPos_hw(pos_pair_wh[::-1])
    def setPos(self, pos_pair_hw):
        return self.setPos_hw(pos_pair_hw)

    def displayImg(self, t=0):
        if self.img is None:
            print("no img")
            return
        cv.imshow(f"obj:{self.name}, id:{self.id}", self.img)
        cv.waitKeyEx(t)

    def instanceCount(self, class_name):
        try:
            class_name.cnt = class_name.cnt + 1
        except AttributeError as e:
            print(e)
            class_name.cnt = 1
            print(f'Now is: {class_name.cnt}, object is: {class_name}')
        return class_name.cnt

    def getInstanceCnt(self, class_name):
        try:
            class_name.cnt = class_name.cnt
        except AttributeError as e:
            print(e)
            class_name.cnt = 0
        return class_name.cnt