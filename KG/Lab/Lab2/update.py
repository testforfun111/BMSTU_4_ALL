"""
    Модуль для обновления изображения
"""

import tkinter as tk
import copy

import messages as msg


NONNUMERIC = 'Нечисловые данные'
EMPTY = 'Пустой ввод'

NONNUM_MOVE = 'dx и dy должны быть представлены вещественными числами'
EMPTY_MOVE = 'Для выполнения переноса заполните поля dx и dy'

NONNUM_SCALE = 'Xc, Yc, Kx и Ky должны быть представлены вещественными числами'
EMPTY_SCALE = 'Для выполнения масштабирования заполните поля Xc, Yc, Kx и Ky'

NONNUM_ROTATION = 'Xc, Yc и угол должны быть представлены вещественными числами'
EMPTY_ROTATION = 'Для выполнения поворота заполните поля Xc, Yc и "Угол (°)"'

FONT = 'DejaVu Sans Mono'
FONT_SIZE = 14
FONT_CONFIG = (FONT, FONT_SIZE)


class History:
    """
        Класс истории состояний изображения
    """
    def __init__(self, index, buf):
        """
            Коструктор класса
        """
        self.index = index
        self.buf = buf


    def add(self, func):
        """
            Добавление состояния в историю
        """
        self.index += 1
        self.buf = self.buf[:self.index] + [func]

    def back(self, model):
        """
            Шаг назад
        """
        self.index -= 1
        self.update_model(model)

    def update_model(self, model):
        """
            Постановка текущего состояния
        """
        model_copy = copy.deepcopy(self.buf[self.index])

        for i, part in enumerate(model_copy.full):
            model.full[i] = part


def renew_label(window):
    """
        Обновление показанных координат
        центра фигуры
    """
    window.lbl_model_centre.configure(
        font=FONT_CONFIG,
        text="Центр фигуры (x, y): ({:.2f}, {:.2f})".format(window.funcs[-1].x_list[0],
                                           window.funcs[-1].y_list[0])
        )


def move(window, model, models):
    try:
        dx = float(window.ent_dx.get())
        dy = float(window.ent_dy.get())

    except ValueError:
        if window.ent_dx.get() and window.ent_dy.get():
            msg.create_errorbox(NONNUMERIC, NONNUM_MOVE)
        else:
            msg.create_errorbox(EMPTY, EMPTY_MOVE)

    else:
        model.move(dx, dy)
        models.add(copy.deepcopy(model))
        window.funcs = model.full
        window.btn_undo.configure(state=tk.NORMAL)
        window.draw_model()
        renew_label(window)


def scale(window, model, models):
    try:
        kx = float(window.ent_kx.get())
        ky = float(window.ent_ky.get())
        xc = float(window.ent_xc.get())
        yc = float(window.ent_yc.get())

    except ValueError:
        if (window.ent_kx.get() and window.ent_ky.get()
                and window.ent_xc.get() and window.ent_yc.get()):
            msg.create_errorbox(NONNUMERIC, NONNUM_SCALE)
        else:
            msg.create_errorbox(EMPTY, EMPTY_SCALE)

    else:
        model.scaling(kx, ky, xc, yc)
        models.add(copy.deepcopy(model))
        window.funcs = model.full
        window.btn_undo.configure(state=tk.NORMAL)
        window.draw_model()
        renew_label(window)


def rotate(window, model, models):
    try:
        phi = float(window.ent_angle.get())
        xc = float(window.ent_xc.get())
        yc = float(window.ent_yc.get())

    except ValueError:
        if (window.ent_xc.get() and window.ent_yc.get()
                and window.ent_angle.get()):
            msg.create_errorbox(NONNUMERIC, NONNUM_ROTATION)
        else:
            msg.create_errorbox(EMPTY, EMPTY_ROTATION)

    else:
        model.rotate(phi, xc, yc)
        models.add(copy.deepcopy(model))
        window.btn_undo.configure(state=tk.NORMAL)
        window.funcs = model.full
        window.draw_model()
        renew_label(window)


def reset(window, model, models):

    model.reset()
    window.funcs = model.full
    window.draw_model()
    models.add(copy.deepcopy(model))
    window.btn_undo.configure(state=tk.NORMAL)
    renew_label(window)


def undo(window, model, models):
    """
        Возвращение к предыдущему состоянию изображения
    """
    if models.index:
        models.back(model)
        window.funcs = model.full
        window.draw_model()
        renew_label(window)

    if not models.index:
        window.btn_undo.configure(state=tk.DISABLED)

def move_center(window, model, models):
    """
        Запуск переноса
    """
    try:
        dx = float(window.ent_xc.get())
        dy = float(window.ent_yc.get())

    except ValueError:
        if window.ent_xc.get() and window.ent_yc.get():
            msg.create_errorbox(NONNUMERIC, NONNUM_MOVE)
        else:
            msg.create_errorbox(EMPTY, EMPTY_MOVE)

    else:
        #model.move(dx, dy)
        models.add(copy.deepcopy(model))
        window.funcs = model.full
        window.btn_undo.configure(state=tk.NORMAL)
        window.draw_model()
        renew_label(window)