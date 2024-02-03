from math import *
from brezenham import *
def count_step_dda(beg_point, end_point):
    
    dx = (end_point[0] - beg_point[0])
    dy = (end_point[1] - beg_point[1])

    if dx == 0 and dy == 0:
        return 0

    l = abs(max(abs(dx), abs(dy)))
    dx /= l
    dy /= l

    x = beg_point[0]
    y = beg_point[1]

    steps = 0

    i = 0
    while i <= l:
        x_buf = x
        y_buf = y

        x += dx
        y += dy

        if round(x_buf) != round(x) and round(y_buf) != round(y):
            steps += 1
        i += 1
    return steps


def count_step_brh_float(start_point, end_point):

    dx = end_point[0] - start_point[0]
    dy = end_point[1] - start_point[1]

    if dx == 0 and dy == 0:
        return 0

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

    x_buf = x
    y_buf = y
    steps = 0

    i = 0
    while i <= dx:
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

        if x_buf != x and y_buf != y:
            steps += 1

        x_buf = x
        y_buf = y
        i += 1
    return steps

def count_step_brh_int(beg_point, end_point):

    dx = end_point[0] - beg_point[0]
    dy = end_point[1] - beg_point[1]

    if dx == 0 and dy == 0:
        return 0

    x_sign = sign(dx)
    y_sign = sign(dy)

    dx = abs(dx)
    dy = abs(dy)

    if dy > dx:
        dx, dy = dy, dx
        exchange = 1
    else:
        exchange = 0

    two_dy = 2 * dy
    two_dx = 2 * dx

    e = two_dy - dx

    x = beg_point[0]
    y = beg_point[1]

    x_buf = x
    y_buf = y
    steps = 0

    i = 0
    while i <= dx:
        if e >= 0:
            if exchange == 1:
                x += x_sign
            else:
                y += y_sign
            e -= two_dx

        if exchange == 1:
            y += y_sign
        else:
            x += x_sign
        
        e += two_dy

        if x_buf != x and y_buf != y:
            steps += 1

        x_buf = x
        y_buf = y
        i += 1
    return steps
    

def count_step_brh_antialiased(beg_point, end_point):

    dx = end_point[0] - beg_point[0]
    dy = end_point[1] - beg_point[1]

    if dx == 0 and dy == 0:
        return 0

    x_sign = sign(dx)
    y_sign = sign(dy)

    dx = abs(dx)
    dy = abs(dy)

    if dy > dx:
        dx, dy = dy, dx
        exchange = 1
    else:
        exchange = 0

    m = dy / dx
    w = 1 - m
    e = 0.5
    
    x = beg_point[0]
    y = beg_point[1]

    x_buf = x
    y_buf = y
    steps = 0

    i = 0
    while i <= dx:
        if e < w:
            if exchange == 0:
                x += x_sign
            else:
                y += y_sign

            e += m

        else:
            x += x_sign
            y += y_sign
            e -= w

        if x_buf != x and y_buf != y:
            steps += 1

        x_buf = x
        y_buf = y
        i += 1
    return steps

def count_step_wu(one_point, two_point):
    x1 = one_point[0]
    y1 = one_point[1]
    x2 = two_point[0]
    y2 = two_point[1]

    dx = x2 - x1
    dy = y2 - y1

    if dx == 0 and dy == 0:
        return 0

    m = 1
    step = 1
    steps = 0
    I = 255

    if (abs(dy) >= abs(dx)):
        if (dy != 0):
            m = dx / dy
            
        m1 = m

        if (y1 > y2):
            m1 *= -1
            step *= -1

        bord = round(y2) - 1 if dy < dx else round(y2) + 1

        for y in range(round(y1), bord, step):
            d1 = x1 - floor(x1)
            d2 = 1 - d1

            if y < round(y2) and int(x1) != int(x1 + m):
                steps += 1

            x1 += m1
    else:
        if (dx != 0):
            m = dy / dx

        m1 = m

        if (x1 > x2):
            step *= -1
            m1 *= -1

        bord = round(x2) - 1 if dy > dx else round(x2) + 1

        for x in range(round(x1), bord, step):
            d1 = y1 - floor(y1)
            d2 = 1 - d1

            if x < round(x2) and int(y1) != int(y1 + m):
                steps += 1

            y1 += m1

    return steps
