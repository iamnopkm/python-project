from tkinter import Label as tkLabel
from tkinter.font import Font

class Label(tkLabel):
    def __init__(self, master ,text: str = "", 
                 foreground: str = "black", background: str = "white", image= None):
        if image:
            super().__init__(master, image = image, background = background)
        else:
            super().__init__(master, text = text, background = background, foreground = foreground)