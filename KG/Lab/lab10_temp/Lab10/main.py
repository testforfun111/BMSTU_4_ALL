#!/usr/bin/python
# -*- coding: utf-8 -*-
from tkinter import *
from numpy import arange 
from functions_answer import *
from interface import *
from constants import *
from draw import *
from solution import *
from tkinter import colorchooser
from functions import *
color_line = "green"

def choose_color_line():
    global color_line
    color_line = colorchooser.askcolor(title="Выбор цвета")[1]
    button_color.configure(bg = color_line)   
    canvas_class.color = color_line
def main():
    root = Tk()

    settings_interface(root, "1200x800", "Алгоритм Плавающего горизонта")

    global canvas_class
    canvas_class = paint_class(root, color_line)

    choice_func = option_menu(root, CHOICE, [900, 30])

    create_label(root, "X:", [810, 100])
    create_label(root, "Начало:", [850, 125])
    border_x_s = create_entry(root, [850, 150], 5, DEFAULT_BORDER_X_S)
    create_label(root, "Конец:", [950, 125])
    border_x_e = create_entry(root, [950, 150], 5, DEFAULT_BORDER_X_E)
    create_label(root, "Шаг:", [1050, 125])
    step_x = create_entry(root, [1050, 150], 5, DEFAULT_STEP_X)

    create_label(root, "Z:", [810, 180])
    create_label(root, "Начало:", [850, 205])
    border_z_s = create_entry(root, [850, 230], 5, DEFAULT_BORDER_Z_S)
    create_label(root, "Конец:", [950, 205])
    border_z_e = create_entry(root, [950, 230], 5, DEFAULT_BORDER_X_E)
    create_label(root, "Шаг:", [1050, 205])
    step_z = create_entry(root, [1050, 230], 5, DEFAULT_STEP_Z)

    create_label(root, "Поворот:", [810, 270])
    create_label(root, "∠ по x:", [850, 305])
    angle_x = create_entry(root, [850, 330], 5, DEFAULT_ANGLE_X)

    create_label(root, "∠ по y:", [950, 305])
    angle_y = create_entry(root, [950, 330], 5, DEFAULT_ANGLE_Y)

    create_label(root, "∠ по z:", [1050, 305])
    angle_z = create_entry(root, [1050, 330], 5,DEFAULT_ANGLE_Z)

    create_label(root, "Масштабирование:", [810, 380])
    scale = create_entry(root, [1000, 380], 5, SCALE)

    global button_color
    button_color = Button(text="Выбор цвета", width=30, command=choose_color_line, font="Times 13", bg = color_line)
    button_color.place(x=850, y=420)

    create_button(
        "Отобразить", lambda arg1=choice_func, arg2=[border_x_s, border_x_e, border_z_s, border_z_e], arg3=[step_x, step_z], 
        arg4=[angle_x, angle_y, angle_z, scale], arg5=canvas_class:  SolutionWrapper(arg1, arg2, arg3, arg4, arg5), [850, 500])

    canvas_class.canvas.bind(
        "<Motion>", lambda event: canvas_class.in_canvas(event))

    root.mainloop()

def draw_pixel(x, y, canvas_class):
    canvas_class.create_pixel(x, y)

def check_vision(x, y):
    return 0 <= x < WIDTH and 0 <= y < HEIGHT

def draw_point(x, y, top, bottom, canvas):
    if not check_vision(x, y):
        return False

    if y > top[x]:
        top[x] = y
        draw_pixel(x, y, canvas)

    elif y < bottom[x]:
        bottom[x] = y
        draw_pixel(x, y, canvas)

    return True

def draw_horizon_part(p1, p2, top, bottom, canvas):
    if p1[0] > p2[0]: # хочу, чтобы x2 > x1
        p1, p2 = p2, p1

    dx = p2[0] - p1[0]
    dy = p2[1] - p1[1]

    if dx == 0 and dy == 0:
        draw_point(round(p1[0]), p1[1], top, bottom, canvas)
        return 
    l = max(abs(dx), abs(dy))
    dx /= l
    dy /= l

    x, y = p1[0], p1[1]

    for _ in range(int(l) + 1):
        draw_point(round(x), y, top, bottom, canvas)
        x += dx
        y += dy

def draw_horizon(func, top, bottom, x_start, x_end, x_step, z, angles, scale, canvas):
    prev = None
    for x in arange(x_start, x_end + x_step, x_step):
        y = func(x, z)
        cur = transform(x, y, z, angles, scale)
        if (prev):
            draw_horizon_part(prev, cur, top, bottom, canvas)
        prev = cur 

def FloatHorizon1(borders_x, x_step, borders_z, z_step, canvas_class, f, angles, scale):
    global top, bottom
    # Инициализируем начальными значениями массивы горизонтов.
    top = [0] * WIDTH  # Верхний.
    bottom = [HEIGHT] * WIDTH  # Нижний.

    x_start = borders_x[0]
    x_end = borders_x[1]

    z_start = borders_z[0]
    z_end = borders_z[1]

    for z in arange(z_start, z_end, z_step):
        if (z < z_end - z_step):
            dot1 = transform(x_start, f(x_start, z), z, angles, scale)
            dot2 = transform(x_start, f(x_start, z+ z_step), z + z_step, angles, scale)
            canvas_class.draw_line(dot1, dot2)

        draw_horizon(f, top, bottom, x_start, x_end, x_step, z, angles, scale, canvas_class)

        if (z < z_end - z_step):
            dot1 = transform(x_end, f(x_end, z), z, angles, scale)
            dot2 = transform(x_end, f(x_end, z+ z_step), z + z_step, angles, scale)
            canvas_class.draw_line(dot1, dot2)

def SolutionWrapper1(choice, borders, step, angles, canvas_class):
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
    FloatHorizon1(borders_x, step_x, borders_z, step_z,
                 canvas_class, f[index], [angle_x, angle_y, angle_z], scale)
    
if __name__ == "__main__":
    main()
