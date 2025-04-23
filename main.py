import tkinter as tk
from model import Torneio
from view import StartupRushView
from controller import StartupRushController

if __name__ == "__main__":
    root = tk.Tk()
    model = Torneio()
    view = StartupRushView(root)
    controller = StartupRushController(model, view)
    root.mainloop()