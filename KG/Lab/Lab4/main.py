from tkinter import *
from tkinter import ttk
import tkinter.messagebox as box
from tkinter import colorchooser
from algorithms import *
from time_measure import *

CWIDE = 1090
CHEIGHT = 780
AUTHOR_TITLE = 'Об авторе'
AUTHOR = 'Ву Хай Данг\nИУ7И-42Б'
color_bg = ((255, 255, 255), '#FFFFFF')
color_line = ((255, 255, 255), '#FFFFFF')

def choose_color_background(canv, button):
    global color_bg
    color_bg = colorchooser.askcolor(title="Выбор цвета")
    canv.configure(bg=color_bg[1])
    button.configure(bg=color_bg[1])

def choose_color_line(button):
    global color_line
    color_line = colorchooser.askcolor(title="Выбор цвета")
    button.configure(bg=color_line[1])

def build_canvas(cnv_solution):                                                
    cnv_solution.create_line(CWIDE / 2, CHEIGHT, CWIDE / 2, 2, fill = 'black', arrow=LAST, width = 2)
    cnv_solution.create_line(0, CHEIGHT / 2, CWIDE - 2, CHEIGHT/ 2, fill = 'black', arrow=LAST, width = 2)
    pass

def check_button(t):
    if t == 1:
        rb.place(relx = 0.89, rely=0.43, relheight=0.04, relwidth=0.05)
        label_Ry.place(relx = 0.89, rely=0.405, relheight=0.03, relwidth=0.05)
        button1.config(text = "Построить эллипс", command=lambda:draw_ellipse(canvas, algorithm_combobox,
                                                        xc, yc, r, rb, color_line[1], True))
        label_Rx.config(text = "Rx")
        label_rn.config(text = "Rx")
        label_rk.config(text = "Ry")
        Rn.configure(state=NORMAL)
        Rk.configure(state=NORMAL)
        step.configure(state=NORMAL)
        amount.configure(state=NORMAL)
        radbutton3.place_forget()
        radbutton4.place_forget()
        radbutton5.place_forget()
        radbutton6.place_forget()
        button_spek.config(command = lambda:draw_spectrumEllipse(canvas, algorithm_combobox, 
                            x_spektrum, y_spektrum, Rn, Rk, step, amount, color_line[1]))
        button_time.config(command=lambda:time_comparison(canvas, color_line[1], 'ellipse'))
    else:
        label_rn.config(text = "Rн")
        label_rk.config(text = "Rк")
        radbutton3.place(relx = 0.723, rely=0.59, relheight=0.05, relwidth=0.05)
        radbutton4.place(relx = 0.79, rely=0.59, relheight=0.05, relwidth=0.05)
        radbutton5.place(relx = 0.86, rely=0.59, relheight=0.05, relwidth=0.05)
        radbutton6.place(relx = 0.93, rely=0.59, relheight=0.05, relwidth=0.05)
        rb.place_forget()
        label_Ry.place_forget()
        button1.config(text = "Построить окружность", command=lambda:draw_circle(canvas,
                                                        algorithm_combobox, xc, yc, r, color_line[1], True))
        label_Rx.config(text = "R")
        button_spek.config(command = lambda:draw_spectrumCircle(canvas, algorithm_combobox, h,
                            x_spektrum, y_spektrum, Rn, Rk, step, amount, color_line[1]))
        button_time.config(command=lambda:time_comparison(canvas, color_line[1], 'circle'))

def check_hide(hide):
    Rn.configure(state=NORMAL)
    Rk.configure(state=NORMAL)
    step.configure(state=NORMAL)
    amount.configure(state=NORMAL)
    if hide == 0:
        Rn.configure(state=DISABLED)
    elif hide == 1:
        Rk.configure(state=DISABLED)
    elif hide == 2:
        step.configure(state=DISABLED)
    else:
        amount.configure(state=DISABLED)

def clear_canvas(canvas):
    canvas.delete("all")
    build_canvas(canvas)

window = Tk()
window.title("Лабораторная работа №3")
window.geometry("1530x780+0+0")
window["bg"] = "#D9D8D7"

menu = Menu(window, font="TkMenuFont")

menu.add_command(label=AUTHOR_TITLE, command=lambda: box.showinfo(AUTHOR_TITLE, AUTHOR))
menu.add_command(label='Выход', command=window.destroy)

window.configure(menu=menu)

canvas = Canvas(window)
canvas.place(relx = 0, rely=0, relheight=1, relwidth=0.713)
canvas.configure(background="#ffffff")
canvas.configure(borderwidth="2")
canvas.configure(highlightbackground="#ffffff")
canvas.configure(insertbackground="#ffffff")
canvas.configure(relief="raised")
canvas.configure(selectbackground="#2908ff")
canvas.configure(selectforeground="#ffffff")
canvas.addtag_all("all")

