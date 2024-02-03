from tkinter import *
from tkinter import messagebox, colorchooser
from math import *
import colorutils as cu
from my_algo import *

X_MIN = 0
X_MAX = 1
Y_MIN = 2
Y_MAX = 3
X_DOT = 0
Y_DOT = 1

cutter = []
figure = []

AUTHOR = "Ву Хай Данг - ИУ7-42Б"
TASK = "Отсечение многоугольника произвольным выпуклым отсекателем"

color_rec = ((255, 0, 0), 0)
color_line = ((0, 255, 0), 0)
color_result = ((0, 0, 255), 0)

def show_info(str):
    messagebox.showinfo("Info", str)
    return

def show_error(str):
    messagebox.showerror("Error", str)

def change_color_rec():
    global color_rec
    color_rec = colorchooser.askcolor()
    changecolor_rec.config(bg = color_rec[1])

def change_color_line():
    global color_line
    color_line = colorchooser.askcolor()
    changecolor_line.config(bg = color_line[1])

def change_color_result():
    global color_result
    color_result = colorchooser.askcolor()
    changecolor_result.config(bg = color_result[1])

def is_maked(object):
    maked = False
    if (len(object) > 3):
        if ((object[0][0] == object[len(object) - 1][0]) and (object[0][1] == object[len(object) - 1][1])):
            maked = True
    return maked

def reboot_prog():
    global figure
    global cutter
    canvas.delete("all")
    cutter = []
    figure = []
    cutter_dotslist_box.delete(0, END)
    figure_dotslist_box.delete(0, END)

def draw_cutter():
    for i in range(len(cutter)):
        canvas.create_line(cutter[i - 1], cutter[i], fill = cu.Color(color_rec[0]).hex)

def add_dot_figure(x, y, last = True):
    if (is_maked(figure)): 
        figure.clear()
        canvas.delete('all')
        draw_cutter()
        figure_dotslist_box.delete(0, END)
    if ([x, y] in figure and last):
        messagebox.showerror("Ошибка", "Ввести координаты точки должен быть разные.")
    else:
        figure.append([x, y])
        cur_dot = len(figure) - 1
        if (last):
            figure_dotslist_box.insert(END, "%d. (%4d;%4d)" %(cur_dot + 1, x, y))
        if (len(figure) > 1):
            canvas.create_line(figure[cur_dot - 1], figure[cur_dot], fill = cu.Color(color_line[0]).hex)

def add_dot_figure_click(event):
    x = event.x
    y = event.y
    add_dot_figure(x, y)

def draw_figure():
    for i in range(len(figure)):
        canvas.create_line(figure[i - 1], figure[i], fill = cu.Color(color_line[0]).hex)

def add_dot_cutter(x, y, last = True):
    if (is_maked(cutter)): # для задания нового отсекателя
        cutter.clear()
        canvas.delete("all")
        draw_figure()
        cutter_dotslist_box.delete(0, END)
    cutter.append([x, y])
    cur_dot = len(cutter) - 1
    if (last):
        cutter_dotslist_box.insert(END, "%d. (%4d;%4d)" %(cur_dot + 1, x, y))
    if (len(cutter) > 1):
        canvas.create_line(cutter[cur_dot - 1], cutter[cur_dot], fill = cu.Color(color_rec[0]).hex)

def add_dot_cutter_click(event):
    x = event.x
    y = event.y
    add_dot_cutter(x, y)

def read_dot_cutter():
    try:
        x = int(cutter_x_entry.get())
        y = int(cutter_y_entry.get())
    except:
        show_error("Неверно введены координаты точки")
        return
    add_dot_cutter(x, y)

def read_dot_figure():
    try:
        x = int(figure_x_entry.get())
        y = int(figure_y_entry.get())
    except:
        show_error("Неверно введены координаты точки")
        return
    add_dot_figure(x, y)

def del_dot_cutter():
    if (is_maked(cutter)):
        return
    cur_dot = len(cutter) - 1
    if (len(cutter) == 0):
        return
    if (len(cutter) > 1):
        canvas.create_line(cutter[cur_dot - 1], cutter[cur_dot], fill = "white")
    # Find index for a table
    index = len(cutter)
    cutter_dotslist_box.delete(index - 1, END)
    cutter.pop(len(cutter) - 1)

