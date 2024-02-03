from newton import newton, Point, z_index, y_index, x_index, matrix_index
from splines import spline_interpolate


def spline_newton_mult_int(data, nx, ny, nz, xp, yp, zp):
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

            y_values.append(Point(y_arr[i], newton(x_values, nx, xp)))

        # print("Значение для нахождение полином Ньютона ny: (y_values)")
        # for el in y_values:
        #     print(el.getX(), el.getY())
        # print("end\n")

        z_values.append(Point(z_arr[k], spline_interpolate(y_values, len(y_values), yp)))

    # print("Значение для нахождение полином Ньютона nz: (z_values)")
    # for el in z_values:
    #     print(el.getX(), el.getY())
    # print("end\n")

    return newton(z_values, nz, zp)
