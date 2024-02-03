from copy import deepcopy

def scalVector(v1, v2):
    return v1[0] * v2[0] + v1[1] * v2[1]

def getVector(point1, point2):
    return [point2[0] - point1[0], point2[1] - point1[1]]

def findNormal(peak1, peak2, peak3):
    normal = [peak2[1] - peak1[1], peak1[0] - peak2[0]]

    if scalVector([peak3[0] - peak2[0], peak3[1] - peak2[1]], normal) < 0:
        normal = [-normal[0], -normal[1]]
    return normal

def isVisiable(point, peak1, peak2, peak3):
    n = findNormal(peak1, peak2, peak3)
    
    if scalVector(n, getVector(peak2, point)) < 0:
        return False
    
    return True

def convertParametric(line, t):
    return [round(line[0][0] + (line[1][0] - line[0][0]) * t), round(line[0][1] + (line[1][1] - line[0][1]) * t)]

def isIntersection(ed1, ed2, peak):
    # ed1 - ребро отсекаемого многоугольника.
    # ed2 - ребро отсекателя.
    # peak - след. вершина отсекателя, нужна для
    # корректного определения нормали
    
    # Определяем видимость вершин относительно рассматриваемого ребра.
    visiable1 = isVisiable(ed1[0], ed2[0], ed2[1], peak)
    visiable2 = isVisiable(ed1[1], ed2[0], ed2[1], peak)
    # Если одна вершина видна, а вторая нет (Есть пересечение).
    # Иначе пересечения нет.
    if not (visiable1 ^ visiable2):
        return False
    # Ищем пересечение
    N = findNormal(ed2[0], ed2[1], peak)
    D = getVector(ed1[0], ed1[1])
    W = getVector(ed2[0], ed1[0])
    # Скалярное произведение D на N.
    DScalar = scalVector(D, N)
    # Скалярное произведение W на N.
    WScalar = scalVector(W, N)
    
    t = -WScalar/DScalar
    
    return convertParametric(ed1, t)

def SutherlandHodgman(cutter, polygon):
    cutter.append(cutter[0])

    cutter.append(cutter[1])
    # Цикл по вершинам отсекателя.
    for i in range(len(cutter) - 2):
        new = []  # новый массив вершин
        
        f = polygon[0]  # Запоминаем первую вершину.
        if isVisiable(f,  cutter[i], cutter[i + 1], cutter[i + 2]):
            new.append(f)
        s = polygon[0]
        # Цикл по вершинам многоугольника
        for j in range(1, len(polygon)):
            # Определяем пересечение текущего ребра отсекателя (cutter[i], cutter[i + 1])
            # И рассматриваемого ребра отсекаемого многоугольника (s, polygon[j]),
            # Где s = polygon[j - 1]. cutter[i + 2] нам нужно, чтобы корректно найти нормаль.
            t = isIntersection([s, polygon[j]], [cutter[i], cutter[i + 1]], cutter[i + 2])
            # Если есть пересечение, то заносим его в новый массив вершин.
            if t:
                new.append(t)
            # Запоминаем в s текущую вершину. (Чтобы на следующем шаге
            # Искать пересечение polygon[j - 1] и polygon[j])
            s = polygon[j]
            # Проверяем, видна ли текущая вершина
            if isVisiable(s, cutter[i], cutter[i + 1], cutter[i + 2]):
                # Если видна, то заносим ее в новый массив вершин.
                new.append(s)
        # Если массив пуст, значит многоугольник невидимый.
        if not len(new):
            return
        t = isIntersection([s, f], [cutter[i], cutter[i + 1]], cutter[i + 2])
        if t:
            new.append(t)
        polygon = deepcopy(new)
    return polygon