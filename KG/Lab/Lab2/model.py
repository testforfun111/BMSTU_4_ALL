"""
    Модуль для работы с изображением
"""

from math import sin, cos
import numpy as np

class Func:
    """
        Класс функции, заданной узлами
    """
    def __init__(self, x_list, y_list):
        self.x_list = x_list
        self.y_list = y_list


class MODEL:
    """
        Класс изображения
    """
    def __init__(self):
        """
            Конструктор класса
        """
        self.body1 = self.create_oval(100, 100, 2.5, 3)
        self.body2 = self.create_oval(112, 100, 2.5, 3)
        self.body3 = self.create_oval(88, 100, 2.5, 3)
        self.body4 = self.create_oval(100, 110, 2.5, 3)
        self.body5 = self.create_oval(100, 90, 2.5, 3)
        self.body6 = self.create_oval(100, 100, 9.5, 7)
        self.body7 = self.create_oval(100, 100, 14.5, 13)

        self.body8 = self.create_line(89.998, 98.232, 86.032, 101.85)
        self.body9 = self.create_line(86.032, 98.132, 89.998, 101.85)
        self.body10 = self.create_line(113.968, 101.85, 110.032, 98.232)
        self.body11 = self.create_line(110.032, 101.85, 113.968, 98.232)
        self.body12 = self.create_line(101.968, 91.768, 98.032, 88.232)
        self.body13 = self.create_line(101.968, 88.232, 98.032, 91.768)
        self.body14 = self.create_line(101.968, 111.768, 98.032, 108.232)
        self.body15 = self.create_line(101.968, 108.232, 98.032, 111.768)

        self.body22 = self.create_line(101.968, 102.121, 106.7, 105)
        self.body23 = self.create_line(98.232, 102.121, 93.3, 105)
        self.body24 = self.create_line(98.232, 97.879, 93.3, 95)
        self.body25 = self.create_line(101.768, 97.879, 106.7, 95)

        self.body16 = self.create_line(100, 100, 90.5, 70)
        self.body17 = self.create_line(100, 100, 85.5, 70)
        self.body18 = self.create_line(90.5, 70, 85.5, 70)
        self.body19 = self.create_line(100, 100, 109.5, 70)
        self.body20 = self.create_line(100, 100, 114.5, 70)
        self.body21 = self.create_line(109.5, 70, 114.5, 70)

        self.full = [self.body1,self.body2,self.body3,self.body4,self.body5,
                    self.body6,self.body7,self.body8,self.body9,self.body10,
                    self.body11, self.body12, self.body13, self.body14, self.body15,
                    self.body16, self.body17, self.body18, self.body19, self.body20,
                    self.body21, self.body22, self.body23, self.body24, self.body25]
        self.centre = Func([100], [100])
        self.full.append(self.centre)


    def reset(self):
        self.__init__()


    def create_oval(self, x, y, a, b): #(x, y) -center; (a, b) radius 
        body = Func([], [])
        angles = np.linspace(0, 360, 360)

        for angle in angles:
            body.x_list.append(x + a * cos(np.radians(angle)))
            body.y_list.append(y + b * sin(np.radians(angle)))

        return body

    def create_line(self, x1, y1, x2, y2):
        return Func([x1, x2], [y1, y2])

    def move(self, dx, dy):
        for element in self.full:
            element.x_list = [x + dx for x in element.x_list]
            element.y_list = [y + dy for y in element.y_list]


    def scaling(self, kx, ky, xc, yc):
        for element in self.full:
            element.x_list = [x * kx + (1 - kx) * xc for x in element.x_list]
            element.y_list = [y * ky + (1 - ky) * yc for y in element.y_list]


    def rotate(self, phi, xc, yc):
        for element in self.full:
            tmp_x = [x for x in element.x_list]
            element.x_list = [xc + (x - xc) * cos(np.radians(phi))
                              + (element.y_list[i] - yc) * sin(np.radians(phi))
                              for i, x in enumerate(element.x_list)]
            element.y_list = [yc - (tmp_x[i] - xc) * sin(np.radians(phi))
                              + (y - yc) * cos(np.radians(phi))
                              for i, y in enumerate(element.y_list)]
