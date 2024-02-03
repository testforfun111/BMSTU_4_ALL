from tkinter import messagebox
from tkinter import *
from math import cos, sin, radians, pi
import main
from brezenham import bresenham_int, bresenham_float, bresenham_antialiased
from dda import dda
from wu import wu
from calc import *
CWIDE = 1090
CHEIGHT = 780

list_algorithm = ['ДДА', 'Брезенхем (float)', 'Брезенхем (int)', 'Брезенхем (устр. ступенчатости)', 'Ву', 'Библиотека']

def change_to_screen(x, y):
    x = x + CWIDE / 2
    y = CHEIGHT / 2 - y 
    return x, y

def set_pixel(canvas, x, y, color):
    canvas.create_line(x, y, (x+1),
        y + 1 , fill = color)

def lib_alg(canvas, one_point, two_point, color):
    canvas.create_line(one_point[0], one_point[1],
        two_point[0] + 1, two_point[1] + 1, fill = color)


def add_line(canvas, color, color_bg, alg, one_point, two_point, draw = True):
    I = 255
    intensities = get_rgb_intensity(color[0], color_bg[0], I) 
    if alg == 0:
        points = dda(one_point, two_point, color[1])
    elif alg == 1:
        points = bresenham_float(one_point, two_point, color[1])
    elif alg == 2:
        points = bresenham_int(one_point, two_point, color[1])
    elif alg == 3:
        points = bresenham_antialiased(one_point, two_point, color[0], intensities)
    elif alg == 4:
        points = wu(one_point, two_point, intensities)
    else:
        lib_alg(canvas, one_point, two_point, color[1])
        return

    if draw:
        for i in points:
            set_pixel(canvas, i[0], i[1], i[2])
    
def draw_line(canvas, color, color_bg, algorithm, x_beg_entry, y_beg_entry, x_end_entry, y_end_entry):
    
    try:
        x_beg = int(x_beg_entry.get())
        y_beg = int(y_beg_entry.get())
    except:
        messagebox.showwarning("Ошибка", 
            "Неверно заданны координаты начала отрезка!\n"
            "Ожидался ввод целлых чисел.")
        return
    
    try:
        x_end = int(x_end_entry.get())
        y_end = int(y_end_entry.get())
    except:
        messagebox.showwarning("Ошибка", 
            "Неверно заданны координаты конца отрезка!\n"
            "Ожидался ввод целых чисел.")
        return
    alg = list_algorithm.index(algorithm.get())
    x_beg, y_beg = change_to_screen(x_beg, y_beg)
    x_end, y_end = change_to_screen(x_end, y_end)
    add_line(canvas, color, color_bg, alg, [x_beg, y_beg], [x_end, y_end])

def draw_spectrum(canvas, x_center_entry, y_center_entry, color, color_bg, algorithm, angle_entry, radius_entry):
    try:
        x_centre = int(x_center_entry.get())
        y_centre = int(y_center_entry.get())
    except:
        messagebox.showwarning("Ошибка", "Неверно заданны координаты начала отрезка!\n"
            "Ожидался ввод целлых чисел.") 
        return 
    
    try:
        angle_rot = int(angle_entry.get())
    except:
        messagebox.showwarning("Ошибка", 
            "Неверно задан угол поворота для построения спектра!\n"
            "Ожидался ввод целого числа.")
        return

    try:
        radius = int(radius_entry.get())
    except:
        messagebox.showwarning("Ошибка", 
            "Неверно заданна длина отрезка для построения спектра!\n"
            "Ожидался ввод целого числа.")
        return
    
    if angle_rot == 0:
        messagebox.showwarning("Ошибка", 
            "Угол поворота для построения спектра не должен равняться 0.")
        return
    elif abs(angle_rot) > 360:
        messagebox.showwarning("Ошибка", 
            "Угол поворота для построения спектра не должен превышать 360 градусов (по модулю).")
        return
    elif radius <= 0:
        messagebox.showwarning("Ошибка", 
            "Длина отрезка для построения спектра должна быть больше 0.")
        return
    x_centre, y_centre = change_to_screen(x_centre, y_centre)
    alg = list_algorithm.index(algorithm.get())
    angle_rot = radians(angle_rot)
    angle =  0

    # canvas.delete('all')
    # main.build_canvas(canvas)
    while (angle < 2 * pi):
        x_end = x_centre + cos(angle) * radius
        y_end = y_centre + sin(angle) * radius

        add_line(canvas, color, color_bg, alg, [x_centre, y_centre], [x_end, y_end])

        angle += angle_rot
    
def clear_canvas(canvas):
    canvas.delete("all")
    main.build_canvas(canvas)
