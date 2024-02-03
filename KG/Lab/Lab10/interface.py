from tkinter import *
from tkinter import messagebox as mb


def print_info(string_info):
    mb.showinfo(title="Информация", message=string_info)


def print_error(string_error):
    mb.showerror(title="Ошибка", message=string_error)


def create_button(str, function, coordinates, color = "white"):
    button = Button(text=str, width=30,
                    command=function, font="Times 13", bg = color)
    button.place(x=coordinates[0], y=coordinates[1])


def create_label(root, str, coordinates):
    label = Label(root, text=str, font="Times 13")
    label.place(x=coordinates[0], y=coordinates[1])


def settings_interface(root, size, title):
    root.title(title)
    root.geometry(size)
    # root.configur)
    root.resizable(width=False, height=False)


def option_menu(master, option, coordinates):
    variable = StringVar(master)
    variable.set(option[0])
    w = OptionMenu(master, variable, *option)
    w.place(x=coordinates[0], y=coordinates[1], width=200)
    return variable


def selection(count, list_text, coordinates):
    # Выбор.
    var = IntVar()
    var.set(0)
    list_method = list()

    for i in range(count):
        method = Radiobutton(text=list_text[i], variable=var,
                             value=i, width=25, font="Verdana 12")
        method.place(x=coordinates[0],
                     y=coordinates[1] + 25 * i)
        list_method.append(method)

    return var


def create_entry(root, coordinates, w, text="123"):
    entry = Entry(root, font="Times 14", width=w)
    entry.place(x=coordinates[0], y=coordinates[1])
    entry.insert(0, text)
    return entry


def create_list_box(root, coordinates):
    list_box = Listbox(root, width=48, height=17)
    list_box.insert(END, "(x y)")
    list_box.place(x=coordinates[0], y=coordinates[1])
    scroll = Scrollbar(command=list_box.yview)
    scroll.place(x=coordinates[0] + 390, y=coordinates[1], height=310)
    return list_box


def settings_bind(canvas_class, line_list, contour):
    # Button-1 # ЛКМ
    # Button-3 # ПКМ
    # space # пробел
    canvas_class.canvas.bind(
        "<ButtonPress>", lambda event: canvas_class.keyPress_rectangle(event))

    canvas_class.canvas.bind(
        "<ButtonRelease>", lambda event, arg1=line_list: canvas_class.keyRelease_rectangle(event, line_list, "red"))

    canvas_class.canvas.bind(
        "<Motion>", lambda event: canvas_class.Motion_rectangle(event))

    canvas_class.canvas.bind(
        "<Shift-ButtonPress>", lambda event: canvas_class.keyPress_rectangle(event))

    canvas_class.canvas.bind(
        "<Shift-ButtonRelease>", lambda event, arg1=contour: canvas_class.keyRelease_rectangle(event, arg1, "blue"))

    canvas_class.canvas.bind(
        "<Shift-Motion>", lambda event: canvas_class.Motion_rectangle(event))


def clear(canvas_class, cutter, contour):
    canvas_class.clear_all()

    for i in range(len(cutter) - 1, -1, -1):
        del cutter[i]

    for i in range(len(contour) - 1, -1, -1):
        del contour[i]

    contour.append([])
    cutter.append([])
