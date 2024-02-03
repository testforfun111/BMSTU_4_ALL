from newton import z_index, y_index, x_index, matrix_index, infinity

EPS = 1e-6


def read_table(filename):
    data_table = [[], [], [], [[]]]
    file = open(filename)
    flagaddx = False
    flagaddy = False
    z = 0
    y = 0
    for line in file.readlines():
        row = line.split("\n")[0].split("\t")

        if "z=" in row[0]:
            z_str = row[0].split("z=")
            data_table[z_index].append(float(z_str[1]))
        elif "y\\x" in row[0]:
            if flagaddx:
                continue
            for i in range(1, len(row)):
                data_table[x_index].append(float(row[i]))
            flagaddx = True
        else:
            if "end" in row[0]:
                continue
            if not row[0].isdigit():
                z += 1
                data_table[matrix_index].append([])
                y = 0
                flagaddy = True
                continue

            if not flagaddy:
                data_table[y_index].append(float(row[0]))

            data_table[matrix_index][z].append([])
            for i in range(1, len(row)):
                data_table[matrix_index][z][y].append(float(row[i]))
            y += 1

    file.close()
    return data_table


# красивый вывод и точка
def printTable(data_table):

    for k in range(len(data_table[z_index])):
        print("z =", data_table[z_index][k])
        print(("+" + "-" * 10) * (len(data_table[x_index]) + 1) + "+")
        print("| {:^8s}".format("Y / X"), end=" ")
        for i in range(len(data_table[x_index])):
            print("| {:^8.2f}".format(data_table[x_index][i]), end=" ")
        print("|")
        print(("+" + "-" * 10) * (len(data_table[x_index]) + 1) + "+")
        for i in range(len(data_table[matrix_index][k])):
            print("| {:^8.3f}".format(data_table[y_index][i]), end=" ")
            for j in range(len(data_table[matrix_index][z_index][i])):
                if data_table[matrix_index][k][i][j] == infinity:
                    print("| {:^8s}".format("inf"), end=" ")
                else:
                    print("| {:^8.3f}".format(data_table[matrix_index][k][i][j]), end=" ")
            print("|")
        print(("+" + "-" * 10) * (len(data_table[x_index]) + 1) + "+")