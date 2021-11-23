"""
Módulo principal
"""
import tkinter as tk
from view import View
from model import Model
from controller import Controller

class App(tk.Tk):
    """
    clase App
    por lo que entiendo hereda Tk
    inspirado en https://www.pythontutorial.net/tkinter/tkinter-mvc/
    """
    def __init__(self):
        super().__init__()

        # create a model
        model = Model()

        # create a view and place it on the root window
        view = View(self)

        # create a controller
        controller = Controller(model, view)

        # set the controller to view
        view.set_controller(controller)


if __name__ == '__main__':
    app = App()
    app.mainloop()
