def read_data_from_file(arr_x, arr_y):
    with open("data.txt", "r") as f:
        while True:
            temp = [float(x) for x in f.readline().split()]
            if (temp == []):
                break
            arr_x.append(temp[0])
            arr_y.append(temp[1])

def find_index(arr_x, x_value):
    index = 0
    for i in range(len(arr_x)):
        if (arr_x[i] > x_value):
            index = i
            break
    return index

def interpolation_spline(arr_x, arr_y, x_value, start, end):
    arr_a = []
    for i in range(len(arr_y) - 1):
        arr_a.append(arr_y[i])

    arr_b = []
    arr_c = [0 for i in range(len(arr_x) - 1)]
    arr_c[0] = start 
    arr_c[1] = end
    arr_d = []
    arr_h = [0 for i in range(len(arr_x))]
    arr_e = [start, end]
    arr_n = [start, end]

    for i in range(1, len(arr_x)):
        arr_h[i] = arr_x[i] - arr_x[i - 1]

    for i in range(2, len(arr_x)):
        fi = 3 * ((arr_y[i] - arr_y[i - 1]) / arr_h[i] - (arr_y[i - 1] - arr_y[i - 2]) / arr_h[i - 1])
        arr_e.append(-1 * arr_h[i] / (arr_h[i - 1] * arr_e[i - 1] + 2 * (arr_h[i - 1] + arr_h[i])))
        arr_n.append((fi - arr_h[i - 1] * arr_n[i - 1]) / (arr_h[i - 1] * arr_e[i - 1] + 2 * (arr_h[i - 1] + arr_h[i])))
    
    arr_c[-1] = arr_n[-1]

    for i in range(len(arr_x) - 2, 0, -1):
        arr_c[i - 1] = arr_e[i] * arr_c[i] + arr_n[i]
    
    for i in range(1, len(arr_x) - 1):
        arr_d.append((arr_c[i] - arr_c[i - 1]) / (3 * arr_h[i]))
        arr_b.append((arr_y[i] - arr_y[i - 1]) / arr_h[i] - arr_h[i] * (arr_c[i] - 2 * arr_c[i - 1]) / 3)

    hi = arr_x[-1] - arr_x[-2]
    arr_b.append((arr_y[-1] - arr_y[-2]) / hi - hi * (arr_c[-1]) / 3)
    arr_d.append((-1 * arr_c[-1]) / (3 * hi))
    
    #y = a + b(x - xi) + c(x - xi) ** 2 + d (x - xi)**3 

    x_index = find_index(arr_x, x_value) - 1
    delta_x = (x_value - arr_x[x_index - 1])
    delta_x2 = delta_x * delta_x 
    delta_x3 = delta_x * delta_x * delta_x 
    y = arr_a[x_index] + arr_b[x_index] * delta_x + arr_c[x_index] * delta_x2 + arr_d[x_index] * delta_x3 
    return y 

