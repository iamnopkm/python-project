from tkinter import Frame as tkFrame
from .Widget import Widget

class Frame(tkFrame):
    def __init__(self, master, width: int = 400, height: int = 400, background: str = "white"):
        super().__init__(master, width = width, height = height, background = background)