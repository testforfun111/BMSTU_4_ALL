"""
    Модуль для вывода сообщений
"""

import tkinter as tk
from PIL import ImageTk, Image
import tkinter.messagebox as box

NAME = 'Ву Хай Данг'
GROUP = 'ИУ7-42Б'
AUTHOR = NAME + '\n' + GROUP

levels = []

def create_infobox(title, text):
    box.showinfo(title, text)


def create_errorbox(title, text):
    box.showerror(title, text)

def create_hintbox(title, text):
    box.showinfo(title, text)

def author():
    create_infobox('Об авторе', AUTHOR)

def destroy_toplevels():
    for level in levels:
        level.destroy()
