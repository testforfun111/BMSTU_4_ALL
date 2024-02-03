from newton import z_index, y_index, x_index, matrix_index, Point


class SplineTuple:
    def __init__(self, a, b, c, d, x):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.x = x


def build_spline(values, n):
    splines = [SplineTuple(0, 0, 0, 0, 0) for _ in range(n - 1)]
    for i in range(0, n - 1):
        splines[i].x = values[i].x
        splines[i].a = values[i].y

    splines[0].c = 0
    splines[n - 2].c = 0

    alpha = [0.0 for _ in range(0, n - 1)]
    beta = [0.0 for _ in range(0, n - 1)]

    for i in range(1, n - 1):
        hi = values[i].x - values[i - 1].x
        hi1 = values[i + 1].x - values[i].x
        delta = (values[i].y - values[i - 1].y) / hi
        delta1 = (values[i + 1].y - values[i].y) / hi1
        a = hi
        c = 2.0 * (hi + hi1)
        b = hi1
        f = 6.0 * (delta1 - delta)
        z = (a * alpha[i - 1] + c)
        alpha[i] = -b / z
        beta[i] = (f - a * beta[i - 1]) / z

    for i in range(n - 3, 0, -1):
        splines[i].c = alpha[i] * splines[i + 1].c + beta[i]

    for i in range(n - 2, 0, -1):
        hi = values[i].x - values[i - 1].x
        splines[i].d = (splines[i].c - splines[i - 1].c) / hi
        splines[i].b = hi * (2.0 * splines[i].c + splines[i - 1].c) / 6.0 + (values[i].y - values[i - 1].y) / hi

    return splines


def spline_interpolate(values, n, x):
    splines = build_spline(values, n)

    if not splines:
        return None

    n = len(splines)
    s = SplineTuple(0, 0, 0, 0, 0)

    if x <= splines[0].x:
        s = splines[0]
    elif x >= splines[n - 1].x:
        s = splines[n - 1]
    else:
        i = 0
        j = n - 1
        while i + 1 < j:
            k = i + (j - i) // 2
            if x <= splines[k].x:
                j = k
            else:
                i = k
        s = splines[j]

    dx = x - s.x

    return s.a + (s.b + (s.c / 2.0 + s.d * dx / 6.0) * dx) * dx


def splines_mult_int(data, xp, yp, zp):
    matrix = data[matrix_index]
    x_arr = data[x_index]
    y_arr = data[y_index]
    z_arr = data[z_index]

    z_values = []
    for k in range(len(z_arr)):
        y_values = []

        for i in range(len(y_arr)):
            x_values = []

            for j in range(len(x_arr)):
                x_values.append(Point(x_arr[j], matrix[k][i][j]))

            # print("Значение для нахождение полином Ньютона nx: (x_values)")
            # for el in x_values:
            #     print(el.getX(), el.getY())
            # print("end\n")

            y_values.append(Point(y_arr[i], spline_interpolate(x_values, len(x_values), xp)))

        # print("Значение для нахождение полином Ньютона ny: (y_values)")
        # for el in y_values:
        #     print(el.getX(), el.getY())
        # print("end\n")

        z_values.append(Point(z_arr[k], spline_interpolate(y_values, len(y_values), yp)))

    return spline_interpolate(z_values, len(z_values), zp)
