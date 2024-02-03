def check_int(n):
    try:
        n = int(n)
    except:
        return False
    return True 

def check_float(n):
    try:
        n = float(n)
    except:
        return False 
    return True 

def sort_table(arr_y, arr_x, arr_yy):
    for i in range(len(arr_y)):
        for j in range(len(arr_y) - i - 1):
            if (arr_y[j] > arr_y[j + 1]):
                arr_y[j], arr_y[j + 1] = arr_y[j + 1], arr_y[j]
                arr_x[j], arr_x[j + 1] = arr_x[j + 1], arr_x[j]
                if (arr_yy != None):
                    arr_yy[j], arr_yy[j + 1] = arr_yy[j + 1], arr_yy[j]

#Взять данные (табличная функция, степень, аргумент) из файл, пользователь
def get_data(filename): 
    arr_x = []
    arr_y = []
    arr_yy = []

    try:
        with open(filename, 'r') as file:
            while True:
                line = [float(x) for x in file.readline().split()]
                if (len(line) % 3 != 0):
                    print("Данные в файле не правильные.")
                    return  
                if (len(line) == 0):
                    break
                arr_x.append(line[0])
                arr_y.append(line[1])
                arr_yy.append(line[2])
    except:
        print("Ошибка открытия файла!")
        return

    sort_table(arr_x, arr_y, arr_yy)
    #Ввод от пользователя
    #Входная степень n
    n = input("Ввести степень n аппроксимирующих Ньютона и Эрмита: ")

    if (check_int(n) == False or int(n) < 0 or int(n) > len(arr_x)):
        print("Ошибка!!!") 
        return
    
    #Входное значение x для расчета
    x = input("Значение аргумента x: ")

    if (check_float(x) == False or float(x) > max(arr_x)):
        print("Ошибка!!!") 
        return 
    
    return arr_x, arr_y, arr_yy, n, x 

#Взять данные для решение систему нелинейных уравнений
def get_data_from_file(filename):
    table = [[], []]
    try:
        with open(filename, "r") as f:
            while True:
                temp = [float(x) for x in f.readline().split()]
                if len(temp) == 0:
                    break
                table[0].append(temp[0])
                table[1].append(temp[1])
    except:
        print("Ошибка!")
        return
    sort_table(table[0], table[1], None)
    return table
