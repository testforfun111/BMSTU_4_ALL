
from brezenham import *
from math import floor, fabs
from colorutils import *
from calc import *

I = 255
def wu(one_point, two_point, intensities):
    x1 = one_point[0]
    y1 = one_point[1]
    x2 = two_point[0]
    y2 = two_point[1]


    if x1 == x2 and y1 == y2:
        return [[x1, y1, intensities[0]]]
    
    flag = abs(y2 - y1) > abs(x2 - x1)

    if flag:
        x1, y1 = y1, x1
        x2, y2 = y2, x2
    if x1 > x2:
        x1, x2 = x2, x1
        y1, y2 = y2, y1

    dx = x2 - x1
    dy = y2 - y1

    if dx == 0:
        tg = 1
    else:
        tg = dy / dx

    points = []

    x1 = int(x1)
    x2 = int(x2 + 0.5)
    y = y1 + tg

    if flag:
        for x in range(x1, x2):
            points.append([int(y) + 1, x + 1, intensities[int((I - 1) * (abs(1 - fabs(y - int(y)))))]])
            points.append([int(y), x + 1, intensities[int((I - 1) * (abs(y - int(y))))]])
            y += tg
    else:
        for x in range(x1, x2):
            points.append([x + 1, int(y) + 1,  intensities[round((I - 1) * (abs(1 - y + floor(y))))]])
            points.append([x + 1, int(y), intensities[round((I - 1) * (abs(y - floor(y))))]])
            y += tg
    return points
