from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as box
from math import *
from process import *

count = 0
listPoints = []
def show_info(str):
    box.showinfo("Информация", str)

def show_error(str):
    box.showerror("Ошибка", str)

def show_warn(str):
    box.showwarning("Предупреждение", str)

def show_info_author():
    show_info("Ву Хай Данг ИУ7И-42Б")

def show_info_program():
    show_info("Дано множество точек. \nНайти такой треуголник с вершинами в этих точке, у которого высота имеет максимальную длину (Берет один из трех высот, длина которой максимальна.)")

def confirm():
    answer = box.askyesno(title='Подтверждение', message="Вы хотите, сразу завершать программу?")
    if answer:
        window.destroy()

def clear_table():
    for item in table.get_children():
        table.delete(item)

def numbers_points():
    try:
        x = int(E1.get())
    except:
        show_error("Количество точек должен быть число")
        confirm()
        return 
    
    if (x < 0):
        show_error("Количество точек должен быть целое число")
        confirm()
        return 
    return x

def write_to_table():
    clear_table()
    for i in range(count):
        table.insert("", "end", values=(str(i + 1), str(listPoints[i][0]), str(listPoints[i][1])))

def coeffi_scale(list_triangle, list_altitude_max):
    x_max = list_triangle[0][0][0]
    x_min = list_triangle[0][0][0]
    y_max = list_triangle[0][0][1]
    y_min = list_triangle[0][0][1]

    for triangle in list_triangle:
        for i in range(len(triangle)):
            x_max = max(x_max, triangle[i][0])
            x_min = min(x_min, triangle[i][0])
            y_max = max(y_max, triangle[i][1])
            y_min = min(y_min, triangle[i][1])

    # for x in list_altitude_max:
    #     for i in range(len(x)):
    #         print(x)
    #         x_max = max(x_max, triangle[i][0])
    #         x_min = min(x_min, triangle[i][0])
    #         y_max = max(y_max, triangle[i][1])
    #         y_min = min(y_min, triangle[i][1])

    kx = (1000 - 0) / (x_max - x_min + 40) # chia 10
    ky = (800 - 0) / (y_max - y_min + 40)  # chia 10
    return min(kx, ky)

def draw_point(point, number, limits):
    #Коэффициент масштабирования Кx, Ky.
    # k = coeffi_scale()

    x = round(point[0], 2)
    y = round(point[1], 2) 
    point_img = translate_to_comp(point, limits)
    canvas.create_oval(point_img[0] - 2, point_img[1] - 2, point_img[0] + 2, point_img[1] + 2, fill = "blue", tags="point")
    canvas.create_text(point_img[0], point_img[1] + 7, text=str(number)+".(" + str(point[0])+","+str(point[1])+")", fill="black", tags="point")

def add_point():
    #numbers = numbers_points()
    # if (numbers == None):
    #     return
    try:
        temp = [float(x) for x in E2.get().split(maxsplit=1)]
    except:
        show_error("Не верно координаты точки")
        confirm()
        return 
    if (len(temp) == 0):
        show_error("Пустой ввод")
        confirm()
        return 

    # if (len(listPoints) == numbers):
    #     show_error("Достаточно количество точек, не монжо добавить.")
    #     confirm()
    #     return 
    x = round(temp[0], 3)
    y = round(temp[1], 3)

    global count
    listPoints.append(temp)
    count = count + 1
    table.insert("", "end", values=(str(count), str(x), str(y)))
    E2.delete(0, END)
    E3.delete(0, END)

def del_point():
    # numbers = numbers_points()
    # if (numbers == None):
    #     return
    try:
        temp = [float(x) for x in E2.get().split(maxsplit=1)]
    except:
        show_error("Не верно координаты точки")
        confirm()
        return 

    if (len(temp) == 0):
        show_error("Пустой ввод")
        confirm()
        return 

    x = round(temp[0], 3)
    y = round(temp[1], 3)

    if temp not in listPoints:
        show_warn("Эта точка не нашел в таблице")

    global count
    while temp in listPoints:
        listPoints.remove(temp)
    count = len(listPoints)
    write_to_table()
    # canvas.delete("point")
    # canvas.delete("triangle")
    # canvas.delete("altitude")
    # canvas.delete("line")
    # for i in range(len(listPoints)):
    #     draw_point(listPoints[i], i + 1)
    E2.delete(0, END)
    E3.delete(0, END)

