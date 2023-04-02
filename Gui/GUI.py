import tkinter as tk
from tkinter.font import Font as tkFont
import os
from .Screen import Screen
from .Navbar import Navbar
from .Label import Label

class GUI(tk.Tk):
    def __init__(self, title, geometry = "800x600", 
                 resizable = (True, True), fullscreen = False, min_size = (0,0), 
                 icon = None, fonts = {}, on_close = None):
        super().__init__()
        self.title(title)

        if fullscreen:
            self.state("zoomed")
            self.resizable(True, True)
        else:
            self.geometry(geometry)
            self.resizable(resizable[0], resizable[1])
            self.minsize(min_size[0], min_size[0])

        if os.path.isfile(icon):
            self.iconphoto(True, tk.PhotoImage(file=icon))
        
        if on_close != None:
             self.protocol("WM_DELETE_WINDOW", lambda: self.on_exit(on_close))

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1, minsize=150)
        self.grid_columnconfigure(1, weight=20)
        self.screens: dict[str, Screen] = {}
        self.current_screen: str = None
    def on_exit(self, func):
        func()
        self.destroy()

    def init_navbar(self, navbar: Navbar):   
        self.navbar = navbar
        self.navbar.grid(row=0,column=0, sticky=tk.NSEW)

    def add_screen(self, screen_name: str, screen: Screen):
        self.screens[screen_name] = screen

    def change_screen(self, screen_name: str):
        self.hide_screen(self.current_screen)
        self.show_screen(screen_name)

    def hide_screen(self, screen_name: str):
        self.screens[screen_name].grid_forget()
    
    def show_screen(self, screen_name: str):
        self.screens[screen_name].grid(row=0, column=1, sticky=tk.NSEW)
        self.current_screen = screen_name