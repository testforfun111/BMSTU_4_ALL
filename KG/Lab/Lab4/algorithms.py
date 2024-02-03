from bresenham import *
from canonic import canonical_сircle, canonical_ellipse
from parametric import parameter_circle, parameter_ellipse
from midpoint import midpoint_circle, midpoint_ellipse
from tkinter import messagebox
from tkinter import *
from math import *
CWIDE = 1090
CHEIGHT = 780
list_algorithm = ['Канонического уравнения', 'Параметрического уравнения', 'Алгоритм средней точки', 'Алгоритм Брезенхем', 'Алгоритм библиотеки']

def change_to_screen(x, y):
    x = x + int(CWIDE / 2)
    y = int(CHEIGHT / 2) - y 
    return x, y

def standart_oval(canvas, xc, yc, ra, rb, colour):
    canvas.create_oval(xc - ra, yc - rb, xc + ra, yc + rb, outline=colour, tags='standart')

def spectrumBy_standart(canvas, xc, yc, ra, rb, step, count, colour):
    constant = ra / rb
    for e in range(0, count):
        standart_oval(canvas, xc, yc, ra, rb, colour)
        ra += step
        rb = round(ra / constant)

def spectrumEllipseBy_algorith(canvas, alg, xc, yc, ra, rb, step, count, colour):
    constant = ra / rb
    for e in range(0, count):
        alg(canvas, xc, yc, ra, rb, colour, True)
        ra += step
        rb = round(ra / constant)

def spectrumCircleBy_algorith(canvas, alg, xc, yc, rs, step, count, colour):
    for e in range(0, count):
        alg(canvas, xc, yc, rs, colour, True)
        rs += step

def draw_spectrumCircle(canvas, algorithm, type_hide, xc, yc, rn, rk, step, count, colour):
    try:
        xc = int(xc.get())
        yc = int(yc.get())
        xc, yc = change_to_screen(xc, yc)
    except:
        messagebox.showwarning("Ошибка", 
            "Неверно заданны координаты!\n"
            "Ожидался ввод целлых чисел.")
        return
    
    type = type_hide.get()
    if type == 0:
        try:
            rk = int(rk.get())
            step = int(step.get())
            count = int(count.get())
        except:
            messagebox.showwarning("Ошибка", 
                "Неверно заданны координаты!\nОжидался ввод целлых чисел.")
            return
        rn = rk - step * (count - 1)
    elif type == 2:
        try:
            rk = int(rk.get())
            rn = int(rn.get())
            count = int(count.get())
        except:
            messagebox.showwarning("Ошибка", 
                "Неверно заданны координаты!\n"
                "Ожидался ввод целлых чисел.")
            return
        step = int((rk - rn) / count)
    elif type == 3:
        try:
            rk = int(rk.get())
            rn = int(rn.get())
            step = int(step.get())
        except:
            messagebox.showwarning("Ошибка", 
                "Неверно заданны координаты!\n"
                "Ожидался ввод целлых чисел.")
            return
        count = floor((rk - rn) / step) + 1
    else:
        try:
            count = int(count.get())
            rn = int(rn.get())
            step = int(step.get())
        except:
            messagebox.showwarning("Ошибка", 
                "Неверно заданны координаты!\n"
                "Ожидался ввод целлых чисел.")
            return
    alg = list_algorithm.index(algorithm.get())

    if alg == 0:
        spectrumCircleBy_algorith(canvas, canonical_сircle, xc, yc, rn, step, count, colour)
    elif alg == 1:
        spectrumCircleBy_algorith(canvas, parameter_circle, xc, yc, rn, step, count, colour)
    elif alg == 2:
        spectrumCircleBy_algorith(canvas, midpoint_circle, xc, yc, rn, step, count, colour)
    elif alg == 3:
        spectrumCircleBy_algorith(canvas, bresenham_circle_octant, xc, yc, rn, step, count, colour)
    else:
        spectrumBy_standart(canvas, xc, yc, rn, rn, step, count, colour)
        return 


