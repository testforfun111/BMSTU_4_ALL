#определить начально и конец (некоторые узлы вблизи заданной точки val)
def find_xo_xn(arr_x, arr_y, degree, val): 
    index = 0
    while (val > arr_x[index]):
        if (index == len(arr_x) - 1): break
        index += 1

    index_0 = index - degree // 2
    index_n = index + degree // 2 + (degree % 2) - 1

    if index_n > len(arr_y) - 1:
        index_n = len(arr_y) - 1
        index_0 = len(arr_y) - degree
    elif index_0 < 0:
        index_0 = 0
        index_n = degree - 1
    
    return index_0, index_n

def get_diff_table(arr_x, arr_y):
    n = len(arr_x)
    diff_table = []
    diff_table.append(arr_y)
    for i in range(n - 1):
        temp = []
        for j in range(len(diff_table[i]) - 1):
            temp.append((diff_table[i][j] - diff_table[i][j + 1]) / (arr_x[j] - arr_x[j + i + 1]))
        diff_table.append(temp)

    return diff_table

def polynom_newton(arr_x, arr_y, degree, val):
    index_0, index_n = find_xo_xn(arr_x, arr_y, degree + 1, val)
    new_arr_x = arr_x[index_0:index_n+1:1]
    new_arr_y = arr_y[index_0:index_n+1:1]

    result = 0
    coefficient = 1
    diff_table = get_diff_table(new_arr_x, new_arr_y)

    for i in range(len(diff_table)):
        result += diff_table[i][0] * coefficient
        coefficient *= val - new_arr_x[i]

    return result

def scd_dir_polynom_newton(arr_x, arr_y, degree, val):
    index_0, index_n = find_xo_xn(arr_x, arr_y, degree + 1, val)
    new_arr_x = arr_x[index_0:index_n+1:1]
    new_arr_y = arr_y[index_0:index_n+1:1]

    diff_table = get_diff_table(new_arr_x, new_arr_y)

    result = 2 * diff_table[2][0] + (6 * val - 2 * (new_arr_x[1] + new_arr_x[2]) - 2 * new_arr_x[0]) * diff_table[3][0]

    return result

def change_table_for_hermite(arr_x, arr_y, degree):
    arr_hermite_x = []
    arr_hermite_y = []

    for i in range(len(arr_x)):
        arr_hermite_x.append(arr_x[i])
        arr_hermite_x.append(arr_x[i])
        arr_hermite_y.append(arr_y[i])
        arr_hermite_y.append(arr_y[i])
    if (degree % 2 == 0):
        arr_hermite_x.pop()
        arr_hermite_y.pop()

    return arr_hermite_x, arr_hermite_y

def get_diff_table_for_hermite(arr_x, arr_y, der_arr):
    count = 0
    n = len(arr_x)
    diff_table = []
    diff_table.append(arr_y)
    for i in range(n - 1):
        temp = []
        for j in range(len(diff_table[i]) - 1):
            if (arr_x[j] - arr_x[j + i + 1] != 0):
                temp.append((diff_table[i][j] - diff_table[i][j + 1]) / (arr_x[j] - arr_x[j + i + 1]))
            else :
                temp.append(der_arr[count])
                count += 1
        diff_table.append(temp)

    return diff_table

def polynom_hermite(arr_x, arr_y, arr_yy, degree, val):

    index_0, index_n = find_xo_xn(arr_x, arr_y, degree // 2 + 1, val)
    new_arr_x = arr_x[index_0:index_n+1:1]
    new_arr_y = arr_y[index_0:index_n+1:1]
    new_arr_yy = arr_yy[index_0:index_n+1:1]

    arr_hermite_x, arr_hermite_y = change_table_for_hermite(new_arr_x, new_arr_y, degree)

    result = 0
    coefficient = 1
    diff_table = get_diff_table_for_hermite(arr_hermite_x, arr_hermite_y, new_arr_yy)

    for i in range(len(diff_table)):
        result += diff_table[i][0] * coefficient
        coefficient *= val - arr_hermite_x[i]
    return result


def create_table_for_cmp(arr_x, arr_y, arr_yy):
    list_degree = [1, 2, 3, 4, 5]
    val = 0.675 

    print("For value x = 0.675")
    print("| Degree |  Newton  |  Hermite |")
    for x in list_degree:
        newton = polynom_newton(arr_x, arr_y, x, val)
        hermite = polynom_hermite(arr_x, arr_y, arr_yy, x, val)
        print("|    {:d}   | {:.6f} | {:.6f} |".format(x, newton, hermite))