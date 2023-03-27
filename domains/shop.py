from tkinter import *
from tkinter.ttk import *
import mysql.connector

window = Tk()
window.title("Shop test program")
window.geometry("800x600")

greeting = Label(text="Hello, Tkinter", foreground="green", background="#e1ad01")
greeting.pack()

say = Label(text="Nerf")
say.pack()

style = Style()
style.configure("BW.TLabel", foreground="Black", background="White")

l1 = Label(text="Test1", style="BW.TLabel")
l2 = Label(text="Test2", style="BW.TLabel")

# sub window
# sub = tk.Toplevel(window)
# sub.title("Name")
# sub.geometry("600x400")

# widgets
Frame(window, width=100, height=100)
Label(window, text="This is label")


window.mainloop()