def make_cutter():
    if (is_maked(cutter)):
        show_error("Фигура уже замкнута")
        return
    cur_dot = len(cutter)
    if (cur_dot < 3):
        show_error("Недостаточно точек, чтобы замкнуть фигуру")
        return
    add_dot_cutter(cutter[0][0], cutter[0][1], last = False)

def make_figure():
    if (is_maked(figure)):
        show_error("Фигура уже замкнута")
        return
    cur_dot = len(figure)
    if (cur_dot < 3):
        show_error("Недостаточно точек, чтобы замкнуть фигуру")
        return
    add_dot_figure(figure[0][0], figure[0][1], last = False)

def get_vector(dot1, dot2):
    return [dot2[X_DOT] - dot1[X_DOT], dot2[Y_DOT] - dot1[Y_DOT]]

def vector_mul(vec1, vec2):
    return (vec1[0] * vec2[1] - vec1[1] * vec2[0])

def scalar_mul(vec1, vec2):
    return vec1[0] * vec2[0] + vec1[1] * vec2[1]


def check_polygon(): # через проход по всем точкам, поворот которых должен быть все время в одну сторону
    if (len(cutter) < 3):
        return False
    sign = 0
    if (vector_mul(get_vector(cutter[1], cutter[2]), get_vector(cutter[0], cutter[1])) > 0):
        sign = 1
    elif (vector_mul(get_vector(cutter[1], cutter[2]), get_vector(cutter[0], cutter[1])) < 0):
        sign = -1
    else:
        sign = 0
    
    if (sign == 0):
        return FALSE

    for i in range(3, len(cutter)):
        if sign * vector_mul(get_vector(cutter[i - 1], cutter[i]), get_vector(cutter[i - 2], cutter[i - 1])) <= 0:
            return False
    if (sign < 0):
        cutter.reverse()
    return True

def cut_area():
    if (not is_maked(cutter)):
        show_error("Отсекатель не замкнут")
        return
    
    if (not is_maked(figure)):
        show_error("Отекаемый многоугольник не замкнут")
        return
    
    if (len(cutter) < 3):
        show_error("Не задан отсекатель")
        return
    
    if (not check_polygon()):
        show_error("Отсекатель должен быть выпуклым многоугольником")
        return

    my_cutter = deepcopy(cutter)
    my_figure = deepcopy(figure)
    
    result = SutherlandHodgman(my_cutter, my_figure)

    if not result:
        return
    draw_result_figure(result)

def draw_result_figure(result):
    result.append(result[0])
    for i in range(len(result) - 1):
        canvas.create_line( round(result[i][0]), round(result[i][1]),
                            round(result[i+1][0]), round(result[i+1][1]), fill = cu.Color(color_result[0]).hex, width = 1.5)

window = Tk()
window.title("Лабораторная работа 9 : Отсечение произвольного многоугольника выпуклым отсекателем")
window.geometry('1200x750+180+20')

canvas = Canvas(window, bg = 'white', width = 880, height = 720, highlightbackground="black")
canvas.place(relx = 0.02, rely = 0.02)

canvas.bind("<1>", add_dot_cutter_click)
canvas.bind("<3>", add_dot_figure_click)

add_dot_text = Label(window, text = "Ввод отсекателя", font = "Times 12 bold")
add_dot_text.place(relx = 0.78, rely = 0.19)

cutter_x_text = Label(window, text = "X:")
cutter_x_text.place(relx = 0.78, rely = 0.23)

cutter_x_entry = Entry(window)
cutter_x_entry.place(relx = 0.8, rely = 0.23, relwidth=0.07)

cutter_y_text = Label(window, text = "Y:")
cutter_y_text.place(relx = 0.78, rely = 0.27)

cutter_y_entry = Entry(window)
cutter_y_entry.place(relx = 0.8, rely = 0.27, relwidth=0.07)

