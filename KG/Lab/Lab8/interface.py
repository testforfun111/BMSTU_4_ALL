import algorithm as alg
# import canvas as cv
import config as cfg
from config import FONT, FONT_BOLD, PADX, PADY
import tkinter as tk
import tkinter.colorchooser as cch
import tkinter.messagebox as mb
import math

class Canvas(tk.Canvas):
    def __init__(self, frame):
        self.frame = frame
        self.width = cfg.CANVAS_WIDTH
        self.height = cfg.CANVAS_HEIGHT

        self.start = cfg.Point(exist=False)
        self.old = cfg.Point(exist=False)
        self.section_1 = cfg.Point(exist=False)
        self.section_2 = cfg.Point(exist=False)
        self.frame.cutter = []
        self.color = 'black'

        super().__init__(self.frame, width=self.width, height=self.height, bg='white', highlightbackground='black')
        self.bind('<ButtonPress-1>', self.draw_section)
        self.bind('<ButtonPress-3>', self.draw_cutter)

    def draw_line(self, x1, y1, x2, y2, color, tag=None):
        self.create_line(x1, y1, x2, y2, fill=color, tag=tag)

    def draw_cutter(self, event):
        color = self.frame.colors['cutter']
        event_x, event_y = cfg.int_n(event.x), cfg.int_n(event.y)
        if not self.start:
            self.delete('cutter')
            self.delete('result')
            self.frame.cutter = []
            boxlist.delete(0, tk.END)
            self.draw_line(event_x, event_y, event_x + 1, event_y, self.color, 'cutter')
            self.start = cfg.Point(event_x, event_y, color)
            self.old = cfg.Point(event_x, event_y, color)
        else:
            try:
                if event.state in cfg.Ctrl:
                    if event_x == self.old.x:
                        m = 0
                    else:
                        m = abs(event_y - self.old.y) / abs(event_x - self.old.x)
                    if m < math.tan(math.pi / 4):
                        new_point = cfg.Point(event_x, self.old.y, color)
                    else:
                        new_point = cfg.Point(self.old.x, event_y, color)
                else:
                    raise AttributeError
            except AttributeError:
                new_point = cfg.Point(event_x, event_y, color)

            self.draw_line(self.old.x, self.old.y, new_point.x, new_point.y, color, 'cutter')
            self.frame.cutter.append([self.old, new_point])
            self.old = new_point
        boxlist.insert(tk.END, "%d. (%4d;%4d)" %(len(self.frame.cutter) + 1, event_x, event_y))

    def end_cutter(self):
        if self.start and self.old:
            color = self.frame.colors['cutter']
            self.frame.cutter.append((self.old, self.start))
            self.draw_line(self.old.x, self.old.y, self.start.x, self.start.y, color, 'cutter')
            self.start = cfg.Point(exist=False)
            self.old = cfg.Point(exist=False)

    def draw_section(self, event):
        event_x, event_y = cfg.int_n(event.x), cfg.int_n(event.y)
        color = self.frame.colors['section']
        if not self.section_1:
            self.section_1.set(event_x, event_y, color)
        else:
            if event.state not in cfg.Ctrl:
                self.section_2.set(event_x, event_y, color)

            elif event.state in cfg.Ctrl:
                if event_x == self.section_1.x:
                    m = 0
                else:
                    m = abs(event_y - self.section_1.y) / abs(event_x - self.section_1.x)
                if m < math.tan(math.pi / 4):
                    self.section_2.set(event_x, self.section_1.y, color)
                else:
                    self.section_2.set(self.section_1.x, event_y, color)
            elif event.state in cfg.Shift:
                pass 
            
            if (self.section_1 == self.section_2):
                mb.showwarning("Warning", "Отрезок вырожден!")
            else:
                self.draw_line(self.section_1.x, self.section_1.y, self.section_2.x, self.section_2.y, color)
                self.frame.section.append([self.section_1, self.section_2])
                self.section_1 = cfg.Point(exist=False)
                self.section_2 = cfg.Point(exist=False)

    def delete_all(self):
        self.delete('all')
        self.frame.section = []
        self.frame.cutter = []
        self.start.clear()
        self.old.clear()
        self.section_1.clear()
        self.section_2.clear()
        boxlist.delete(0, tk.END)
    

