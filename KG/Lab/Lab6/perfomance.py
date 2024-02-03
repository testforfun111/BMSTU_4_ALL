from tkinter import *
from tkinter import colorchooser
from info import *
from time import time, sleep
from stack import stack_class
from numpy import sign
from algorithm import *

img = 0
curColorFigure = ((0, 255, 0), '#00FF00')
curColorBorder = ((0, 0, 0), '#000000')
curColorBackground = ((255, 255, 255), '#FFFFFF')
WIDTH_CANVAS = 820
HEIGHT_CANVAS = 720

polygons = [[]]
seed_point = []
check_num = 0

def create_menu(window):
    menubar = Menu(window)
    
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label='Выход', command=window.destroy)
    menubar.add_cascade(label='Файл', menu=filemenu)
    
    infomenu = Menu(menubar, tearoff=0)
    infomenu.add_command(label='О авторе', command=about_author)
    infomenu.add_command(label = 'О программе', command=about_task)
    menubar.add_cascade(label='Информация', menu=infomenu)
    
    window.config(menu=menubar)
    
def create_labels(window):
    coordsLabel = Label(window, text = "Координаты точки", font=("Time News Roman", 14))
    coordsLabel.place(relx = 0.72, rely= 0.1)
    
    xLabel = Label(window, text = "X: ")
    xLabel.place(relx = 0.75, rely = 0.15)
    
    yLabel = Label(window, text = "Y: ")
    yLabel.place(relx = 0.75, rely = 0.18)
    
    tableLabel = Label(window, text = "Таблица точек", font = ("Time News Roman", 14))
    tableLabel.place(relx = 0.72, rely= 0.265)
    modeLabel = Label(window, text = "Режим заполнения", font=("Time News Roman", 14))
    modeLabel.place(relx = 0.72, rely = 0.68)
    
    seedPointLabel = Label(window, text = "Координаты затравочной точка", font=("Time News Roman", 14))
    seedPointLabel.place(relx = 0.72, rely = 0.78)
    
    xSeedLabel = Label(window, text = "X: ")
    xSeedLabel.place(relx = 0.72, rely = 0.83)
    
    ySeedLabel = Label(window, text = "Y: ")
    ySeedLabel.place(relx = 0.81, rely = 0.83)
    
    timeLabel = Label(window, text = "Время выполнения: ", font = "Consolas 14")
    timeLabel.place(relx = 0, rely = 0.96)
    
    # sizeLabel = Label(window, text = "820 x 720", font = "Consolas 14")
    # sizeLabel.place(relx = 0.58, rely = 0.96)
    
    return timeLabel

def create_table():
    table = Listbox(bg = "white", height = 17, width = 45)
    table.place(relx = 0.72, rely = 0.3)
    
    return table

def creat_radio_button():
    option = IntVar()
    option.set(2)
    
    no_delay = Radiobutton(text = "Без зажержки", variable = option, value = 1)
    no_delay.place(relx = 0.73, rely =0.72)
    
    no_delay = Radiobutton(text = "C зажержкой", variable = option, value = 2)
    no_delay.place(relx = 0.85, rely =0.72)
    
    return option

def create_canvas(window):
    canvas = Canvas(window, width=WIDTH_CANVAS, height=HEIGHT_CANVAS, background='#000000')
    canvas.place(relx=0.02, rely=0)
    
    global img
    
    img = PhotoImage(width=WIDTH_CANVAS, height=HEIGHT_CANVAS)
    canvas.create_image((410, 360), image=img, state='normal')
    img.put(curColorBackground[1], to=(0, 0, WIDTH_CANVAS, HEIGHT_CANVAS))

    figure_canvas = Canvas(window, bg = curColorFigure[1], width = 30, height = 29)
    figure_canvas.place(relx=0.815, rely=0.035)
    
    border_canvas = Canvas(window, bg = curColorBorder[1], width = 30, height = 29)
    border_canvas.place(relx = 0.955, rely = 0.035)
    
    return canvas, figure_canvas, border_canvas

