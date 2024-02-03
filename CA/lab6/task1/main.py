from prettytable import PrettyTable
from integral_solution import *


def readFile(filename):
    data = []
    with open(filename, "r") as f:
        lines = f.readlines()
        data.append(list(map(float, lines[1].strip().split())))
        data.append(list(map(float, lines[3].strip().split())))
        data.append([list(map(float, lines[i].strip().split())) for i in range(5, 5 + len(data[1]))])

    return data

print("Главное меню:")
print("1 - Самостоятельно задать")
print("2 - Исследовать влияние количества выбираемых узлов на результаты расчетов.")
print("0 - Выход.")

data = readFile("data.txt")
t = True
while t:
    choice = int(input("Выберите действие: "))

    if choice == 1:
        n = int(input("Введите кол-во участков разбиения по Симпсону: "))
        if n % 2:
            print("количество участков должно быть четным.")
        else:
            m = int(input("Введите кол-во участков разбиения по Гауссу: "))
            nx = int(input("Введите кол-во узлов по Х (для интерполяции): "))
            ny = int(input("Введите кол-во узлов по Y (для интерполяции): "))

            result = Result(n, m, data, nx, ny)
            print(f"Значение интеграла: {result}")

    elif choice == 2:
        n = int(input("Введите кол-во участков разбиения по Симпсону: "))
        if n % 2:
            print("количество участков должно быть четным.")
        else:
            m = int(input("Введите кол-во участков разбиения по Гауссу: "))

            table = PrettyTable()
            table.add_column("Кол-во узлов по y\\x", [_ for _ in range(1, 6)])
            for i in range(1, 6):
                result = []
                for j in range(1, 6):
                    result.append(Result(n, m, data, i, j))
                table.add_column(f"{i}", result)

            print(table)

    elif choice == 0:
        t = False