def replace_point():
    # numbers = numbers_points()
    # if (numbers == None):
    #     return
    try:
        temp1 = [float(x) for x in E2.get().split(maxsplit=1)]
        temp2 = [float(x) for x in E3.get().split(maxsplit=1)]
    except:
        show_error("Не верно координаты точки")
        confirm()
        return 

    if (len(temp1) == 0 or len(temp2) == 0):
        show_error("Пустой ввод")
        confirm()
        return 

    x1 = round(temp1[0], 3)
    y1 = round(temp1[1], 3)
    x2 = round(temp2[0], 3)
    y2 = round(temp2[1], 3)

    if temp1 not in listPoints:
        show_warn("Эта точка не нашел в таблице")
        confirm()

    for i in range(len(listPoints)):
        if (listPoints[i] == temp1):
            listPoints[i] = temp2

    write_to_table()
    # canvas.delete("point")
    # canvas.delete("altitude")
    # for i in range(len(listPoints)):
    #     draw_point(listPoints[i], i + 1)
    E2.delete(0, END)
    E3.delete(0, END)

def draw_triangle(pointA, pointB, pointC):

    x1 = round(pointA[0], 2)
    y1 = round(pointA[1], 2) 
    x2 = round(pointB[0], 2)
    y2 = round(pointB[1], 2) 
    x3 = round(pointC[0], 2)
    y3 = round(pointC[1], 2) 
    canvas.create_polygon(x1, y1, x2, y2, x3, y3, fill='', outline='red', tags="triangle")

def draw_altitude(list_altitudes_comp, list_altitudes_max, triangle_comp, point_name, color):
    count1 = 0
    
    for i in range(0, len(list_altitudes_comp), 2):
        temp_x1 = round(list_altitudes_comp[i][0], 2)
        temp_y1 = round(list_altitudes_comp[i][1], 2)
        temp_x2 = round(list_altitudes_comp[i + 1][0], 2) 
        temp_y2 = round(list_altitudes_comp[i + 1][1], 2)
        canvas.create_oval(temp_x2 - 2, temp_y2 - 2, temp_x2 + 2, temp_y2 + 2, fill = "black", tags="altitude")
        canvas.create_text(temp_x2, temp_y2 - 7, text=point_name + str(count1) + ".(" + str(list_altitudes_max[i + 1][0])+","+str(list_altitudes_max[i + 1][1])+")", fill="black", tags="altitude")
        count1 += 1
        canvas.create_line(temp_x1, temp_y1, temp_x2, temp_y2, fill=color, tags="line")
    
def draw_ext(list_altitudes_comp, triangle_comp):
    for i in range(0, len(list_altitudes_comp), 2):
        temp_x2 = round(list_altitudes_comp[i + 1][0], 2) 
        temp_y2 = round(list_altitudes_comp[i + 1][1], 2)
        for v in triangle_comp:
            canvas.create_line(v[0], v[1], temp_x2,temp_y2, fill="yellow", tags="line", dash=(1, 1))
            draw_triangle(triangle_comp[0], triangle_comp[1], triangle_comp[2])

def point_to_str(point):
    return "(" + str(point[0]) + "," + str(point[1]) + ")"

def info_solution(list_triangle, list_altitudes_max):
    st = "Результирующий треугольник построен на точках: "
    for i in range(len(list_triangle)):
        if i != 0:
            st = st + "; еще треугольник построен на точках: "
        st = st + " с номерами " + str(listPoints.index(list_triangle[i][0]) + 1) + ' с координатами ' + point_to_str(list_triangle[i][0]) 
        st = st + ", " + " с номерами " + str(listPoints.index(list_triangle[i][1]) + 1) + ' с координатами ' + point_to_str(list_triangle[i][1])
        st = st + ", " + " с номерами " + str(listPoints.index(list_triangle[i][2]) + 1) + ' с координатами ' + point_to_str(list_triangle[i][2])

    st = st + ".\nДлина максимальной высоты (Зеленный свет) треуголники: " + str(distance_two_point(list_altitudes_max[0][0], list_altitudes_max[0][1]))
    st = st + ".\nДругие высоты (не максимальные) - это синий; если высоты находятся вне треуголника то нарисовал больше желтого расширения края по направлению к высоте."
    return st

