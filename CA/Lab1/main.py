from IO import * 
from interpolation import *
from solutionSys import *

def main():
    datas = get_data("data.txt")
    if (datas == None):
        return

    arr_x = datas[0]
    arr_y = datas[1]
    arr_yy = datas[2]
    degree = int(datas[3])
    val = float(datas[4])

    print("Newton: {:.6f}".format(polynom_newton(arr_x, arr_y, degree, val)))

    print("Hermite: {:.6f}".format(polynom_hermite(arr_x, arr_y, arr_yy, degree, val)))

    # # найти решение 
    arr_x_Hermite = [x for x in arr_x]
    arr_y_Hermite = [y for y in arr_y]
    arr_xx = [float(1 / x) for x in arr_yy]
    sort_table(arr_y, arr_x, arr_yy)
    print("Root (with Newton): {:.7f}".format(polynom_newton(arr_y, arr_x, degree, 0)))
    
    sort_table(arr_y_Hermite, arr_x_Hermite, arr_xx)

    print("Rooot (with Hermite): {:.7f}".format(polynom_hermite(arr_y_Hermite, arr_x_Hermite, arr_xx, degree, 0)))
    # #Таблица
    # create_table_for_cmp(arr_x, arr_y, arr_yy)

    # #Решение систему нелинейных уравнений
    # print("Решение систему нелинейных уравнений: ", solution("data1.txt", "data2.txt"))
if __name__ == "__main__":
    main()   