build_canvas(canvas)

Label(text = "АЛГОРИТМ", font = ("Arial", 16, "bold"), bg = "#00B3FF",
    fg = "white").place(relx = 0.713, rely=0, relheight=0.04, relwidth=0.3)

list_algorithm = ['Канонического уравнения', 'Параметрического уравнения', 'Алгоритм средней точки', 'Алгоритм Брезенхем', 'Алгоритм библиотеки']
algorithm_combobox = ttk.Combobox(values=list_algorithm, font = ("Arial", 15))
algorithm_combobox.place(relx = 0.753, rely=0.05, relheight=0.05, relwidth=0.2)
algorithm_combobox.current(0)

Label(text = "ЗАДАНО ЦВЕТ", font = ("Arial", 16, "bold"), bg = "#00B3FF",
    fg = "white").place(relx = 0.713, rely=0.11, relheight=0.04, relwidth=0.3)

button = Button(window)
button.configure(text="Цвет фона", font = ("Arial", 15), command=lambda: choose_color_background(canvas, button))
button.place(relx=0.753, rely=0.16, relheight=0.05, relwidth=0.1)

buttonColor = Button(window)
buttonColor.configure(text="Цвет линий", font = ("Arial", 15), command=lambda: choose_color_line(buttonColor))
buttonColor.place(relx=0.87, rely=0.16, relheight=0.05, relwidth=0.1)

Label(text = "ПОСТРОЕНИЕ", font = ("Arial", 16, "bold"), bg = "#00B3FF",
    fg = "white").place(relx = 0.713, rely=0.22, relheight=0.04, relwidth=0.3)

Label(text = "Фигура: ", font = ("Arial", 15), bg = "#D9D8D7",
    fg = "#29293d").place(relx = 0.713, rely=0.27, relheight=0.05, relwidth=0.1)

t = IntVar()
t.set(0)
radbutton1 = Radiobutton(text="Окружность", variable=t, value=0, font = ("Arial", 15), bg = "#D9D8D7", fg = "#29293d", 
                         command=lambda: check_button(t.get()))
radbutton1.place(relx = 0.793, rely=0.27, relheight=0.05, relwidth=0.1)

radbutton2 = Radiobutton(text="Эллипс", variable=t, value=1, font = ("Arial", 15), bg = "#D9D8D7", fg = "#29293d",        
                            command=lambda: check_button(t.get()))
radbutton2.place(relx = 0.9, rely=0.27, relheight=0.05, relwidth=0.06)

Label(text = "X", font = ("Arial", 13), bg = "#D9D8D7",
    fg = "#29293d").place(relx = 0.82, rely=0.335, relheight=0.03, relwidth=0.05)
Label(text = "Y", font = ("Arial", 13), bg = "#D9D8D7",
    fg = "#29293d").place(relx = 0.89, rely=0.335, relheight=0.03, relwidth=0.05)

Label(text = "Центр: ", font = ("Arial", 15), bg = "#D9D8D7",
    fg = "#29293d").place(relx = 0.713, rely=0.35, relheight=0.03, relwidth=0.1)

xc = Entry(font = ("Arial", 15))
xc.place(relx = 0.82, rely=0.36, relheight=0.04, relwidth=0.05)

yc = Entry(font = ("Arial", 15))
yc.place(relx = 0.89, rely=0.36, relheight=0.04, relwidth=0.05)


label_Ry = Label(text = "Ry", font = ("Arial", 13), bg = "#D9D8D7", fg = "#29293d")
rb = Entry(font = ("Arial", 15))


label_Rx = Label(text = "R", font = ("Arial", 13), bg = "#D9D8D7", fg = "#29293d")
label_Rx.place(relx = 0.82, rely=0.405, relheight=0.03, relwidth=0.05)

Label(text = "Радиус: ", font = ("Arial", 15), bg = "#D9D8D7",
    fg = "#29293d").place(relx = 0.713, rely=0.415, relheight=0.03, relwidth=0.1)

r = Entry(font = ("Arial", 15))
r.place(relx = 0.82, rely=0.43, relheight=0.04, relwidth=0.05)

button1 = Button(text = "Построить окружность", font = ("Arial", 15), 
    highlightbackground = "#b3b3cc", highlightthickness = 30, fg = "#33334d",
    command = lambda:draw_circle(canvas, algorithm_combobox, xc, yc, r, color_line[1], True))
button1.place(relx = 0.75, rely=0.49, relheight=0.05, relwidth=0.2)

Label(text = "ПОСТРОЕНИЕ СПЕКТРА", font = ("Arial", 16, "bold"), bg = "#00B3FF",
    fg = "white").place(relx = 0.713, rely=0.545, relheight=0.04, relwidth=0.3)

