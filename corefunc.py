def lapTUnit(a, b, w=None, gamma=0):
    if w is None:
        w = float(b[3]) / 255
    ret = b * w + a * (1 - w) + gamma
    return ret


TRANSPARENCY_AUTO = 0
def lapTIMG(base, cover, transparency=0, gamma=0, pos=[0, 0], ifCopy=False):
    if ifCopy is True:
        ret = base.copy()
    else:
        ret = base
    opacity = None
    if transparency != 0:
        print(transparency)
        opacity = 1 - transparency
    for j in range(0, cover.__len__()):
        for i in range(0, cover[j].__len__()):
            if opacity is None:
                ret[j + pos[0]][i + pos[1]] = lapTUnit(base[j + pos[0]][i + pos[1]], cover[j][i], w=None, gamma=gamma)
            else:
                ret[j + pos[0]][i + pos[1]] = lapTUnit(base[j + pos[0]][i + pos[1]], cover[j][i], w=int(1.0 * cover[j][i][3] * opacity / 255), gamma=gamma)
    return ret

def simpleLap(base, cover, pos=[0,0], ifCopy=False):
    if ifCopy is True:
        ret = base.copy()
    else:
        ret = base
    length = cover[0].__len__()
    for j in range(0, cover.__len__()):
        ret[j+pos[0]][pos[1]:pos[1]+length] = cover[j]
    return ret
