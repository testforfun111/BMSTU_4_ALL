from tkinter import *
from tkinter import messagebox
from math import *
from const import *
from tkinter import colorchooser
from time import time, sleep
from algorithm import *

def choose_color_background(canv):
    global color_bg
    color_bg = colorchooser.askcolor(title="Выбор цвета")
    canv.configure(bg=color_bg[1])
    image_canvas.put(color_bg[1], to=(0, 0, CV_WIDE, CV_HEIGHT))
    ent_bg_canvas.configure(bg=color_bg[1])

def choose_color_line():
    global color_line
    color_line = colorchooser.askcolor(title="Выбор цвета")
    ent_line.configure(bg=color_line[1])

def check_option(option):
    messagebox.showindowfo("Выбран", "Выбрана опция %d" %(option))

def clear_canvas():
    canvas.delete("all")

def draw_dot(x, y, color):
    image_canvas.put(color, (x, y))
    
def sign(difference):
    if (difference < 0):
        return -1
    elif (difference == 0):
        return 0
    else:
        return 1

def brezeham_int(p1, p2, color):
    x1 = p1[0]
    y1 = p1[1]
    x2 = p2[0]
    y2 = p2[1]

    if (x2 - x1 == 0) and (y2 - y1 == 0):
        return [[x1, y1, color]]

    x = x1
    y = y1

    dx = abs(x2 - x1)
    dy = abs(y2 - y1)

    s1 = sign(x2 - x1)
    s2 = sign(y2 - y1)

    if (dy > dx):
        tmp = dx
        dx = dy
        dy = tmp
        swaped = 1
    else:
        swaped = 0

    e = 2 * dy - dx

    i = 1

    while (i <= dx + 1):

        draw_dot(x, y, color)

        while (e >= 0):
            if (swaped):
                x = x + s1
            else:
                y = y + s2

            e = e - 2 * dx

        if (swaped):
            y = y + s2
        else:
            x = x + s1

        e = e + 2 * dy

        i += 1

def draw_line(p1, p2, color):
    canvas.create_line(p1[0], p1[1], p2[0], p2[1], fill = color)

def read_dot():
    try:
        x = float(x_entry.get())
        y = float(y_entry.get())
    except:
        messagebox.showerror("Ошибка", "Неверно введены координаты точки")
        return

    add_dot(int(x), int(y))


def add_dot_click(event):
    x = event.x
    y = event.y

    add_dot(x, y)


def add_dot(x, y, last = True):
    cur_figure = len(dots) - 1
    dots[cur_figure].append([x, y])

    cur_dot = len(dots[cur_figure]) - 1

    if (last):
        dotslist_box.insert(END, "%d. (%4d;%4d)" %(cur_dot + 1, x, y))

    if (len(dots[cur_figure]) > 1):
        sides_list[cur_figure].append([dots[cur_figure][cur_dot - 1], dots[cur_figure][cur_dot]])
        draw_line(dots[cur_figure][cur_dot - 1], dots[cur_figure][cur_dot], COLOR_LINE)
        
def make_figure():
    cur_figure = len(dots)
    cur_dot = len(dots[cur_figure - 1])

    if (cur_dot < 3):
        messagebox.showerror("Ошибка", "Недостаточно точек, чтобы замкнуть фигуру")

    add_dot(dots[cur_figure - 1][0][0], dots[cur_figure - 1][0][1], last = False)

    dots.append(list())
    sides_list.append(list())

    dotslist_box.insert(END, "_______________________")

def reboot_prog():
    global dots
    global sides_list
    global image_canvas

    canvas.delete("all")

    image_canvas = PhotoImage(width = CV_WIDE, height = CV_HEIGHT)
    canvas.create_image((CV_WIDE / 2, CV_HEIGHT / 2), image = image_canvas, state = "normal")
    image_canvas.put(color_bg[1], to=(0, 0, CV_WIDE, CV_HEIGHT))
    canvas.grid(row = 0, column = 0, padx = 0, pady = 0)

    dots = [[]]
    sides_list = [[]]
    dotslist_box.delete(0, END)