h = IntVar()
h.set(1)
radbutton3 = Radiobutton(text="Rн", variable=h, value=0, font = ("Arial", 15), bg = "#D9D8D7", fg = "#29293d", 
                         command=lambda: check_hide(h.get()))
radbutton3.place(relx = 0.723, rely=0.59, relheight=0.05, relwidth=0.05)

radbutton4 = Radiobutton(text="Rк", variable=h, value=1, font = ("Arial", 15), bg = "#D9D8D7", fg = "#29293d",        
                            command=lambda: check_hide(h.get()))
radbutton4.place(relx = 0.79, rely=0.59, relheight=0.05, relwidth=0.05)
radbutton5 = Radiobutton(text="шаг", variable=h, value=2, font = ("Arial", 15), bg = "#D9D8D7", fg = "#29293d", 
                         command=lambda: check_hide(h.get()))
radbutton5.place(relx = 0.86, rely=0.59, relheight=0.05, relwidth=0.05)

radbutton6 = Radiobutton(text="Кол", variable=h, value=3, font = ("Arial", 15), bg = "#D9D8D7", fg = "#29293d",        
                            command=lambda: check_hide(h.get()))
radbutton6.place(relx = 0.93, rely=0.59, relheight=0.05, relwidth=0.05)

center = Label(text = "Центр", font = ("Arial", 15), bg = "#D9D8D7",
    fg = "#29293d")
center.place(relx = 0.783, rely=0.64, relheight=0.04, relwidth=0.04)

x_spektrum = Entry(font = ("Arial", 15))
x_spektrum.place(relx = 0.835, rely=0.64, relheight=0.04, relwidth=0.05)

y_spektrum = Entry(font = ("Arial", 15))
y_spektrum.place(relx = 0.885, rely=0.64, relheight=0.04, relwidth=0.05)

label_rn = Label(text = "Rн: ", font = ("Arial", 15), bg = "#D9D8D7",
    fg = "#29293d")
label_rn.place(relx = 0.743, rely=0.69, relheight=0.04, relwidth=0.04)

Rn = Entry(font = ("Arial", 15))
Rn.place(relx = 0.775, rely=0.69, relheight=0.04, relwidth=0.05)

label_rk = Label(text = "Rк: ", font = ("Arial", 15), bg = "#D9D8D7",
    fg = "#29293d")
label_rk.place(relx = 0.883, rely=0.69, relheight=0.04, relwidth=0.04)

Rk = Entry(font = ("Arial", 15))
Rk.configure(state=DISABLED)
Rk.place(relx = 0.915, rely=0.69, relheight=0.04, relwidth=0.05)

label_step = Label(text = "Шаг: ", font = ("Arial", 15), bg = "#D9D8D7",
    fg = "#29293d")
label_step.place(relx = 0.743, rely=0.74, relheight=0.04, relwidth=0.04)

step = Entry(font = ("Arial", 15))
step.place(relx = 0.775, rely=0.74, relheight=0.04, relwidth=0.05)

label_number = Label(text = "Кол: ", font = ("Arial", 15), bg = "#D9D8D7",
    fg = "#29293d")
label_number.place(relx = 0.883, rely=0.74, relheight=0.04, relwidth=0.04)

amount = Entry(font = ("Arial", 15))
amount.place(relx = 0.915, rely=0.74, relheight=0.04, relwidth=0.05)

button_spek = Button(text = "Построить cпектр", font = ("Arial", 15), 
    highlightbackground = "#b3b3cc", highlightthickness = 30, 
    fg = "#33334d", command = lambda:draw_spectrumCircle(canvas, algorithm_combobox, h,
                            x_spektrum, y_spektrum, Rn, Rk, step, amount, color_line[1]))
button_spek.place(relx = 0.75, rely=0.82, relheight=0.05, relwidth=0.2)

button_time = Button(text = "Исследование По Времени", font = ("Arial", 15), 
    highlightbackground = "#d1d1e0", highlightthickness = 30, fg = "#33334d",
    command=lambda:time_comparison(canvas, color_line[1], 'circle'))
button_time.place(relx = 0.75, rely=0.88, relheight=0.05, relwidth=0.2)

Button(text = "Очистить", font = ("Arial", 15), 
    highlightbackground = "#b3b3cc", highlightthickness = 30, fg = "#33334d",
    command=lambda:clear_canvas(canvas)).\
    place(relx = 0.81, rely=0.95, relheight=0.05, relwidth=0.1)

xc.insert(0, 0)
yc.insert(0, 0)
r.insert(0, 200)
rb.insert(0, 100)
x_spektrum.insert(0, 0)
y_spektrum.insert(0, 0)
Rn.insert(0, 100)
Rk.insert(0, 200)
step.insert(0, 4)
amount.insert(0, 20)
window.mainloop()
