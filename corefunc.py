def lapTUnit(a, b, w=None, gamma=0):
    if w is None:
        w = float(b[3]) / 255
    ret = b * w + a * (1 - w) + gamma
    return ret


TRANSPARENCY_AUTO = 0
def lapTIMG(base, cover, transparency=0, gamma=0, pos=[0, 0]):
    ret = base.copy()
    opacity = None
    if transparency != 0:
        print(transparency)
        opacity = 1 - transparency
    for j in range(0, cover.__len__()):
        for i in range(0, cover[j].__len__()):
            if opacity is None:
                ret[j + pos[0]][i + pos[1]] = lapTUnit(base[j + pos[0]][i + pos[1]], cover[j][i], w=None, gamma=gamma)
            else:
                ret[j + pos[0]][i + pos[1]] = lapTUnit(base[j + pos[0]][i + pos[1]], cover[j][i], w=int(float(cover[j][i][3] * opacity) / 255), gamma=gamma)
    return ret