def create_button(window, main_canvas, figure_canvas,border_canvas, option, table, timeLabel, new_point, new_seed_point):
    choosefigureColor = Button(window, text = "Цвет заполнения", command = lambda: chooseFigureColor(figure_canvas))
    choosefigureColor.place(relx = 0.728, rely = 0.035, relheight=0.04)
    
    chooseborderColor = Button(window, text = "Цвет границы", command = lambda: chooseBorderColor(border_canvas))
    chooseborderColor.place(relx = 0.88, rely = 0.035, relheight = 0.04)
    
    addPoint = Button(window, text = "Добавить", width=10, height=1, command = lambda: add_point_from_screen(new_point, table, main_canvas))
    addPoint.place(relx = 0.86, rely = 0.16)
    
    closeButton = Button(window, text = "Замкнуть", width = 10, height=1, command = lambda : close_figure(main_canvas, table))
    closeButton.place(relx = 0.795, rely = 0.22)
    
    addSeedPoint = Button(window, text = "Добавить зат.точку", command = lambda: add_seed_point_from_screen(new_seed_point))
    addSeedPoint.place(relx = 0.89, rely = 0.825)
    
    drawButton = Button(window, text = "Закрасить", command = lambda: fill_wrapper(main_canvas, img, polygons, 
                                                                seed_point, check_num, curColorBorder, curColorFigure, option, timeLabel))
    drawButton.place(relx = 0.76, rely = 0.90, relheight=0.04, relwidth=0.15)
    
    clearButton = Button(window, text = "Очистить", command = lambda: clear_screen(main_canvas, table, timeLabel))
    clearButton.place(relx = 0.76, rely = 0.94, relheight=0.04, relwidth=0.15)
    
    main_canvas.bind("<1>", lambda e, f = table, g =main_canvas : add_point_click(e, f, g))
    main_canvas.bind("<B1-Motion>", lambda e, f = table, g =main_canvas : add_point_click(e, f, g))
    main_canvas.bind("<3>", lambda e : add_seed_point_click(e))

def chooseFigureColor(canvas_color_figure):
    global curColorFigure
    curColorFigure = colorchooser.askcolor()
    canvas_color_figure.config(bg = curColorFigure[1])
    
def chooseBorderColor(canvas_color_border):
    global curColorBorder
    curColorBorder = colorchooser.askcolor()    
    canvas_color_border.config(bg = curColorBorder[1])
    
def create_entry(window):
    global xSeedEntry, ySeedEntry
    xEntry = Entry(window)
    xEntry.place(relx = 0.77, rely = 0.15, relwidth = 0.07)
    
    yEntry = Entry(window)
    yEntry.place(relx = 0.77, rely = 0.18, relwidth = 0.07)
    
    xSeedEntry = Entry(window)
    xSeedEntry.place(relx = 0.74, rely = 0.83, relwidth = 0.03)
    # xSeedEntry.insert(0, str(seed_point[0]))

    ySeedEntry = Entry(window)
    ySeedEntry.place(relx = 0.83, rely = 0.83, relwidth = 0.03)
    # ySeedEntry.insert(0, str(seed_point[1]))
    
    return [xEntry, yEntry], [xSeedEntry, ySeedEntry]

def add_point_click(event, table, main_canvas):
    x = event.x
    y = event.y

    if not (0 <= x <= WIDTH_CANVAS) or not (0 <= y <= HEIGHT_CANVAS):
        box.showerror("Ошибка", "Выходится за границей дисплея")
        return

    add_point(x, y, table, main_canvas)
    
def add_seed_point_click(event):
    x = event.x
    y = event.y

    if not (0 <= x <= WIDTH_CANVAS) or not (0 <= y <= HEIGHT_CANVAS):
        box.showerror("Ошибка", "Выходится за границей дисплея")
        return

    add_seed_point(x, y)
    xSeedEntry.delete(0, END)
    ySeedEntry.delete(0, END)
    xSeedEntry.insert(END, str(x))
    ySeedEntry.insert(END, str(y))
