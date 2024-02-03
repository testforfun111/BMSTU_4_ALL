import numpy as numpy


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def setX(self, x):
        self.x = x

    def setY(self, y):
        self.x = y

    def printData(self):
        print("[", self.x, self.y,  "]", end=' ')


# константы для работы с массивом данных
x_index = 0  # индекс x
y_index = 1  # индекс y
z_index = 2  # индекс z
matrix_index = 3  # индекс матрицы
infinity = None


# нахождение индекса ближайшей точки по значению к искомой
def prox_index(points, x):
    dif = abs(points[0].x - x)
    index = 0
    for i in range(len(points)):
        if abs(points[i].x - x) < dif:
            dif = abs(points[i].x - x)
            index = i
    return index


# взятие рабочих ближайших точек для расчетов
def get_points(points, index, n):
    left = index
    right = index
    for i in range(n - 1):
        if i % 2 == 0:
            if left == 0:
                right += 1
            else:
                left -= 1
        else:
            if right == len(points) - 1:
                left -= 1
            else:
                right += 1
    return points[left:right + 1]


# расчет полином Ньютона м результаты в виде таблицы всех данных f(xi .... xn)
def newton_table(table):
    row_count = 2
    sub_table = []
    [sub_table.append([point.x, point.y]) for point in table]

    sub_table = list([list(row) for row in numpy.transpose(sub_table)])
    x_data = sub_table[0]
    # Добавление столбцов (строк в моей реализации)
    for i in range(1, len(x_data)):
        sub_table.append([])
        y_row = sub_table[len(sub_table) - row_count]
        # Добавление очередного элемента
        for j in range(0, len(x_data) - i):
            if y_row[j] == infinity and y_row[j + 1] == infinity:
                cur = 1
            elif y_row[j] == infinity:
                cur = y_row[j + 1] / (x_data[j] - x_data[j + i])
            elif y_row[j + 1] == infinity:
                print(2)
                cur = y_row[j] / (x_data[j] - x_data[j + i])
            else:
                cur = (y_row[j] - y_row[j + 1]) / (x_data[j] - x_data[j + i])
            sub_table[i + row_count - 1].append(cur)
    return sub_table


# скомпликтовал в одну функцию
def newton(point_table, n, x):
    table = get_points(point_table, prox_index(point_table, x), n)
    subs = newton_table(table)
    return count_approx(subs, x)


def count_approx(table, x):
    y_x = 0.0
    x_data = table[0]
    for i in range(1, len(table)):
        member_val = table[i][0]
        for j in range(i - 1):
            member_val *= (x - x_data[j])
        y_x += member_val
    return y_x


# двумерная интерполяция Полином Ньютона
def newton_interpolate(data, x, y, nx, ny):
    matrix = data[2]
    x_arr = data[0]
    y_arr = data[1]

    y_values = []
    for i in range(len(y_arr)):
        x_values = []
        for j in range(len(x_arr)):
            x_values.append(Point(x_arr[j], matrix[i][j]))
        y_values.append(Point(y_arr[i], newton(x_values, nx, x)))

    return newton(y_values, ny, y)
