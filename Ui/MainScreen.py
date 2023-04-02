from Gui import Screen, Label, BasicColors
from tkinter import PhotoImage

class MainScreen(Screen):
    def __init__(self, master):
        """Init screen"""
        super().__init__(master, BasicColors.PEACH)

        self.logo_image = PhotoImage(file="./Image/mobile_store.png")
        self.image_label = Label(self, image=self.logo_image, background=BasicColors.PEACH)
        self.image_label.pack()
        self.app_name = Label(self, "mobile Phone Store Information Management System App", background=BasicColors.CREAM)
        self.app_name.pack()