def intBresenham(xStart, yStart, xEnd, yEnd):
    if xStart == xEnd and yStart == yEnd:
        img.put(curColorBorder[1], (xStart, yStart))
        return

    deltaX = xEnd - xStart
    deltaY = yEnd - yStart

    stepX = int(sign(deltaX))
    stepY = int(sign(deltaY))

    deltaX = abs(deltaX)
    deltaY = abs(deltaY)

    if deltaX < deltaY:
        deltaX, deltaY = deltaY, deltaX
        flag = True
    else:
        flag = False

    acc = deltaY + deltaY - deltaX
    curX = xStart
    curY = yStart

    for i in range(deltaX):
        img.put(curColorBorder[1], (curX, curY))

        if flag:
            if acc >= 0:
                curX += stepX
                acc -= deltaX + deltaX
            curY += stepY
            acc += deltaY + deltaY
        else:
            if acc >= 0:
                curY += stepY
                acc -= deltaX + deltaX
            curX += stepX
            acc += deltaY + deltaY

def add_point(x, y, table, main_canvas, finish = False):
    polygons[-1].append([x, y])
    table.insert(END, "%d. (%4d;%4d)" %(len(polygons[-1]), x, y))
    
    if len(polygons[-1]) > 1:
        beg = polygons[-1][-2]
        end = polygons[-1][-1]
        
        intBresenham(beg[0], beg[1], end[0], end[1])
    
    elif len(polygons[-1]) == 1:
        img.put(curColorBorder[1], (polygons[-1][0][0], polygons[-1][0][1]))
        
def add_seed_point(x, y):
    global seed_point
    if (seed_point):
        img.put(curColorBackground[1], seed_point)
    img.put(curColorFigure[1], (x, y))
    seed_point = [x, y]
    
    
def add_point_from_screen(new_point, table, main_canvas):
    try:
        x = int(new_point[0].get())
        y = int(new_point[1].get())
    except:
        box.showerror("Ошибка", "Входные данные должны быть целыми")
        return
    
    if not (0 <= x <= WIDTH_CANVAS) or not (0 <= y <= HEIGHT_CANVAS):
        box.showerror("Ошибка", "Выходится за границей дисплея")
        return
    
    add_point(x, y, table, main_canvas)
    
def clear_screen(main_canvas, table, timeLabel):
    main_canvas.delete("all")    
    global img
    img = PhotoImage(width=WIDTH_CANVAS, height=HEIGHT_CANVAS)
    main_canvas.create_image((410, 360), image=img, state='normal')
    img.put(curColorBackground[1], to=(0, 0, WIDTH_CANVAS, HEIGHT_CANVAS))
    
    table.delete(0, END)
    timeLabel.config(text = "Время выполнения: ")
    xSeedEntry.delete(0, END)
    ySeedEntry.delete(0, END)
    global polygons, check_num
    polygons = [[]]
    check_num = 0
        

def close_figure(main_canvas, table):
    if len(polygons[-1]) < 3:
        box.showerror("Ошибка", "Количество точек должно быть больше двух")
        return
    table.insert(END, "_" * 20)
    beg = polygons[-1][-1]
    end = polygons[-1][0]
    
    intBresenham(beg[0], beg[1], end[0], end[1])
    global check_num
    check_num += 1
    polygons.append([])
    
def add_seed_point_from_screen(new_seed_point):
    try:
        x = int(new_seed_point[0].get())
        y = int(new_seed_point[1].get())
    except:
        box.showerror("Ошибка", "Входные данные должны быть целыми")
        return

    if not (0 <= x <= WIDTH_CANVAS) or not (0 <= y <= HEIGHT_CANVAS):
        box.showerror("Ошибка", "Выходится за границей дисплея")
        return
    
    add_seed_point(x, y)
    
def fill_wrapper(main_canvas, img, polygons, seed_point, check_num, cBorder, cFigure, option, timeLabel):
    if not seed_point:
        box.showerror("Ошибка", "Пока не задана точка затравки")
        return
    if not (check_num + 1 == len(polygons) and len(polygons[-1]) == 0):
        box.showerror("Ошибка", "Фигура не замкнута")
        return
    
    begin_time, end_time = 0, 0
    
    if option.get() == 1:
        begin_time = time()
        fillArea(main_canvas, img, seed_point, cBorder, cFigure)
        end_time = time()
        
    elif option.get() == 2:
        begin_time = time()
        fillArea(main_canvas, img, seed_point, cBorder, cFigure, True)
        end_time = time()
        
    timeLabel.config(text = "Время выполнения: {} с".format(round(end_time - begin_time, 4)))