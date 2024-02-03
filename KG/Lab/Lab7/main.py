import interface
import tkinter as tk
from config import *

def create_main_frame(root):
    main_window = interface.MainWindowClass(root=root)
    root.geometry("%dx%d+50+0" %(WIDTH_WINDOW, HEIGHT_WINDOW))
    root.title('Отсечение (простой алгоритм)')
    # root.resizable(False, False)
    main_window.grid()

def main():
    master = tk.Tk()
    create_main_frame(master)
    master.mainloop()

if __name__ == '__main__':
    main()
