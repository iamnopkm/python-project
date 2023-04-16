from tkinter import *
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as messagebox
import sqlite3
from PIL import Image,ImageTk
from OperationUI.OperationCommandGUI import *
from OperationUI.Colors import *


if __name__ == "__main__":
# Create the main window
    root.geometry("1440x826")
    root.config(background="#FFCAD4")
    root.grid_columnconfigure((0,1), weight=1)
    image = Image.open("./Image/mobile_store.png")
    image.geometry = "900x750"
    image_logo = ImageTk.PhotoImage(image)
    image_label = tk.Label(image=image_logo, background="#FFCAD4")
    # label1.image = image_logo
    image_label.place(x=400,y=0)
   
    """Product buttons"""
    
    add_phone_button = Button(root, text="Add Phone", command=open_add_phone_window, bg=MINUS_PINK, borderwidth=3, fg="white", font=("VNI-Vari", 12, "bold"))
    add_phone_button.grid(row=4, column=0, pady=10)
    
    remove_button = Button(root, text="Remove Phone", command=remove_phone, bg=MINUS_PINK, borderwidth=3, fg="white", font=("VNI-Vari", 12, "bold"))
    remove_button.grid(row=5, column=0, pady=10)
    
    search_button = Button(root, text="Search Phone", command=search_phone, bg=MINUS_PINK, borderwidth=3, fg="white", font=("VNI-Vari", 12, "bold"))
    search_button.grid(row=6, column=0, pady=10)
    
    restock_button = Button(root, text="Restock Phone", command=restock_phone, bg=MINUS_PINK, borderwidth=3, fg="white", font=("VNI-Vari", 12, "bold"))
    restock_button.grid(row=7, column=0, pady=10)
    
    list_button = Button(root, text="List Phones", command=list_phones, bg=MINUS_PINK, borderwidth=3, fg="white", font=("VNI-Vari", 12, "bold"))
    list_button.grid(row=8, column=0, pady=10)

    """Customer buttons"""

    add_customer_button = Button(root, text="Add Customer", command=add_customer, bg=MINUS_PINK, borderwidth=3, fg="white", font=("VNI-Vari", 12, "bold"))
    
    add_customer_button.grid(row=4, column=1, pady=10)
    
    remove_customer_button = Button(root, text="Remove Customer", command=remove_customer, bg=MINUS_PINK, borderwidth=3, fg="white", font=("VNI-Vari", 12, "bold"))
    remove_customer_button.grid(row=5, column=1,columnspan=1, pady=10)
    
    search_customer_button = Button(root, text="Search Customer", command=search_customer, bg=MINUS_PINK, borderwidth=3, fg="white", font=("VNI-Vari", 12, "bold"))
    search_customer_button.grid(row=6, column=1, pady=10)
    
    edit_customer_button = Button(root, text="Edit Customer", command=edit_customer, bg=MINUS_PINK, borderwidth=3, fg="white", font=("VNI-Vari", 12, "bold"))
    edit_customer_button.grid(row=7, column=1, pady=10)
    
    list_customer_button = Button(root, text="List Customers", command=list_customer, bg=MINUS_PINK, borderwidth=3, fg="white", font=("VNI-Vari", 12, "bold"))
    list_customer_button.grid(row=8, column=1, pady=10)
    
    """EXIT button"""
    
    exit_button = Button(root, text="Exit Program", command=exit_program, bg=RED, fg="white", borderwidth=3, font=("VNI-Vari", 12, "bold"))
    exit_button.grid(row=9, column=0,columnspan=2, pady=10)


    # Run the main loop
    root.mainloop()

    # Close the database connection when the program is done
    conn.close()