cutter_add_dot_btn = Button(window, text = "Добавить точку", command = lambda: read_dot_cutter())
cutter_add_dot_btn.place(relx = 0.9, rely = 0.24, relheight=0.05)

make_cutter_btn = Button(window, text = "Замкнуть отсекатель", command = lambda: make_cutter())
make_cutter_btn.place(relx = 0.818, rely = 0.31, relheight=0.05)

label_cutter_box = Label(window, text="Таблица вершин отсекателя", font="Times 12 bold")
label_cutter_box.place(relx=0.78, rely=0.37)
cutter_dotslist_box = Listbox(window, bg = "white", height = 6, width = 30)
cutter_dotslist_box.place(relx = 0.805, rely = 0.41)


figure_add_dot_text = Label(window, text = "Ввод многоугольника", font = "Times 12 bold")
figure_add_dot_text.place(relx = 0.77, rely = 0.56)

figure_x_text = Label(window, text = "X:")
figure_x_text.place(relx = 0.78, rely = 0.6)

figure_x_entry = Entry(window)
figure_x_entry.place(relx = 0.8, rely = 0.6, relwidth=0.07)

figure_y_text = Label(window, text = "Y:")
figure_y_text.place(relx = 0.78, rely = 0.64)

figure_y_entry = Entry(window)
figure_y_entry.place(relx = 0.8, rely = 0.64, relwidth=0.07)

figure_add_dot_btn = Button(window, text = "Добавить точку", command = lambda: read_dot_figure())
figure_add_dot_btn.place(relx = 0.9, rely = 0.61, relheight=0.05)

make_figure_btn = Button(window, text = "Замкнуть многоугольник", command = lambda: make_figure())
make_figure_btn.place(relx = 0.818, rely = 0.68, relheight=0.05)

label_figure_box = Label(window, text="Таблица вершин многоугольника", font="Times 12 bold")
label_figure_box.place(relx=0.78, rely=0.74)
figure_dotslist_box = Listbox(window, bg = "white", height = 7, width = 30)
figure_dotslist_box.place(relx = 0.805, rely = 0.77)

label_crec = Label(window, text = 'Цвет отсекателя', font ="Times 12")
label_crec.place(relx = 0.78, rely= 0.01, relheight=0.04, relwidth=0.1)
changecolor_rec = Button(window, text = 'Выбрать', bg = "#ff0000", command = lambda: change_color_rec())
changecolor_rec.place(relx = 0.88, rely = 0.01, relheight=0.04, relwidth=0.1)
label_crec = Label(window, text = 'Цвет отрезка', font ="Times 12")
label_crec.place(relx = 0.78, rely= 0.07, relheight=0.04, relwidth=0.1)
changecolor_line = Button(window, text = 'Выбрать', bg = "#00ff00", command = lambda: change_color_line())
changecolor_line.place(relx = 0.88, rely = 0.07, relheight=0.04, relwidth=0.1)
label_crec = Label(window, text = 'Цвет результата', font ="Times 12")
label_crec.place(relx = 0.78, rely= 0.13, relheight=0.04, relwidth=0.1)
changecolor_result = Button(window, text = 'Выбрать', bg = "#0000ff", command = lambda: change_color_result())
changecolor_result.place(relx = 0.88, rely = 0.13, relheight=0.04, relwidth=0.1)

cut_btn = Button(window, text = "Отсечь", command = lambda: cut_area())
cut_btn.place(relx = 0.77, rely = 0.94, relheight=0.05, relwidth=0.1)

clear_btn = Button(window, text = "Очистить экран", command = lambda: reboot_prog())
clear_btn.place(relx = 0.89, rely = 0.94, relheight=0.05, relwidth=0.1)

menubar = Menu(window) 
info_menu = Menu(menubar, tearoff = 0)
info_menu.add_command(label="О авторе", command = lambda: show_info(AUTHOR))
info_menu.add_command(label="О программе", command = lambda: show_info(TASK))
menubar.add_cascade(label="Инфор", menu = info_menu)
exit_menu = Menu(menubar, tearoff = 0)
menubar.add_command(label = "Выход", command = window.destroy)
window.config(menu = menubar)

window.mainloop()