from tkinter import Button as tkButton

class Button(tkButton):
    def __init__(self, master, command, 
                 text, width = None, height = None, 
                 background: str = "white", foreground: str = "black", activebackground: str = "grey", 
                 activeforeground="black", borderwidth: int = 0, padx = 0, pady = 0):
        super().__init__(
            master, activebackground = activebackground, activeforeground = activeforeground, 
            background = background, foreground = foreground, borderwidth = borderwidth, 
            command = command, text = text, width = width, height = height, cursor = "hand2", padx = padx, pady = pady)