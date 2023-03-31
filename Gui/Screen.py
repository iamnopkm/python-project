import tkinter as tk
from .Navbar import Navbar
from .Frame import Frame

class Screen(Frame):
    def __init__(self, master, background = "#ffffff"):
        super().__init__(master, width = 400, height = 400, background = background)
        self.grid_propagate(False)
        self.pack_propagate(False)
    