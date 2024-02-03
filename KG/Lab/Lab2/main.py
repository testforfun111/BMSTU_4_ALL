from asyncio import events
import tkinter as tk
import tkinter.messagebox as box
import copy
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import model
import update

matplotlib.use('TkAgg')


AUTHOR_TITLE = 'Об авторе'
AUTHOR = 'Ву Хай Данг\nИУ7-42Б'
WIDTH=1530
HEIGHT=780
PLOT_WIDTH=200
PLOT_HEIGHT=200
ST=0
END=0
MARGINS = {
            "left"   : 0.050,
            "bottom" : 0.050,
            "right"  : 0.980,
            "top"    : 0.980
        }

class RootWindow():
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("%dx%d+%d+%d"%(WIDTH, HEIGHT, ST, END))
        self.root.title("ЛР2")
        cnv_solution = tk.Canvas(self.root)
        cnv_solution.place(relx=0.989, y=0, relheight=1.0, relwidth=0.713)
        self.figure = plt.Figure(figsize=(8.5, 7.5))
        self.canvas = FigureCanvasTkAgg(self.figure, self.root)
        self.plot = self.canvas.get_tk_widget()
        self.plot.place(relx=0.01, rely=0.02, relheight=0.96, relwidth=0.70)

    def create_menu(self):
        self.menu = tk.Menu(self.root, font="TkMenuFont")

        self.menu.add_command(label=AUTHOR_TITLE, command=lambda: box.showinfo(AUTHOR_TITLE, AUTHOR))
        self.menu.add_command(label='Выход', command=self.root.destroy)

        self.root.configure(menu=self.menu)


    def display_center_model(self):
        self.lblfrm_model_centre = tk.LabelFrame(self.root)
        self.lblfrm_model_centre.place(relx=0.73, rely=0.013, relheight=0.109, relwidth=0.25)

        self.lbl_model_centre = tk.Label(self.lblfrm_model_centre)
        self.lbl_model_centre.place(relx=0.007, rely=0.330, relheight=0.5, relwidth=0.98, bordermode='inside')
        self.lbl_model_centre.configure(font=update.FONT_CONFIG,
            text="Центр фигуры (x, y): ({:.2f}, {:.2f})".format(self.funcs[-1].x_list[0], self.funcs[-1].y_list[0]))

    def crtwdg_transfer(self):
        self.lblfrm_transfer = tk.LabelFrame(self.root)
        self.lblfrm_transfer.place(relx=0.73, rely=0.133, relheight=0.157, relwidth=0.25)

        self.lbl_transfer = tk.Label(self.lblfrm_transfer)
        self.lbl_transfer.place(relx=0.2, rely=0.01, relheight=0.25, relwidth=0.5, bordermode='inside')
        self.lbl_transfer.configure(font=('DejaVu Sans', 17), text="Перемещение", fg="blue")
        
        self.lbl_dx = tk.Label(self.lblfrm_transfer)
        self.lbl_dx.place(relx=0.007, rely=0.29, relheight=0.2, relwidth=0.15, bordermode='inside')
        self.lbl_dx.configure(font=('DejaVu Sans', 12), text="dx:")

        self.lbl_dy = tk.Label(self.lblfrm_transfer)
        self.lbl_dy.place(relx=0.007, rely=0.637, relheight=0.2, relwidth=0.15,bordermode='inside')
        self.lbl_dy.configure(font=('DejaVu Sans', 12), text="dy:")

        self.ent_dx = tk.Entry(self.lblfrm_transfer)
        self.ent_dx.place(relx=0.164, rely=0.29, relheight=0.25, relwidth=0.4, bordermode='inside')
        self.ent_dx.configure(background="white", font="TkFixedFont", selectbackground="blue", selectforeground="white")

        self.ent_dy = tk.Entry(self.lblfrm_transfer)
        self.ent_dy.place(relx=0.171, rely=0.645, relheight=0.25, relwidth=0.4, bordermode='inside')
        self.ent_dy.configure(background="white", font="TkFixedFont", selectbackground="blue", selectforeground="white")

        self.btn_transfer = tk.Button(self.lblfrm_transfer, background='#99ccff')
        self.btn_transfer.place(relx=0.6, rely=0.28, relheight=0.6, relwidth=0.37, bordermode='inside')
        self.btn_transfer.configure(activebackground="#f9f9f9", text="Перенести", font=17, command=lambda: update.move(self, MODEL, MODELS))


    def crtwdg_trans_centre(self):
        self.lblfrm_centre = tk.LabelFrame(self.root)
        self.lblfrm_centre.place(relx=0.73, rely=0.308, relheight=0.147, relwidth=0.25)

        self.lbl_trans_center = tk.Label(self.lblfrm_centre)
        self.lbl_trans_center.place(relx=0.02, rely=0.009, relheight=0.25, relwidth=0.9, bordermode='inside')
        self.lbl_trans_center.configure(font=('DejaVu Sans', 17), text="Центр преобразований", fg='blue')

        self.lbl_xc = tk.Label(self.lblfrm_centre)
        self.lbl_xc.place(relx=0.02, rely=0.259, relheight=0.3, relwidth=0.15, bordermode='inside')
        self.lbl_xc.configure(font=('DejaVu Sans', 12), text="Xc:")

        self.lbl_yc = tk.Label(self.lblfrm_centre)
        self.lbl_yc.place(relx=0.02, rely=0.612, relheight=0.3, relwidth=0.15, bordermode='inside')
        self.lbl_yc.configure(activebackground="#f9f9f9", font=('DejaVu Sans', 12), text="Yc:")

        self.ent_xc = tk.Entry(self.lblfrm_centre)
        self.ent_xc.place(relx=0.178, rely=0.3, relheight=0.25, relwidth=0.4, bordermode='inside')
        self.ent_xc.configure(background="white", font="TkFixedFont")
        self.ent_xc.insert(0, "100.00")

        self.ent_yc = tk.Entry(self.lblfrm_centre)
        self.ent_yc.place(relx=0.178, rely=0.638, relheight=0.25, relwidth=0.4, bordermode='inside')
        self.ent_yc.configure(background="white", font="TkFixedFont", selectbackground="blue", selectforeground="white")
        self.ent_yc.insert(0, "100.00")

    def crtwdg_scaling(self):
        self.lblfrm_scaling = tk.LabelFrame(self.root)
        self.lblfrm_scaling.place(relx=0.73, rely=0.472, relheight=0.157, relwidth=0.25)

        self.lbl_scale = tk.Label(self.lblfrm_scaling)
        self.lbl_scale.place(relx=0.2, rely=0.009, relheight=0.25, relwidth=0.6, bordermode='inside')
        self.lbl_scale.configure(font=('DejaVu Sans', 17), text="Масштабирование", fg='blue')

        self.lbl_kx = tk.Label(self.lblfrm_scaling)
        self.lbl_kx.place(relx=0.007, rely=0.29, relheight=0.25, width=53, bordermode='inside')
        self.lbl_kx.configure(font=('DejaVu Sans', 12), text="Kx:")

        self.lbl_ky = tk.Label(self.lblfrm_scaling)
        self.lbl_ky.place(relx=0.007, rely=0.59, relheight=0.25, width=53, bordermode='inside')
        self.lbl_ky.configure(font=('DejaVu Sans', 12), text="Ky:")

        self.ent_kx = tk.Entry(self.lblfrm_scaling)
        self.ent_kx.place(relx=0.164, rely=0.27, relheight=0.25, relwidth=0.4, bordermode='inside')
        self.ent_kx.configure(background="white", font="TkFixedFont", selectbackground="blue", selectforeground="white")

        self.ent_ky = tk.Entry(self.lblfrm_scaling)
        self.ent_ky.place(relx=0.164, rely=0.57, relheight=0.25, relwidth=0.4, bordermode='inside')
        self.ent_ky.configure(background="white", font="TkFixedFont", selectbackground="blue", selectforeground="white")

        self.btn_scaling = tk.Button(self.lblfrm_scaling, background='#99ccff')
        self.btn_scaling.place(relx=0.6, rely=0.23, relheight=0.6, relwidth=0.37, bordermode='inside')
        self.btn_scaling.configure(text="Масштабировать", command=lambda: update.scale(self, MODEL, MODELS))


    def crtwdg_rotate(self):
        self.lblfrm_rotate = tk.LabelFrame(self.root)
        self.lblfrm_rotate.place(relx=0.73, rely=0.649, relheight=0.157, relwidth=0.25)

        self.lbl_rotate = tk.Label(self.lblfrm_rotate)
        self.lbl_rotate.place(relx=0.2, rely=0.009, relheight=0.25, relwidth=0.6, bordermode='inside')
        self.lbl_rotate.configure(font=('DejaVu Sans', 17), justify=tk.CENTER, text="Поворот", fg='blue')

        self.lbl_angle = tk.Label(self.lblfrm_rotate)
        self.lbl_angle.place(relx=0.025, rely=0.42, bordermode='inside')
        self.lbl_angle.configure(activebackground="#f9f9f9", font=('DejaVu Sans', 12), justify=tk.CENTER, text="Угол (°):")

        self.ent_angle = tk.Entry(self.lblfrm_rotate)
        self.ent_angle.place(relx=0.28, rely=0.42, relheight=0.25, relwidth=0.3, bordermode='inside')
        self.ent_angle.configure(background="white", font="TkFixedFont", selectbackground="blue", selectforeground="white")

        self.btn_rotate = tk.Button(self.lblfrm_rotate, background='#99ccff')
        self.btn_rotate.place(relx=0.6, rely=0.23, relheight=0.6, relwidth=0.37, bordermode='inside')
        self.btn_rotate.configure(activebackground="#f9f9f9", text="Повернуть", command=lambda: update.rotate(self, MODEL, MODELS))


    def crtwdg_edit(self):
        self.btn_undo = tk.Button(self.root, background='#99ccff')
        self.btn_undo.place(relx=0.73, rely=0.819, relheight=0.075, relwidth=0.251)
        self.btn_undo.configure(text="← Назад", font=17, state=tk.DISABLED, command=lambda: update.undo(ROOT, MODEL, MODELS))

        self.btn_original = tk.Button(self.root, background='#99ccff')
        self.btn_original.place(relx=0.73, rely=0.905, relheight=0.075,relwidth=0.251)
        self.btn_original.configure(text="Исходное изображение", font=17, command=lambda: update.reset(ROOT, MODEL, MODELS))
    
    def delete_model(self):
        self.figure.clear()

        self.figure.subplots_adjust(**MARGINS)
        self.subplt = self.figure.add_subplot(111)

        self.subplt.set_xlim((0, PLOT_WIDTH))
        self.subplt.set_ylim((0, PLOT_HEIGHT))
        self.subplt.grid(True)

    def draw_model(self):
        self.delete_model()
        for func in self.funcs:
            self.subplt.plot(func.x_list, func.y_list, color='k', linewidth=2)

        self.canvas.draw()

    def create_widgets(self):
        """
            Создание виджетов окна
        """
        self.create_menu()
        self.draw_model()
        self.display_center_model()
        self.crtwdg_transfer()
        self.crtwdg_trans_centre()
        self.crtwdg_scaling()
        self.crtwdg_rotate()
        self.crtwdg_edit()


    def run(self):
        self.create_widgets()
        self.root.mainloop()


if __name__ == "__main__":
    ROOT = RootWindow()
    MODEL = model.MODEL()
    ROOT.funcs = MODEL.full
    MODELS = update.History(0, [copy.deepcopy(MODEL)])
    ROOT.run()
