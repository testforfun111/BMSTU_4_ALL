from math import *
from gauss_method import *
from newton import newton_interpolate


def func(data, x, y, nx, ny):
    return newton_interpolate(data, x, y, nx, ny)

# Формула границы
def func_border(x):
    # return 1 - x
    return 0


def func_borders():
    return 0, pi / 2
    # return 0, 1


# Полином Лежандра (рекурсивный способ нахождения)
def Legendre(x, n):
    p = [1, x]
    for i in range(2, n + 1):
        p.append(((2 * i - 1) * x * p[i - 1] - (i - 1) * p[i - 2]) / i)

    return p[n]


# Производная полинома Лежандра
def derivative_Legendre(x, n):
    return (n / (1 - x ** 2)) * (Legendre(x, n - 1) - x * Legendre(x, n))


# Поиск корней полинома Лежандра методом Ньютона.
def FindRootLegendre(i, n):
    xn = cos(pi * ((4 * i - 1) / (4 * n + 2)))
    xn1 = xn - Legendre(xn, n) / derivative_Legendre(xn, n)
    while abs(xn1 - xn) > 1e-10:
        xn = xn1
        xn1 = xn - Legendre(xn, n) / derivative_Legendre(xn, n)

    return xn1


# Поиск узлов t
def GetLegendreRoots(n):
    roots = []
    for i in range(1, n + 1):
        roots.append(FindRootLegendre(i, n))

    return roots


# Поиск коэффициентов A
def FindCoefficients(nodes):
    matrix = []
    for i in range(len(nodes)):
        matrix.append([])
        for j in range(len(nodes)):
            matrix[i].append(nodes[j] ** i)
        matrix[i].append((1 - (-1) ** (i + 1)) / (i + 1))

    return gaussMethod(matrix)


# Квадратурная формула Гаусса
def GaussQuadrature(data, phi, m, nx, ny):
    t = GetLegendreRoots(m)
    a = FindCoefficients(t)

    c, d = func_borders()

    sum = 0
    for i in range(m):
        teta = ((d + c) / 2) + ((d - c) / 2) * t[i]
        sum += a[i] * func(data, phi, teta, nx, ny)

    sum = sum * (d - c) / 2

    return sum


# Метод Симпсона.
def Simpson(N, M, data, nx, ny):
    a, b = func_borders()

    step = (b - a) / (N - (N % 2))

    sum = 0
    for i in range(N // 2):
        phi = a + 2 * i * step
        sum += abs(GaussQuadrature(data, phi, M, nx, ny) - func_border(phi))

        phi = a + (2 * i + 1) * step
        sum += abs(4 * GaussQuadrature(data, phi, M, nx, ny) - func_border(phi))

        phi = a + (2 * i + 2) * step
        sum += abs(GaussQuadrature(data, phi, M, nx, ny) - func_border(phi))

    sum = sum * (step / 3)

    return sum


def Result(N, M, data, nx, ny):
    I = Simpson(N, M, data, nx, ny)

    return I
