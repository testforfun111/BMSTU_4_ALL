from math import *
from const import *
from tkinter import messagebox
from time import *

def get_limit(dots):
    x_max = 0 
    x_min = CV_WIDE 

    y_max = 0
    y_min = CV_HEIGHT

    for figure in dots:
        for dot in figure:
            if (dot[0] > x_max):
                x_max = dot[0]
            if (dot[0] < x_min):
                x_min = dot[0]
            if (dot[1] < y_min):
                y_min = dot[1]
            if (dot[1] > y_max):
                y_max = dot[1]
    
    block_edges = (x_min, y_min, x_max, y_max)
    return block_edges

def find_intersections(start, stop, lst):
    if stop[1] == start[1]:
        return

    if start[1] > stop[1]:
        start, stop = stop, start

    dy = 1
    dx = (stop[0] - start[0]) / (stop[1] - start[1])
    x = start[0]
    y = start[1]

    while y < stop[1]:
        lst.append([int(x), int(y)])
        y += dy
        x += dx

def reverse_pixel(img, x, y, color_bg, color_line):
    color_pixel = img.get(x, y)
    if color_pixel != color_line[0]:
        img.put(color_line[1], (x, y))
    elif color_pixel == color_line[0]:
        img.put(color_bg[1], (x, y))


def fill(canvas, image_canvas, dots, side_list, option_delay, color_bg, color_line):
    cur_figure = len(dots) - 1
    if (len(dots[cur_figure]) != 0):
        messagebox.showerror("Ошибка", "Крайняя фигура не замкнута")
        return 
    block_edges = get_limit(dots)

    if (option_delay.get() == 1):
        delay = True 
    else:
        delay = False 
    time_start = time()
    edge_fill_algorithm(canvas, image_canvas, side_list, block_edges, color_bg, color_line, delay)
    time_end = time()
    if delay == False:
        messagebox.showinfo("Время", "Время заполнения " + str(round(time_end - time_start, 4)))

def edge_fill_algorithm(canvas, image_canvas, side_list, block_edges, color_bg, color_fill, delay = False):
    x_max = block_edges[2]
    for edges in side_list:
        for edge in edges:
            lst = []
            find_intersections(edge[0], edge[1], lst)
            
            for i in range(len(lst)):
                for j in range(lst[i][0] + 1, x_max + 1):
                    reverse_pixel(image_canvas, j, lst[i][1], color_bg, color_fill)
                if delay:
                    sleep(0.001)
                    canvas.update()
                        