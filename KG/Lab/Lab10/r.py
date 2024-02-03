# from math import pi, sin, cos
# from constants import *

# def rotate_matrix(trans_matrix, matrix):
#     res_matrix = [[0 for i in range(4)] for j in range(4)]

#     for i in range(4):
#         for j in range(4):
#             for k in range(4):
#                 res_matrix[i][j] += trans_matrix[i][k] * matrix[k][j]

#     trans_matrix = res_matrix
#     return trans_matrix

# def scale(x, y, coeff_scale):
#     x *= coeff_scale
#     y *= coeff_scale
#     x += WIDTH // 2
#     y += HEIGHT // 2 # - y
#     return round(x), round(y)
    
# def convers(arg):
#     return arg * pi / 180

# def rotateX(x, y, z, angle, trans_matrix):
#     angle = convers(angle)
#     rotating_matrix = [[1, 0, 0, 0],
#                      [0, cos(angle), -sin(angle), 0],
#                      [0, sin(angle), cos(angle), 0],
#                      [0, 0, 0, 1]]
#     trans_matrix = rotate_matrix(trans_matrix, rotating_matrix)
#     y = y * trans_matrix[1][1] + z * trans_matrix[1][2]
#     return x, y

# def rotateY(x, y, z, angle, trans_matrix):
#     angle = convers(angle)
#     rotating_matrix = [[cos(angle), 0, sin(angle), 0],
#                      [0, 1, 0, 0],
#                      [-sin(angle), 0, cos(angle), 0],
#                      [0, 0, 0, 1]]
#     trans_matrix = rotate_matrix(trans_matrix, rotating_matrix)
#     x = trans_matrix[0][0] * x + trans_matrix[0][2] * z
#     return x, y

# def rotateZ(x, y, z, angle, trans_matrix):
#     angle = convers(angle)
#     buf = x
#     rotating_matrix = [[cos(angle), -sin(angle), 0, 0],
#                      [sin(angle), cos(angle), 0, 0],
#                      [0, 0, 1, 0],
#                      [0, 0, 0, 1]]
#     trans_matrix = rotate_matrix(trans_matrix, rotating_matrix)
#     x = trans_matrix[0][0] * x + trans_matrix[0][1] * y
#     y = trans_matrix[1][1] * y + trans_matrix[1][0] * buf
#     return x, y

# def transform(x, y, z, angles, coeff_scale, trans_matrix):
#     x, y = rotateX(x, y, z, angles[0], trans_matrix)
#     x, y = rotateY(x, y, z, angles[1], trans_matrix)
#     x, y = rotateZ(x, y, z, angles[2], trans_matrix)
#     return scale(x, y, coeff_scale)