def draw_spectrumEllipse(canvas, algorithm, xc, yc, ra, rb, step, count, colour):
    try:
        xc = int(xc.get())
        yc = int(yc.get())
        ra = int(ra.get())
        rb = int(rb.get())
        step = int(step.get())
        count = int(count.get())
        xc, yc = change_to_screen(xc, yc)
    except:
        messagebox.showwarning("Ошибка", 
            "Неверно заданны координаты!\n"
            "Ожидался ввод целлых чисел.")
        return
    
    alg = list_algorithm.index(algorithm.get())

    if alg == 0:
        spectrumEllipseBy_algorith(canvas, canonical_ellipse, xc, yc, ra, rb, step, count, colour)
    elif alg == 1:
        spectrumEllipseBy_algorith(canvas, parameter_ellipse, xc, yc, ra, rb, step, count, colour)
    elif alg == 2:
        spectrumEllipseBy_algorith(canvas, midpoint_ellipse, xc, yc, ra, rb, step, count, colour)
    elif alg == 3:
        spectrumEllipseBy_algorith(canvas, bresenham_ellipse, xc, yc, ra, rb, step, count, colour)
    else:
        spectrumBy_standart(canvas,xc, yc, ra, rb, step, count, colour)
        return

def draw_ellipse(canvas, algorithm, xc, yc, ra, rb, color, drawMode=True):
    try:
        xc = int(xc.get())
        yc = int(yc.get())
        xc, yc = change_to_screen(xc, yc)
    except:
        messagebox.showwarning("Ошибка", 
            "Неверно заданны координаты!\n"
            "Ожидался ввод целлых чисел.")
        return
    
    try:
        ra = int(ra.get())
        rb = int(rb.get())
    except:
        messagebox.showwarning("Ошибка", 
            "Неверно заданно радиус!\n"
            "Ожидался ввод целых чисел.")
        return

    alg = list_algorithm.index(algorithm.get())
    
    add_ellipse(canvas, alg, xc, yc, ra, rb, color, True)

def add_ellipse(canvas, alg, xc, yc, ra, rb, color, drawMode=True):
    if alg == 0:
        canonical_ellipse(canvas, xc, yc, ra, rb, color, drawMode)
    elif alg == 1:
        parameter_ellipse(canvas, xc, yc, ra, rb, color, drawMode)
    elif alg == 2:
        midpoint_ellipse(canvas, xc, yc, ra, rb, color, drawMode)
    elif alg == 3:
        bresenham_ellipse(canvas, xc, yc, ra, rb, color, drawMode)
    else:
        standart_oval(canvas, xc, yc, ra, rb, color)
        return

def draw_circle(canvas, algorithm, xc, yc, r, color, drawMode=True):
    try:
        xc = int(xc.get())
        yc = int(yc.get())
        xc, yc = change_to_screen(xc, yc)
    except:
        messagebox.showwarning("Ошибка", 
            "Неверно заданны координаты!\n"
            "Ожидался ввод целлых чисел.")
        return
    
    try:
        r = int(r.get())
    except:
        messagebox.showwarning("Ошибка", 
            "Неверно заданно радиус!\n"
            "Ожидался ввод целых чисел.")
        return

    alg = list_algorithm.index(algorithm.get())
    
    add_circle(canvas, alg, xc, yc, r, color, True)

def add_circle(canvas, alg, xc, yc, r, color, drawMode=True):
    if alg == 0:
        canonical_сircle(canvas, xc, yc, r, color, drawMode)
    elif alg == 1:
        parameter_circle(canvas, xc, yc, r, color, drawMode)
    elif alg == 2:
        midpoint_circle(canvas, xc, yc, r, color, drawMode)
    elif alg == 3:
        bresenham_circle_octant(canvas, xc, yc, r, color, drawMode)
    else:
        standart_oval(canvas, xc, yc, r, r, color)
        return