from newton import newton_mult_int
from read_file import read_table, printTable
from splines import splines_mult_int
from newton_splines import spline_newton_mult_int


table = read_table("data.txt")
# printTable(table)

x = float(input("Введите аргумент x: "))
y = float(input("Введите аргумент y: "))
z = float(input("Введите аргумент z: "))

nx = int(input("Введите степень аппроксимиляции nx: "))
ny = int(input("Введите степень аппроксимиляции ny: "))
nz = int(input("Введите степень аппроксимиляции nz: "))

print("Newton result:")
print("u = f(x, y, z) = {:.9f}".format(newton_mult_int(table, nx + 1, ny + 1, nz + 1, x, y, z)))

# print("All result:")
# for i_nz in range(1, nz + 1):
#     print("nz =", i_nz)
#     print("+" + "-" * 10 + ("+" + "-" * 10) * nx + "+")
#     print("| {:^8s}".format("ny \\ nx"), end=" ")
#
#     for i in range(1, nx + 1):
#         print("| {:^8d}".format(i), end=" ")
#     print("|")
#
#     print("+" + "-" * 10 + ("+" + "-" * 10) * nx + "+")
#     for i_ny in range(1, ny + 1):
#         print("| {:^8d}".format(i_ny), end=" ")
#         for i_nx in range(1, nx + 1):
#             print("| {:^8.3f}".format(newton_mult_int(table, i_nx + 1, i_ny + 1, i_nz + 1, x, y, z)), end=" ")
#         print("|")
#     print("+" + "-" * 10 + ("+" + "-" * 10) * nx + "+")

print("Spline result:")
print("u = f(x, y, z) = {:.9f}".format(splines_mult_int(table, x, y, z)))

print("Spline + newton result:")
print("u = f(x, y, z) = {:.9f}".format(spline_newton_mult_int(table, nx + 1, ny + 1, nz + 1, x, y, z)))
