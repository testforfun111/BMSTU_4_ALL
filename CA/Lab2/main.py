from spline import *
from interpolation import *

arr_x = []
arr_y = []
read_data_from_file(arr_x, arr_y)
x_value = float(input("Input x for find value y: "))

print("Newton: Value Y: ", polynom_newton(arr_x, arr_y, 3, x_value))

print("1.Value Y: ", interpolation_spline(arr_x, arr_y, x_value, 0, 0))
start2 = scd_dir_polynom_newton(arr_x, arr_y, 3, arr_x[0]) / 2
end2 = 0
print("2.Value Y: ", interpolation_spline(arr_x, arr_y, x_value, start2, end2))

start3 = scd_dir_polynom_newton(arr_x, arr_y, 3, arr_x[0]) / 2
end3 = scd_dir_polynom_newton(arr_x, arr_y, 3, arr_x[-1]) / 2
print("3.Value Y: ", interpolation_spline(arr_x, arr_y, x_value, start3, end3))