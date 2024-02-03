from tkinter import *
from tkinter import messagebox
from info import *
from time import time, sleep
from stack import stack_class
from numpy import sign
WIDTH_CANVAS = 820
HEIGHT_CANVAS = 720

def FindSeed(img, stack, x_right, x_left, y, cFigure, cBorder):
    x = x_left
    while x <= x_right:
        flag = False
        
        while not is_cBorder(img, cBorder, x, y) and not is_cFigure(img, cFigure, x, y) and x <= x_right:
            if flag == False:
                flag = True
            x += 1

        if flag:
            if x == x_right and not is_cBorder(img, cBorder, x, y) and not is_cFigure(img, cFigure, x, y):
                stack.push([x, y])
            else:
                stack.push([x - 1, y])
            flag = False

        # Продолжаем проверку (Если интервал был прерван)
        x_temp = x
        while (is_cBorder(img, cBorder, x, y) or is_cFigure(img, cFigure, x, y)) and x < x_right:
            x += 1
            
        # удостоверимся, что координата пиксела увеличена
        if x == x_temp:
            x += 1

def fillArea(main_canvas, img, seed_point, cBorder, cFigure, delay = False):
    stack = stack_class(seed_point)

    while not stack.is_empty():

        x, y = stack.pop()

        img.put(cFigure[1], (x, y))

        x_temp = x 
        # процесс закрашивать правые пиксели
        x += 1
        while not is_cBorder(img, cBorder, x, y):
            img.put(cFigure[1], (x, y))
            x += 1
            check_limit(x) # проверить затравка
        x_right = x - 1

        # процесс закрашивать левые пиксели
        x = x_temp - 1
        while not is_cBorder(img, cBorder, x, y):
            img.put(cFigure[1], (x, y))
            x -= 1
            check_limit(x) # проверить затравка
        x_left = x + 1
        
        FindSeed(img, stack, x_right, x_left, y + 1, cFigure, cBorder)
        FindSeed(img, stack, x_right, x_left, y - 1, cFigure, cBorder)
        
        if delay:
            sleep(0.001)
            main_canvas.update()

            
def is_cBorder(img, cBorder, x, y):
        return img.get(x, y) == cBorder[0]

def is_cFigure(img, cFigure, x, y):
        return img.get(x, y) == cFigure[0]

def check_limit(x):
    if x >= WIDTH_CANVAS or x <= 0:
        messagebox.showerror("Ошибка", "Затравка находится внешние области")
    