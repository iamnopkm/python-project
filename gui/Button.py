from tkinter import Button as tkButton

class Button(tkButton):
    def __init__(self, master, command, text, 
                 width: int = None, height: int = None, background: str = "white", 
                 foreground: str = "black", activebackground: str = "grey", activeforeground: str = "black", 
                 borderwidth: int = 0
                 ):

        super().__init__(master, activebackground = activebackground,  activeforeground = activeforeground, 
                         background = background, foreground = foreground, borderwidth = borderwidth, 
                         command = command, text = text, width = width, 
                         height = height, cursor = "hand2")