def get_limits(list_triangle, list_altitudes_max, list_altitudes_norm):
    limits = [[list_triangle[0][0][0], list_triangle[0][0][1]], [list_triangle[0][0][0], list_triangle[0][0][1]]]

    for triangle in list_triangle:
        for point in triangle:
            if point[0] < limits[0][0]:
                limits[0][0] = point[0]

            if point[0] > limits[1][0]:
                limits[1][0] = point[0]

            if point[1] < limits[0][1]:
                limits[0][1] = point[1]

            if point[1] > limits[1][1]:
                limits[1][1] = point[1]

    for list_altitudes in list_altitudes_max:
        for point in list_altitudes:
            if point[0] < limits[0][0]:
                limits[0][0] = point[0]

            if point[0] > limits[1][0]:
                limits[1][0] = point[0]

            if point[1] < limits[0][1]:
                limits[0][1] = point[1]

            if point[1] > limits[1][1]:
                limits[1][1] = point[1]
    for list_altitudes in list_altitudes_norm:
        for point in list_altitudes:
            if point[0] < limits[0][0]:
                limits[0][0] = point[0]

            if point[0] > limits[1][0]:
                limits[1][0] = point[0]

            if point[1] < limits[0][1]:
                limits[0][1] = point[1]

            if point[1] > limits[1][1]:
                limits[1][1] = point[1]

    for i in range(2):
        limits[i][0] -= (limits[(i + 1) % 2][0] - limits[i][0]) * 0.05
        limits[i][1] -= (limits[(i + 1) % 2][1] - limits[i][1]) * 0.05

    return limits

def translate_to_comp(point, limits):
    scale = min(1000 / (limits[1][0] - limits[0][0]), 750 / (limits[1][1] - limits[0][1]))
    x = int((point[0] - limits[0][0]) * scale)
    y = int(750 - (point[1] - limits[0][1]) * scale)
    
    return [x, y]
def limit_exp():
    limits = [[listPoints[0][0], listPoints[0][1]], [listPoints[0][0], listPoints[0][1]]]

    for point in listPoints:
        if point[0] < limits[0][0]:
            limits[0][0] = point[0]

        if point[0] > limits[1][0]:
            limits[1][0] = point[0]

        if point[1] < limits[0][1]:
            limits[0][1] = point[1]

        if point[1] > limits[1][1]:
            limits[1][1] = point[1]

    for i in range(2):
        limits[i][0] -= (limits[(i + 1) % 2][0] - limits[i][0]) * 0.05
        limits[i][1] -= (limits[(i + 1) % 2][1] - limits[i][1]) * 0.05

    return limits
def draw_exp():
    limits = limit_exp()
    listPoints_comp = []
    for point in listPoints:
        listPoints_comp.append(translate_to_comp(point, limits))
    
    for point in listPoints:
        draw_point(point, listPoints.index(point) + 1, limits)

    for i in range(len(listPoints_comp) - 1):
        canvas.create_line(listPoints_comp[i][0], listPoints_comp[i][1], listPoints_comp[i + 1][0], listPoints_comp[i + 1][1], fill="red", tags='line')