class MainWindowClass(tk.Frame):
    def __init__(self, root):
        super().__init__(root)

        self.canvas = Canvas(self)
        self.add_canvas()

        self.frame_cutter = tk.Frame(self)
        self.cutter_coors = None
        self.cutter = []
        self.add_cutter()

        self.frame_section = tk.Frame(self)
        self.section_coors = None
        self.section = []
        self.add_section()

        self.frame_color = tk.Frame(self)
        self.color_wins = dict()
        self.colors = {
            'cutter': 'black',
            'section': 'red',
            'result': 'green'
        }
        self.add_color()

        self.frame_buttons = tk.Frame(self)
        self.add_buttons()
    def add_canvas(self):
        self.canvas.grid(row=0, column=0, rowspan=4, padx=5, pady=5)

    def add_cutter(self):
        cfg.create_label(self.frame_cutter, 'ВВОД ОТСЕКАТЕЛЯ', FONT_BOLD, 0, 0, PADX, PADY, tk.N, 'flat')
        cfg.create_label(self.frame_cutter, 'Очередная вершина',
                         FONT_BOLD, 1, 0, PADX, 1, tk.N)
        self.cutter_coors = cfg.create_entry(self.frame_cutter, FONT, 2, 0, PADX, PADY, tk.N)
        cfg.create_button(self.frame_cutter, 'ДОБАВИТЬ', FONT, 3, 0, PADX, PADY, 1, 'WE', self.create_cutter)
        cfg.create_button(self.frame_cutter, 'ЗАМКНУТЬ', FONT, 4, 0, PADX, PADY, 1, 'WE', self.canvas.end_cutter)

        global boxlist
        boxlist = tk.Listbox(self.frame_cutter, bg = "white", width=50)
        boxlist.grid(row=5, column=0, sticky=tk.N)
        self.frame_cutter.grid(row=1, column=1, padx=5, pady=5, sticky=tk.N)

    def create_cutter(self):
        coors = self.cutter_coors.get().split()
        self.cutter_coors.delete(0, 'end')
        try:
            for i in range(0, len(coors) - 1, 2):
                x, y = float(coors[i]), float(coors[i + 1])
                self.canvas.draw_cutter(cfg.Point(x, y))

        except IndexError:
            mb.showerror('Ошибка', 'Должно быть введено больше двух координат, и их количество должно быть четным')
        except ValueError:
            mb.showerror('Ошибка', 'Каждая координата должна быть числом, введенным через пробел')

    def add_section(self):
        cfg.create_label(self.frame_section, 'ВВОД ОТРЕЗКОВ', FONT_BOLD, 0, 0, PADX, PADY, tk.N, 'flat')
        cfg.create_label(self.frame_section, 'Координаты отрезка',
                         FONT_BOLD, 1, 0, PADX, 1, tk.N)
        self.section_coors = cfg.create_entry(self.frame_section, FONT, 2, 0, PADX, PADY, tk.N)
        cfg.create_button(self.frame_section, 'ВВЕСТИ', FONT, 3, 0, PADX, PADY, 1, 'WE', self.create_section)
        self.frame_section.grid(row=2, column=1, padx=5, pady=5, sticky=tk.N)

    def create_section(self):
        coors = self.section_coors.get().split()
        self.section_coors.delete(0, 'end')
        try:
            x1, y1 = cfg.int_n(float(coors[0])), cfg.int_n(float(coors[1]))
            x2, y2 = cfg.int_n(float(coors[2])), cfg.int_n(float(coors[3]))
            if (x1 == x2 and y1 == y2):
                mb.showwarning("Warning", "Отрезок вырожден!")
            else:
                self.canvas.draw_line(x1, y1, x2, y2, self.colors['section'])
                self.section.append([cfg.Point(x1, y1, self.colors['section']), cfg.Point(x2, y2, self.colors['section'])])
        except IndexError:
            mb.showerror('Ошибка', 'Должно быть введено 4 координаты')
        except ValueError:
            mb.showerror('Ошибка', 'Каждая координата должна быть числом, введенным через пробел')

    def add_color(self):
        cfg.create_label(self.frame_color, 'ЦВЕТ ОТСЕКАТЕЛЯ: ', FONT_BOLD, 0, 0, PADX, 4, tk.N, 'flat')
        self.color_wins['cutter'] = cfg.create_button(self.frame_color, '', FONT, 1, 0, PADX, 0, 4, 'WE',
                                                      lambda: self.choose_color('cutter'), self.colors['cutter'])

        cfg.create_label(self.frame_color, 'ЦВЕТ ОТРЕЗКОВ: ', FONT_BOLD, 2, 0, PADX, 4, tk.N, 'flat')
        self.color_wins['section'] = cfg.create_button(self.frame_color, '', FONT, 3, 0, PADX, 0, 4, 'WE',
                                                       lambda: self.choose_color('section'), self.colors['section'])

        cfg.create_label(self.frame_color, 'ЦВЕТ РЕЗУЛЬТАТА: ', FONT_BOLD, 4, 0, PADX, 4, tk.N, 'flat')
        self.color_wins['result'] = cfg.create_button(self.frame_color, '', FONT, 5, 0, PADX, 0, 4, 'WE',
                                                      lambda: self.choose_color('result'), self.colors['result'])

        self.frame_color.grid(row=0, column=1, padx=5, pady=5, sticky=tk.N)

    def choose_color(self, color):
        self.colors[color] = cch.askcolor()[1]
        self.color_wins[color].config(**{'background': self.colors[color], 'activebackground': self.colors[color]})

    def add_buttons(self):
        cfg.create_button(self.frame_buttons, 'ОТСЕЧЬ', FONT, 0, 0, PADX, PADY, 1, 'WE', lambda:
                          alg.process(self.canvas, self.cutter, self.section))

        cfg.create_button(self.frame_buttons, 'ОЧИСТИТЬ', FONT, 1, 0, PADX, PADY, 1, 'WE', self.canvas.delete_all)

        self.frame_buttons.grid(row=3, column=1, padx=5, pady=5, sticky=tk.N)

