class color:
    COLOR_BLACK = [0,0,0,255]
    COLOR_WHITE = [255,255,255,255]
    COLOR_RED = [0,0,255,255]
    COLOR_GREEN = [0,255,0,255]
    COLOR_BLUE = [255,0,0,255]
    TRANSPARENT_WHITE = [255,255,255,0]
    TRANSPARENT_BLACK = [0,0,0,0]
    TRANSPARENT = TRANSPARENT_WHITE

    COLOR_BROWN = [0, 64, 128, 255]
    COLOR_GREY = [128, 128, 128, 255]

    def __init__(self):
        pass

    def addCustomColor(self, name, value):
        self.dict:dict
        self.dict[name] = value

    def getColor(self, name):
        ret = None
        try:
            ret = self.dict[name]
        except AttributeError or KeyError as e:
            print(e)
            print(f'No such color: {name}')
        return ret