def solution():
    n = len(listPoints)
    if n < 3:
        show_error("Не достаточно точки для создания треугольника")
        confirm()
        return 0
    
    max_altitude = 0
    list_triangle = []
    triangle = []
    altitudes_max = []
    list_altitudes_max = []
    list_altitudes_norm = []
    for i in range(0,n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if (check_triangle(listPoints[i], listPoints[j], listPoints[k]) == True):
                    list_altitudes, list_norm_altitudes_temp = find_altitudes_triangle(listPoints[i], listPoints[j], listPoints[k])
                    altitude = distance_two_point(list_altitudes[0], list_altitudes[1])
                    if (fabs(altitude - max_altitude) <= EPS):
                        triangle = [listPoints[i], listPoints[j], listPoints[k]]
                        altitudes_max = list_altitudes
                        list_triangle.append(triangle)
                        list_altitudes_max.append(altitudes_max)
                        list_altitudes_norm.append(list_norm_altitudes_temp)
                    elif (altitude - max_altitude >= EPS):
                        list_altitudes_max = []
                        list_altitudes_norm = []
                        list_triangle = []
                        max_altitude = altitude
                        triangle = [listPoints[i], listPoints[j], listPoints[k]]
                        altitudes_max = list_altitudes
                        list_altitudes_max.append(altitudes_max)
                        list_triangle.append(triangle)
                        list_altitudes_norm.append(list_norm_altitudes_temp)
    
    canvas.delete("triangle")
    canvas.delete("line")
    canvas.delete("altitude")
    canvas.delete("point")
    if max_altitude == 0:
        draw_exp()
        show_warn("Не могу создать треугольник")
        return 0
    limits = get_limits(list_triangle, list_altitudes_max, list_altitudes_norm)

    for point in listPoints:
        draw_point(point, listPoints.index(point) + 1, limits)
    
    list_triangle_comp = list()
    triangle_comp = list()
    list_max_altitudes_comp = list()
    altitudes_comp = list()
    list_norm_altitudes_comp = list()
    for i in range(len(list_triangle)):
        for j in range(3):
            # draw_point(list_triangle[i][j], listPoints.index(list_triangle[i][j]) + 1, limits)
            triangle_comp.append(translate_to_comp(list_triangle[i][j], limits))
        list_triangle_comp.append(triangle_comp)
        triangle_comp = []
        for j in range(len(list_altitudes_max[i])):
            altitudes_comp.append(translate_to_comp(list_altitudes_max[i][j], limits))
        list_max_altitudes_comp.append(altitudes_comp)
        altitudes_comp = []
        for j in range(len(list_altitudes_norm[i])):
            altitudes_comp.append(translate_to_comp(list_altitudes_norm[i][j], limits))
        list_norm_altitudes_comp.append(altitudes_comp)
        altitudes_comp = []

    for i in range(len(list_triangle_comp)):
        # draw_triangle(list_triangle_comp[i][0], list_triangle_comp[i][1], list_triangle_comp[i][2])
        draw_ext(list_max_altitudes_comp[i], list_triangle_comp[i])
        draw_ext(list_norm_altitudes_comp[i], list_triangle_comp[i])
        draw_altitude(list_max_altitudes_comp[i], list_altitudes_max[i], list_triangle_comp[i], 'H', 'green')
        draw_altitude(list_norm_altitudes_comp[i], list_altitudes_norm[i], list_triangle_comp[i], 'K', "blue")
    show_info(info_solution(list_triangle, list_altitudes_max))

def Enter(event):
    solution()

def clear_all():
    global count, listPoints
    count = 0
    listPoints = []
    canvas.delete("point")
    canvas.delete("altitude")
    canvas.delete("triangle")
    canvas.delete("line")
    clear_table()
    # E1.delete(0, END)
    E2.delete(0, END)
    E3.delete(0, END)

def motion(event):
    x, y = event.x, event.y
    print('{}, {}'.format(x, y))

window = Tk()
window.geometry("1550x800+-10+0")

window.title("Lab 1")

menubar = Menu(window)
# author = Menu(menubar, tearoff=0)
menubar.add_command(label='О авторе', command=show_info_author)
# program = Menu(menubar, tearoff=0)
menubar.add_command(label='О программе', command=show_info_program)
window.config(menu=menubar)

# window.bind('<Motion>', motion)

frame_left = Frame(window, width = 1000, height = 800, background= "blue")
frame_left.grid(row = 0, column = 0, padx=10, pady = 10, sticky="nsew")

canvas = Canvas(window, width=1000, height=800, background="white")
canvas.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

# Рисуем координатные оси.
canvas.create_line(15, 750, 1000, 750, fill="black", width=2, arrow=LAST,
                    arrowshape="10 20 10")
canvas.create_line(15, 0, 15, 750, fill="black", width=2, arrow=FIRST,
                    arrowshape="10 20 10")

# label_1 = Label(window, text="Количество точек", font="Arial 16")
# label_1.place(x=1150, y=10)
# E1 = Entry(width=20, font="Arial 16")
# E1.place(x=1150, y=50)

label_2 = Label(window, text="Координат точек", font="Arial 16")
label_2.place(x=1180, y=55)
E2 = Entry(width=20, font="Arial 16")
E2.place(x=1150, y=100)

label_3 = Label(window, text="==>", font="Arial 16")
label_3.place(x=1100, y=150)
E3 = Entry(width=20, font="Arial 16")
E3.place(x=1150, y=150)

button_1 = Button(window, text="Добавить", font="Arial 16", command= add_point)
button_1.place(x=1200, y=200)
button_2 = Button(window, text="Удалить", font="Arial 16", command=del_point)
button_2.place(x=1205, y=250)
button_3 = Button(window, text="Изменить", font="Arial 16", command=replace_point)
button_3.place(x=1200, y=300)

window.bind('<Return>', Enter)

label_4 = Label(window, text="Множество точек", font="Arial 16")
label_4.place(x=1170, y=380)

table = ttk.Treeview(window)
table['columns'] = ("Id", "X", "Y")
table.column("#0", width=0,  stretch=NO)
table.column("Id",anchor=CENTER, width=50)
table.column("X",anchor=CENTER,width=80)
table.column("Y",anchor=CENTER,width=80)

table.heading("#0",text="",anchor=CENTER)
table.heading("Id",text="№",anchor=CENTER)
table.heading("X",text="X",anchor=CENTER)
table.heading("Y",text="Y",anchor=CENTER)
table.place(x=1150, y=420)

button_4 = Button(window, text="Решить", font="Arial 16", command=solution)
button_4.place(x=1210, y=650)
button_5 = Button(window, text="Очистить", font="Arial 16", command=clear_all)
button_5.place(x=1200, y=700)

window.mainloop()