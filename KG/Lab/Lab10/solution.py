from main import * 
from math import fabs, ceil, sqrt
from tkinter import messagebox as mb
from functions_answer import float_answer, get_two_answer, int_answer
# from draw import coordinate_transform
from interface import print_error
from functions import *
from constants import *
from r import *


top = [None] * WIDTH  # Верхний.
bottom = [HEIGHT] * WIDTH  # Нижний.
# Подпрограмма вычисляет пересечение с горизонтом.
def Intersection(x1, y1, x2, y2, arr, canvas_class):
    dx = x2 - x1
    dyc = y2 - y1
    dyp = arr[x2] - arr[x1]
    if dx == 0:
        xi = x2
        yi = arr[x2]
        return xi, yi
    if y1 == arr[x1] and y2 == arr[x2]:
        return x1, y1
    m = dyc / dx
    xi = x1 - round(dx * (y1 - arr[x1]) / (dyc - dyp))
    yi = round((xi - x1) * m + y1)
    return xi, yi

# Подпрограмма, определяющая видимость точки.
# flag:
# 0 - невидима.
# 1 - выше верхнего.
# -1 - ниже нижнего.
def Visible(x, y):  # Visible point
    global top, bottom
    # Если точка, ниже нижнего горизонта (или на нем)
    # То она видима.
    
    if bottom[x] == None or y <= bottom[x]:
        return -1
    # Если точка выше верхнего горизонта (или на нем)
    # То она видима.
    if top[x] == None or y >= top[x]:  
        return 1
    # Иначе она невидима.
    return 0

# Подпрограмма заполнения массивов горизонтов между x1 и x2 
def Horizon(x1, y1, x2, y2, canvas_class):
    global top, bottom

    # Проверка вертикальности наклона.
    if (x2 - x1 == 0):
        if top[x2] == None: top[x2] = y2
        else: top[x2] = max(top[x2], y2)
        if bottom[x2] == None: bottom[x2] = y2 
        else: bottom[x2] = min(bottom[x2], y2)
        return
    # Иначе вычисляем наклон.
    m = (y2 - y1) / (x2 - x1)
    # Движемся по x с шагом 1, чтобы заполнить 
    # Массивы от x1 до x2.
    for x in range(x1, x2 + 1):
        y = round(m * (x - x1) + y1)
        if top[x] == None: top[x] = y
        else: top[x] = max(top[x], y)
        if bottom[x] == None: bottom[x] = y
        else: bottom[x] = min(bottom[x], y)

# Функция обработки и обновления точек бокового рёбра
def Side(x, y, xe, ye,canvas_class):
    if (xe != -1):
        # Если кривая не первая
        canvas_class.draw_line([xe, ye], [x, y])
        Horizon(xe, ye, x, y, canvas_class)
    xe = x
    ye = y
    return xe, ye