if __name__ == "__main__":
    window = Tk()
    window['bg'] = window_COLOR
    window.geometry("%dx%d+0+0" %(window_WIDTH, window_HEIGHT))
    window.title("Растровое заполнение областей")

    menu = Menu(window, font="TkMenuFont")

    menu.add_command(label=AUTHOR_TITLE, command=lambda: messagebox.showinfo(AUTHOR_TITLE, AUTHOR))
    menu.add_command(label='Выход', command=window.destroy)
    window.configure(menu=menu)

    window.columnconfigure(0, weight=1)
    window.columnconfigure(1, weight=1)
    window.rowconfigure(0, weight=1)

    color_line = ((0, 0, 0), '#000000')
    color_bg = ((255, 255, 255), '#ffffff')
    canvas = Canvas(window, width = CV_WIDE, height = CV_HEIGHT, bg = CV_COLOR)
    canvas.grid(row = 0, column = 0, padx = 0, pady = 0)

    image_canvas = PhotoImage(width = CV_WIDE, height = CV_HEIGHT)
    canvas.create_image((CV_WIDE / 2, CV_HEIGHT / 2), image = image_canvas, state = "normal")
    image_canvas.put(color_bg[1], to=(0, 0, CV_WIDE, CV_HEIGHT))
    frame = Frame(window, bg ="khaki", width = 250, height = 750)
    frame.grid(row = 0, column = 1, padx = 0, pady = 0)

    #Color

    button = Button(frame)
    button.configure(text="Цвет фона", font = ("Arial", 15), command=lambda: choose_color_background(canvas))
    button.place(relx=0.01, rely=0.01, relheight=0.05, relwidth=0.7)

    button1 = Button(frame)
    button1.configure(text="Цвет заполнения", font = ("Arial", 15), command=lambda: choose_color_line())
    button1.place(relx=0.01, rely=0.08, relheight=0.05, relwidth=0.7)

    ent_bg_canvas = Label(frame, text =" " *5, font="-family {Consolas} -size 14", bg=color_bg[1])
    ent_bg_canvas.place(relx=0.74, rely=0.01, relheight=0.05, relwidth=0.27)

    ent_line = Label(frame, text =" " *5, font="-family {Consolas} -size 14", bg=color_line[1])
    ent_line.place(relx=0.74, rely=0.08, relheight=0.05, relwidth=0.27)
    ent_line.configure(bg=color_line[1])

    # Add dot

    add_dot_text = Label(frame, text = "Ввести точку", font = ("Arial", 16, "bold"), width = 43, bg = window_COLOR)
    add_dot_text.place(relx = 0, rely=0.15, relheight=0.05, relwidth=1)

    x_text = Label(frame, text = "X: ", font = ("Arial", 15), bg = window_COLOR)
    x_text.place(relx=0.08, rely=0.2, relwidth=0.1, relheight=0.047)

    x_entry = Entry(frame)
    x_entry.place(relx=0.2, rely=0.2, relwidth=0.65, relheight=0.036)

    y_text = Label(frame, text = "Y: ", font = ("Arial", 15), bg = window_COLOR)
    y_text.place(relx=0.08, rely=0.24, relwidth=0.1, relheight=0.047)

    y_entry = Entry(frame)
    y_entry.place(relx=0.2, rely=0.24, relwidth=0.65, relheight=0.036)

    add_dot_btn = Button(frame, text = "Добавить точку", font = ("Arial", 15), command = lambda: read_dot())
    add_dot_btn.place(relx=0.08, rely=0.32, relwidth=0.81, relheight=0.04)


    make_figure_btn = Button(frame, text = "Замкнуть фигуру", font = ("Arial", 15), command = lambda: make_figure())
    make_figure_btn.place(relx=0.08, rely=0.38, relwidth=0.81, relheight=0.04)


    # Dots list

    dots = [[]]
    sides_list = [[]]

    dots_list_text = Label(frame, text = "Список точек", font = ("Arial", 16, "bold"), width = 43, bg = window_COLOR)
    dots_list_text.place(relx=0, rely=0.46, relheight=0.03, relwidth=1)

    dotslist_box = Listbox(frame, bg = "white")
    dotslist_box.place(relx=0.08, rely=0.50, relheight=0.25, relwidth=0.82)

    # Fill figure

    option_filling = IntVar()
    option_filling.set(1)

    draw_delay = Radiobutton(frame, text = " С задержкой", font = ("Arial", 15), variable = option_filling, 
                    value = 1, bg = window_COLOR)
    draw_delay.place(relx=0.07, rely=0.77, relheight=0.03, relwidth=0.7)

    draw_without_delay = Radiobutton(frame, text = "Без задержки", font = ("Arial", 15), 
                    variable = option_filling, value = 2, bg = window_COLOR)
    draw_without_delay.place(relx=0.07, rely=0.81, relheight=0.03, relwidth=0.7)

    fill_figure_btn = Button(frame, text = "Закрасить область", font = ("Arial", 15),
                    command = lambda: fill(canvas, image_canvas, dots, sides_list, option_filling, color_bg, color_line))
    fill_figure_btn.place(relx=0.08, rely=0.86, relwidth=0.81, relheight=0.04)

    # Time and clear

    clear_window_btn = Button(frame, text = "Очистить экран", font = ("Arial", 15), command = lambda: reboot_prog())
    clear_window_btn.place(relx=0.08, rely=0.93, relwidth=0.81, relheight=0.04)
    # Binds

    canvas.bind("<1>", add_dot_click)
    window.mainloop()