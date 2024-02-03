from math import * 

EPS = 1e-9

def check_triangle(point_A, point_B, point_C):
    return fabs((point_A[1] - point_B[1]) * (point_A[0] - point_C[0]) - (point_A[1] - point_C[1]) * (point_A[0] - point_B[0])) >= EPS

def distance_two_point(point_A, point_B):
    return round(sqrt((point_A[0] - point_B[0]) ** 2 + (point_A[1] -  point_B[1]) ** 2), 3)

def linear_equation(point_A, point_B):
    return point_B[1] - point_A[1], point_A[0] - point_B[0],\
            (point_B[0] - point_A[0]) * point_A[1] - (point_B[1] - point_A[1]) * point_A[0]

def altitude_equation(point_A, direct_x, direct_y):
    return direct_y, direct_x * -1, -1 * direct_y * point_A[0] + direct_x * point_A[1]

def intersection_lines(a1, b1, c1, a2, b2, c2):
    if a1 * b2 - a2 * b1 == 0:
        return 
    
    x = round((c1 * b2 - c2 * b1) / (a1 * b2 - a2 * b1), 3)
    y = round((a1 * c2 - a2 * c1) / (a1 * b2 - a2 * b1), 3)

    return x, y

def find_altitudes_triangle(point_A, point_B, point_C):
    line_ab = linear_equation(point_A, point_B)
    line_bc = linear_equation(point_B, point_C)
    line_ac = linear_equation(point_A, point_C)

    line_ah = altitude_equation(point_A, line_bc[0], line_bc[1])
    line_bk = altitude_equation(point_B, line_ac[0], line_ac[1])
    line_cf = altitude_equation(point_C, line_ab[0], line_ab[1])

    point_H = intersection_lines(line_bc[0], line_bc[1], line_bc[2] * -1, line_ah[0], line_ah[1], line_ah[2] * -1)
    point_K = intersection_lines(line_ac[0], line_ac[1], line_ac[2] * -1, line_bk[0], line_bk[1], line_bk[2] * -1)
    point_F = intersection_lines(line_ab[0], line_ab[1], line_ab[2] * -1, line_cf[0], line_cf[1], line_cf[2] * -1)
    AH = distance_two_point(point_A, point_H)
    BK = distance_two_point(point_B, point_K)
    CF = distance_two_point(point_C, point_F)

    max_altitude = max(AH, BK, CF)
    list_max_altitudes = []
    if AH == max_altitude:
        list_max_altitudes.append(point_A)
        list_max_altitudes.append(point_H)  
    if BK == max_altitude:
        list_max_altitudes.append(point_B)
        list_max_altitudes.append(point_K)
    if CF == max_altitude:
        list_max_altitudes.append(point_C)
        list_max_altitudes.append(point_F)
    
    list_altitudes = []

    if point_A not in list_max_altitudes:
        list_altitudes.append(point_A)
        list_altitudes.append(point_H)  
    if point_B not in list_max_altitudes:
        list_altitudes.append(point_B)
        list_altitudes.append(point_K)
    if point_C not in list_max_altitudes:
        list_altitudes.append(point_C)
        list_altitudes.append(point_F)
    return list_max_altitudes, list_altitudes