def FloatHorizon(borders_x, x_step, borders_z, z_step, canvas_class, f, angles, scale):
    global top, bottom
    # Инициализируем начальными значениями массивы горизонтов.
    top = [None] * WIDTH  # Верхний. Начальные значения не определен, потом если мы первый раз сравнение то мы 
                            # мы сразу присвоить его новый значения.
    bottom = [HEIGHT] * WIDTH  # Нижний.

    x_start = borders_x[0]
    x_end = borders_x[1]

    z_start = borders_z[0]
    z_end = borders_z[1]

    x_left, y_left = -1, -1
    x_right, y_right = -1, -1

    z = z_end

    while z >= z_start - z_step / 2:
        x_prev = x_start
        y_prev = f(x_start, z)
        x_prev, y_prev = transform(x_prev,y_prev, z, angles, scale)

        flag_prev = Visible(x_prev, y_prev)
        #check vision
        x_left, y_left = Side(x_prev, y_prev, x_left, y_left, canvas_class)
        x = x_start
        while x <= x_end + x_step / 2:
            y_curr = f(x, z)
            x_curr, y_curr = transform(x, y_curr, z, angles, scale)

            flag_curr = Visible(x_curr, y_curr)

            if flag_curr == flag_prev:
                if flag_curr != 0:
                    canvas_class.draw_line([x_prev, y_prev], [x_curr, y_curr])
                    Horizon(x_prev, y_prev, x_curr, y_curr, canvas_class)
            else:
                if flag_curr == 0:
                    if flag_prev == 1:
                        xi, yi = Intersection(x_prev, y_prev, x_curr, y_curr, top, canvas_class)
                    else: 
                        xi, yi = Intersection(x_prev, y_prev, x_curr, y_curr, bottom, canvas_class)
                    canvas_class.draw_line([x_prev, y_prev], [xi, yi])
                    Horizon(x_prev, y_prev, xi, yi, canvas_class)
                else:
                    if flag_curr == 1:
                        if flag_prev == 0:
                            xi, yi = Intersection(x_prev, y_prev, x_curr, y_curr, top, canvas_class)
                            canvas_class.draw_line([xi, yi], [x_curr, y_curr])
                            Horizon(xi, yi, x_curr, y_curr, canvas_class) 
                        else:
                            xi, yi = Intersection(x_prev, y_prev, x_curr, y_curr, bottom, canvas_class)
                            canvas_class.draw_line([x_prev, y_prev], [xi, yi])
                            Horizon(x_prev, y_prev, xi, yi, canvas_class)
                            xi, yi = Intersection(x_prev, y_prev, x_curr, y_curr, top, canvas_class)
                            canvas_class.draw_line([xi, yi], [x_curr, y_curr])
                            Horizon(xi, yi, x_curr, y_curr, canvas_class)
                    else: # flag_curr == -1
                        if flag_prev == 0:
                            xi, yi = Intersection(x_prev, y_prev, x_curr, y_curr, bottom, canvas_class)
                            canvas_class.draw_line([xi, yi], [x_curr, y_curr])
                            Horizon(xi, yi, x_curr, y_curr, canvas_class)  
                        else:
                            xi, yi = Intersection(x_prev, y_prev, x_curr, y_curr, top, canvas_class)
                            canvas_class.draw_line([x_prev, y_prev], [xi, yi])
                            Horizon(x_prev, y_prev, xi, yi, canvas_class)
                            xi, yi = Intersection(x_prev, y_prev, x_curr, y_curr, bottom, canvas_class)
                            canvas_class.draw_line([xi, yi], [x_curr, y_curr])
                            Horizon(xi, yi, x_curr, y_curr, canvas_class)
            x_prev, y_prev = x_curr, y_curr
            flag_prev = flag_curr
            x += x_step
        x_right, y_right = Side(x_prev, y_prev, x_right, y_right,canvas_class)
        z -= z_step

def SolutionWrapper(choice, borders, step, angles, canvas_class):
    borders_x = [int_answer(borders[0].get()), int_answer(borders[1].get())]
    if borders_x[0] == FALSE:
        return

    step_x = float_answer(step[0].get())
    if step_x == FALSE:
        return

    borders_z = [int_answer(borders[2].get()), int_answer(borders[3].get())]
    if borders_z[0] == FALSE:
        return

    step_z = float_answer(step[1].get())
    if step_z == FALSE:
        return

    angle_x = float_answer(angles[0].get())
    if angle_x == FALSE:
        return

    angle_y = float_answer(angles[1].get())
    if angle_y == FALSE:
        return

    angle_z = float_answer(angles[2].get())
    if angle_z == FALSE:
        return

    scale = int_answer(angles[3].get())
    if scale == FALSE:
        return 
    
    f = [f1, f2, f3, f4]
    index = CHOICE.index(choice.get())

    canvas_class.clear_all()
    FloatHorizon(borders_x, step_x, borders_z, step_z,
                 canvas_class, f[index], [angle_x, angle_y, angle_z], scale)