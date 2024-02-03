from IO import * 
from interpolation import *

def solution(filename1, filename2):
    table1 = get_data_from_file(filename1)
    table2 = get_data_from_file(filename2)
    if table1 == None or table2 == None:
        return 

    new_table = []
    new_table.append(table2[0])
    new_table.append([])
    for i in range(len(table2[0])):
        new_x = polynom_newton(table1[1], table1[0], 5, table2[0][i])
        # print(table2[0][i],'    ', new_x)
        new_table[1].append(table2[1][i] - new_x)

    sort_table(new_table[1], new_table[0], None)

    result = polynom_newton(new_table[1], new_table[0], 5, 0)
    return result