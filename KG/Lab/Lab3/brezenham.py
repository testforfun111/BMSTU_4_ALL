'''
Алгоритмы Брезенхема
'''
from math import *
from calc import *

I = 255

def sign(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0

def bresenham_float(start_point, end_point, color):

    dx = end_point[0] - start_point[0]
    dy = end_point[1] - start_point[1]

    if dx == 0 and dy == 0:
        return [[start_point[0], start_point[1], color]]

    x_sign = sign(dx)
    y_sign = sign(dy)

    dx = abs(dx)
    dy = abs(dy)

    if dy > dx:
        dx, dy = dy, dx
        exchange = 1
    else:
        exchange = 0

    e = dy / dx - 0.5

    x = start_point[0]
    y = start_point[1]
    points = []

    i = 0
    while i <= dx:
        points.append([x, y, color])

        if e >= 0:
            if exchange:
                x += x_sign
            else:
                y += y_sign
            e -= 1

        if exchange:
            y += y_sign
        else:
            x += x_sign
        
        e += dy / dx
        i += 1
    return points

def bresenham_int(start_point, end_point, color):

    dx = end_point[0] - start_point[0]
    dy = end_point[1] - start_point[1]

    if dx == 0 and dy == 0:
        return [[start_point[0], start_point[1], color]]

    x_sign = sign(dx)
    y_sign = sign(dy)

    dx = abs(dx)
    dy = abs(dy)

    if dy > dx:
        dx, dy = dy, dx
        exchange = 1
    else:
        exchange = 0

    e = 2 * dy - dx

    x = start_point[0]
    y = start_point[1]
    points = []

    i = 0
    while i <= dx:
        points.append([x, y, color])

        if e >= 0:
            if exchange == 1:
                x += x_sign
            else:
                y += y_sign

            e -= 2 * dx

        if exchange == 1:
            y += y_sign
        else:
            x += x_sign
        
        e += 2 * dy
        i += 1

    return points

def bresenham_antialiased(start_point, end_point, color, intensities):

    dx = end_point[0] - start_point[0]
    dy = end_point[1] - start_point[1]

    if dx == 0 and dy == 0:
        return [[start_point[0], start_point[1], color]]

    x_sign = sign(dx)
    y_sign = sign(dy)

    dx = abs(dx)
    dy = abs(dy)

    if dy > dx:
        dx, dy = dy, dx
        exchange = 1
    else:
        exchange = 0

    m = dy / dx * I
    w = I - m    
    e = I / 2
    
    x = start_point[0]
    y = start_point[1]
    points = []

    i = 0
    while i <= dx:
        points.append([x, y, intensities[I - round(e) - 1]])

        if e < w:    #Если ордината соседнего пиксела не увеличивается
            if exchange == 0:
                x += x_sign
            else:
                y += y_sign

            e += m

        else:       # ордината соседнего пиксела увеличивается на единицу
            x += x_sign
            y += y_sign
            e -= w  # необходимо вычесть величину площади пиксела, то есть единицу: f=f+m-1
        i += 1
    return points
