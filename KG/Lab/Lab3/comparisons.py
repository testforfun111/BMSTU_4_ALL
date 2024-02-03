import matplotlib.pyplot as plt
import numpy as np
import time
from math import cos, sin, radians, pi
from tkinter import messagebox

from count_step import *
from brezenham import *
from dda import dda
from wu import wu
import draw

NUMBER_OF_RUNS = 50
list_algorithm = ['ДДА', 'Брезенхем (float)', 'Брезенхем (int)', 'Брезенхем (устр. ступенчатости)', 'Ву', 'Библиотека']

def step_comparison(x_center_entry, y_center_entry, radius_entry):

    try:
        x_centre = int(x_center_entry.get())
        y_centre = int(y_center_entry.get())
        radius = int(radius_entry.get())
    except:
        messagebox.showwarning("Ошибка", 
            "Неверно заданна длина отрезка для построения спектра!\n"
            "Ожидался ввод целого числа.")
        return

    if radius <= 0:
        messagebox.showwarning("Ошибка", 
            "Длина отрезка для построения спектра должна быть больше 0.")
        return
    
    centre_point = [x_centre, y_centre]

    dda_list = []
    bres_float_list = []
    bres_int_list = []
    bres_antial_list = []
    wu_list = []

    angle = 0
    angle_rot = radians(2)
    angle_list = [i for i in range(0, 91, 2)]
    
    while angle <= pi /2 + 0.01:
        x = x_centre + cos(angle) * radius
        y = y_centre + sin(angle) * radius

        dda_list.append(count_step_dda(centre_point, [x, y]))
        bres_float_list.append(count_step_brh_float(centre_point, [x, y]))
        bres_int_list.append(count_step_brh_int(centre_point, [x, y]))
        bres_antial_list.append(count_step_brh_antialiased(centre_point, [x, y]))
        wu_list.append(count_step_wu(centre_point, [x, y]))

        angle += angle_rot
    
    figure, axis = plt.subplots(2, 3)
    figure.set_figheight(8)
    figure.set_figwidth(14)
    axis[0, 0].plot(angle_list, dda_list)
    axis[0, 0].set_title("ЦДА")
    axis[0, 1].plot(angle_list, bres_float_list, linestyle = '--')
    axis[0, 1].set_title("Брезенхем float")
    axis[0, 2].plot(angle_list, bres_int_list, linestyle = '-')
    axis[0, 2].set_title("Брезенхем int")
    axis[1, 0].plot(angle_list, bres_antial_list, linestyle = '-.')
    axis[1, 0].set_title("Брезенхем c устранением ступенчатости")
    axis[1, 1].plot(angle_list, wu_list, linestyle = ':')
    axis[1, 1].set_title("Ву")

    plt.figure(figsize = (10, 6))
    plt.rcParams['font.size'] = '14'

    plt.plot(angle_list, dda_list, label = 'ЦДА')
    plt.plot(angle_list, bres_float_list, linestyle = '--', label = 'Брезенхем\n(float/int)')
    plt.plot(angle_list, bres_antial_list, label = 'Брезенхем\n(с устранением\nступенчатости)',
        linestyle = '-.')
    plt.plot(angle_list, wu_list, label = 'Ву', linestyle = ':')

    plt.title("Исследование ступенчатости.\n{0} - длина отрезка".format(radius))
    plt.legend()
    plt.xticks(np.arange(91, step = 5))
    plt.ylabel("Колличество ступенек")
    plt.xlabel("Угол в градусах")

    plt.show()

def time_comparison(canvas, color, color_bg, x_center_entry, y_center_entry, angle_entry, radius_entry):

    try:
        x_centre = int(x_center_entry.get())
        y_centre = int(y_center_entry.get())
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

    time_list = []   

    centre_point = [x_centre, y_centre]

    for i in range(0, 6):
        time_start = 0
        time_end = 0
        alg = i
        for _ in range(NUMBER_OF_RUNS):
            angle = 0

            while (angle < 2 * pi):
                x = x_centre + cos(angle) * radius
                y = y_centre + sin(angle) * radius

                end_point = [x, y]
                
                time_start += time.time()
                draw.add_line(canvas, color, color_bg, alg, centre_point, end_point, draw = False)
                time_end += time.time()

                angle += radians(angle_rot)

            draw.clear_canvas(canvas)

        res_time = (time_end - time_start) / NUMBER_OF_RUNS
        time_list.append(res_time)

    plt.figure(figsize = (10, 6))
    plt.rcParams['font.size'] = '12'
    plt.title("Замеры времени для построения спектров различными методами")

    positions = np.arange(6)
    methods = ["ЦДА", "Брезенхем\n(float)", "Брезенхем\n(int)",
               "Брезенхем\n(с устранением\n ступенчатости)", "Ву", "Библиотечная\nфункция"]

    plt.xticks(positions, methods)
    plt.ylabel("Время")

    plt.bar(positions, time_list, align = "center", alpha = 1)

    plt.show()
