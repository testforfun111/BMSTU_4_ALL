# Алгоритм Кируса-Бека

import config as cfg
import tkinter.messagebox as mb


def get_vector(points):
    return cfg.Vector(points[1].x - points[0].x, points[1].y - points[0].y)

def vector_mul(vector_1, vector_2):
    return vector_1.x * vector_2.y - vector_1.y * vector_2.x


def scalar_mul(vector_1, vector_2):
    return vector_1.x * vector_2.x + vector_1.y * vector_2.y


def is_convex(edges):
    if len(edges) < 3:
        return False

    first = vector_mul(get_vector(edges[0]), get_vector(edges[-1]))
    if first > 0:
        sign = 1
    elif first == 0:
        sign = 0
    else:
        sign = -1

    multi = []
    if not first:
        multi.append(first)

    for i in range(1, len(edges)):
        tmp = vector_mul(get_vector(edges[i]), get_vector(edges[i - 1]))
        if multi and not tmp:
            multi.append(tmp)

        if sign * tmp < 0:
            return False

    if len(multi) == len(edges):
        return False
    if sign < 0:
        edges.reverse()

    return True


def get_innomal(edge_1, edge_2):
    vector = get_vector(edge_1)
    if vector.x == 0:
        normal = cfg.Vector(1, 0)
    else:
        normal = cfg.Vector(-vector.y / vector.x, 1)

    if scalar_mul(normal, -get_vector(edge_2)) < 0:
        normal.negative()

    return normal


def get_innomals(edges):
    length = len(edges)
    normals = []
    for i in range(length):
        normals.append(get_innomal(edges[i], edges[(i + 1) % length]))

    return normals

def cyrus_beck_algorithm(canvas, color, cutter, lines):
    normals = get_innomals(cutter) # найти все векторы нормали от граница отсекателя (внутрь)
    for line in lines:
        flag_break = False
        t_start, t_end = 0, 1  # инициализация пределов значений параметра при отрезок полностью видимый

        D = get_vector(line)  # Вектор ориентации отрезка (директрисса)
        for i in range(len(cutter)):
            # Вектор W (fi - вершины многоугольника)
            if cutter[i][0] != line[0]:
                WI = get_vector([cutter[i][0], line[0]])
            else:
                WI = get_vector([cutter[i][1], line[0]])

            Dck = scalar_mul(D, normals[i])
            Wck = scalar_mul(WI, normals[i])

            # проверка отрезок параллельно i-ой стороне отсекателя
            if Dck == 0:
                if Wck < 0:
                    flag_break = True
                    break
                else:
                    continue

            t = -Wck / Dck
            
            if Dck > 0:
                if t > 1:   
                    flag_break = True
                    break
                t_start = max(t_start, t)
            elif (Dck < 0):
                if (t < 0): 
                    flag_break = True 
                    break 
                t_end = min(t_end, t)

            # Проверка фактической видимости отсеченного отрезка
            if t_start > t_end:
                break
        
        if flag_break:
            continue

        if t_start < t_end:
            canvas.draw_line(cfg.int_n(line[0].x + D.x * t_start), cfg.int_n(line[0].y + D.y * t_start),
                             cfg.int_n(line[0].x + D.x * t_end), cfg.int_n(line[0].y + D.y * t_end),
                             color, 'result')
            
def process(canvas, cutter, lines):
    if canvas.start and canvas.old and canvas.start != canvas.old:
        mb.showerror('Ошибка', 'Перед использованием алгоритма необходимо замкнуть область')
        return None

    if not is_convex(cutter):
        mb.showerror('Ошибка', 'Многоугольник должен быть выпуклым')
        return None

    color = canvas.frame.colors['result']
    verteces = []
    for edge in cutter:
        verteces.extend([edge[0].x, edge[0].y])
    canvas.create_polygon(*verteces, outline=canvas.frame.colors['cutter'], fill='white', tag='result')

    cyrus_beck_algorithm(canvas, color, cutter, lines)

