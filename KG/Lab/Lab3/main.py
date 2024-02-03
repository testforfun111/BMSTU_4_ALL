from tkinter import *
from tkinter import ttk
import draw
from comparisons import *
import tkinter.messagebox as box
from tkinter import colorchooser

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

def main():
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
    
    list_algorithm = ['ДДА', 'Брезенхем (float)', 'Брезенхем (int)', 'Брезенхем (устр. ступенчатости)', 'Ву', 'Библиотека']
    algorithm_combobox = ttk.Combobox(values=list_algorithm, font = ("Arial", 15))
    algorithm_combobox.place(relx = 0.753, rely=0.05, relheight=0.05, relwidth=0.2)
    algorithm_combobox.current(0)

    Label(text = "ЗАДАНО ЦВЕТ", font = ("Arial", 16, "bold"), bg = "#00B3FF",
        fg = "white").place(relx = 0.713, rely=0.11, relheight=0.04, relwidth=0.3)

    button = Button(window)
    button.configure(text="Цвет фона", font = ("Arial", 15), command=lambda: choose_color_background(canvas, button))
    button.place(relx=0.753, rely=0.16, relheight=0.05, relwidth=0.1)

    button1 = Button(window)
    button1.configure(text="Цвет линий", font = ("Arial", 15), command=lambda: choose_color_line(button1))
    button1.place(relx=0.87, rely=0.16, relheight=0.05, relwidth=0.1)

    Label(text = "ПОСТРОЕНИЕ ОТРЕЗКА", font = ("Arial", 16, "bold"), bg = "#00B3FF",
        fg = "white").place(relx = 0.713, rely=0.22, relheight=0.04, relwidth=0.3)


    Label(text = "Начальная: ", font = ("Arial", 15), bg = "#D9D8D7",
        fg = "#29293d").place(relx = 0.713, rely=0.276, relheight=0.03, relwidth=0.1)

    x_beg_entry = Entry(font = ("Arial", 15))
    x_beg_entry.place(relx = 0.82, rely=0.276, relheight=0.04, relwidth=0.05)

    y_beg_entry = Entry(font = ("Arial", 15))
    y_beg_entry.place(relx = 0.89, rely=0.276, relheight=0.04, relwidth=0.05)

    Label(text = "Конечная: ", font = ("Arial", 15), bg = "#D9D8D7",
        fg = "#29293d").place(relx = 0.713, rely=0.33, relheight=0.03, relwidth=0.1)
    
    x_end_entry = Entry(font = ("Arial", 15))
    x_end_entry.place(relx = 0.82, rely=0.33, relheight=0.04, relwidth=0.05)

    y_end_entry = Entry(font = ("Arial", 15))
    y_end_entry.place(relx = 0.89, rely=0.33, relheight=0.04, relwidth=0.05)

    # Button(highlightbackground = "#00B3FF", highlightthickness = 30, fg = "#D9D8D7", state = DISABLED).\
    #     place(relx = 0.75, rely=0.52, relheight=0.04, relwidth=0.2)

    Button(text = "Построить отрезок", font = ("Arial", 15), 
        highlightbackground = "#b3b3cc", highlightthickness = 30, fg = "#33334d",
        command = lambda: draw.draw_line(canvas, color_line, color_bg, algorithm_combobox,
            x_beg_entry, y_beg_entry, x_end_entry, y_end_entry)).\
        place(relx = 0.75, rely=0.39, relheight=0.05, relwidth=0.2)

    Label(text = "ПОСТРОЕНИЕ СПЕКТРА", font = ("Arial", 16, "bold"), bg = "#00B3FF",
        fg = "white").place(relx = 0.713, rely=0.45, relheight=0.04, relwidth=0.3)

    Label(text = "Центра спектра: ", font = ("Arial", 15), bg = "#D9D8D7",
        fg = "#29293d").place(relx = 0.713, rely=0.5, relheight=0.04, relwidth=0.14)
    
    x_spek_entry = Entry(font = ("Arial", 15))
    x_spek_entry.place(relx = 0.85, rely=0.5, relheight=0.04, relwidth=0.05)

    y_spek_entry = Entry(font = ("Arial", 15))
    y_spek_entry.place(relx = 0.92, rely=0.5, relheight=0.04, relwidth=0.05)

    Label(text = "Угол поворота:", font = ("Arial", 15), bg = "#D9D8D7",
        fg = "#29293d").place(relx = 0.713, rely=0.55, relheight=0.04, relwidth=0.14)

    angle_entry = Entry(font = ("Arial", 15))
    angle_entry.place(relx = 0.87, rely=0.55, relheight=0.04, relwidth=0.05)

    Label(text = "Длина отрезка:", font = ("Arial", 15), bg = "#D9D8D7",
        fg = "#29293d").place(relx = 0.713, rely=0.6, relheight=0.04, relwidth=0.14)

    radius_entry = Entry(font = ("Arial", 15))
    radius_entry.place(relx = 0.87, rely=0.6, relheight=0.04, relwidth=0.05)

    # Button(highlightbackground = "#00B3FF", highlightthickness = 30, fg = "#D9D8D7", state = DISABLED).\
    #     place(relx = 0.75, rely=0.72, relheight=0.04, relwidth=0.2)

    Button(text = "Построить cпектр", font = ("Arial", 15), 
        highlightbackground = "#b3b3cc", highlightthickness = 30, fg = "#33334d",
        command = lambda: draw.draw_spectrum(canvas, x_spek_entry, y_spek_entry, color_line, color_bg, algorithm_combobox, angle_entry, radius_entry)).\
        place(relx = 0.75, rely=0.66, relheight=0.05, relwidth=0.2)


    # Button(highlightbackground = "#00B3FF", highlightthickness = 30, fg = "#D9D8D7", state = DISABLED).\
    #     place(relx = 0.75, rely=0.77, relheight=0.04, relwidth=0.2)

    Label(text = "ИССЛЕДОВАНИЕ", font = ("Arial", 16, "bold"), bg = "#00B3FF",
        fg = "white").place(relx = 0.713, rely=0.72, relheight=0.04, relwidth=0.3)

    Button(text = "По Времени", font = ("Arial", 15), 
        highlightbackground = "#d1d1e0", highlightthickness = 30, fg = "#33334d",
        command = lambda: time_comparison(canvas, color_line, color_bg, x_spek_entry, y_spek_entry, angle_entry, radius_entry)).\
        place(relx = 0.8, rely=0.78, relheight=0.05, relwidth=0.12)


    # Button(highlightbackground = "#00B3FF", highlightthickness = 30, fg = "#D9D8D7", state = DISABLED).\
    #     place(relx = 0.75, rely=0.82, relheight=0.04, relwidth=0.2)

    Button(text = "По Ступенчатости", font = ("Arial", 15), 
        highlightbackground = "#d1d1e0", highlightthickness = 30, fg = "#33334d",
        command = lambda: step_comparison(x_spek_entry, y_spek_entry, radius_entry)).\
        place(relx = 0.8, rely=0.85, relheight=0.05, relwidth=0.12)


    # Button(highlightbackground = "#00B3FF", highlightthickness = 30, fg = "#D9D8D7", state = DISABLED).\
    #     place(relx = 0.75, rely=0.87, relheight=0.04, relwidth=0.2)

    Button(text = "Очистить", font = ("Arial", 15), 
        highlightbackground = "#b3b3cc", highlightthickness = 30, fg = "#33334d",
        command = lambda: draw.clear_canvas(canvas)).\
        place(relx = 0.81, rely=0.93, relheight=0.05, relwidth=0.1)

    angle_entry.insert(0, 10)
    radius_entry.insert(0, 200)
    x_spek_entry.insert(0, 0)
    y_spek_entry.insert(0, 0)
    x_beg_entry.insert(0, 0)
    y_beg_entry.insert(0, 0)

    x_end_entry.insert(0, 200)
    y_end_entry.insert(0, 40)

    window.mainloop()

if __name__ == "__main__":
    main()
