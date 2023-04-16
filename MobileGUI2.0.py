from tkinter import *
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as messagebox
import sqlite3

# Define the main window
root = tk.Tk()
root.title("Phone Store Management")

# Define the database connection
conn = sqlite3.connect('phone_store.db')
c = conn.cursor()

# Create the table if it doesn't exist
c.execute('''CREATE TABLE IF NOT EXISTS phones
            (model text, brand text, price real, stock integer)''')
conn.commit()


# Define the validation functions


def open_add_phone_window():
    add_phone_window = tk.Toplevel(root)
    add_phone_window.title("Add Phone")
    add_phone_window.configure(bg="#87CEFA") # set background color to light blue

    model_label = Label(add_phone_window, text="Model:", bg="#87CEFA", fg="#000080")
    model_entry = Entry(add_phone_window)
    model_label.grid(row=0, column=0, padx=10, pady=10)
    model_entry.grid(row=0, column=1, padx=10, pady=10)

    brand_label = Label(add_phone_window, text="Brand:", bg="#87CEFA", fg="#000080")
    brand_entry = Entry(add_phone_window)
    brand_label.grid(row=1, column=0, padx=10, pady=10)
    brand_entry.grid(row=1, column=1, padx=10, pady=10)

    price_label = Label(add_phone_window, text="Price:", bg="#87CEFA", fg="#000080")
    price_entry = Entry(add_phone_window)
    price_label.grid(row=2, column=0, padx=10, pady=10)
    price_entry.grid(row=2, column=1, padx=10, pady=10)

    stock_label = Label(add_phone_window, text="Stock:", bg="#87CEFA", fg="#000080")
    stock_entry = Entry(add_phone_window)
    stock_label.grid(row=3, column=0, padx=10, pady=10)
    stock_entry.grid(row=3, column=1, padx=10, pady=10)
    
    def add_phone():
        model = model_entry.get().strip()
        brand = brand_entry.get().strip()
        if not model:
            messagebox.showerror("Error", "Please enter a valid model.")
            return
        elif not brand:
            messagebox.showerror("Error", "Please enter a valid brand.")
            return
        
        try:
            price = float(price_entry.get())
            if price <= 0:
                raise messagebox.showerror("Add Error", "Price must be a positive number.")
        except ValueError:
            messagebox.showerror("Add Error", "Invalid price entered.")
            return
        
        try:
            stock = int(stock_entry.get())
            if stock <= 0:
                raise messagebox.showerror("Add Error", "Stock must be a positive number.")
        except ValueError:
            messagebox.showerror("Add Error", "Invalid stock entered.")
            return
        
        c.execute("INSERT INTO phones VALUES (?, ?, ?, ?)", (model, brand, price, stock))
        messagebox.showinfo("Success", f"Your {brand} {model} has been added successfully!")
        conn.commit()
        clear_entries()
        add_phone_window.destroy()
    

    add_button = Button(add_phone_window, text="ADD", command=add_phone, bg="#0077C2", fg="white", font=("Arial", 12, "bold"))
    add_button.grid(row=4, column=1, pady=10)
    

# Add the validation functions to the input fields


def list_phones():
    # Create a new window for the table
    table_window = tk.Toplevel(root)
    table_window.title("Phone Store Inventory")

    # Define a custom style for the Treeview widget
    custom_style = ttk.Style()
    custom_style.configure("Custom.Treeview", background="#007EA7", foreground="#00171F", fieldbackground="#007EA7")
    custom_style.map("Custom.Treeview", background=[("selected", "#F9D5E5")], foreground=[("selected", "black")])

    # Create a new Treeview widget in the new window with the custom style
    phones_list = ttk.Treeview(table_window, style="Custom.Treeview", columns=("model", "brand", "price", "stock"))
    phones_list.heading("model", text="Model")
    phones_list.heading("brand", text="Brand")
    phones_list.heading("price", text="Price")
    phones_list.heading("stock", text="Stock")

    # Populate the Treeview widget with the data from the database
    for row in c.execute("SELECT * FROM phones"):
        if row[3] < 20:
            # Add a tag to the row if stock is low
            phones_list.insert("", "end", values=row, tags=("low_stock",))
        else:
            phones_list.insert("", "end", values=row)
    
    # Configure the style for the tags
    phones_list.tag_configure("low_stock", background="#D54441")

    # Add the Treeview widget to the new window
    phones_list.pack()

def search_phone():
    # Create a new window for the search dialog
    search_window = tk.Toplevel(root)
    search_window.title("Search Phones")
    search_window.configure(bg="#87CEFA")

    # Create the widgets for the search dialog
    model_label = ttk.Label(search_window, text="Model:", background="#87CEFA")
    model_entry = ttk.Entry(search_window)
    brand_label = ttk.Label(search_window, text="Brand:", background="#87CEFA")
    brand_entry = ttk.Entry(search_window)

    # Define a style for the search button
    search_button_style = ttk.Style()
    search_button_style.configure("Search.TButton", font=("Arial", 12), foreground="white", background="#0070C0", padding=10)

    search_button = ttk.Button(search_window, text="Search", command=lambda: perform_search(model_entry.get(), brand_entry.get()), style="Search.TButton")

    # Add the widgets to the search window
    model_label.pack(padx=5, pady=5)
    model_entry.pack(padx=5, pady=5)
    brand_label.pack(padx=5, pady=5)
    brand_entry.pack(padx=5, pady=5)
    search_button.pack(padx=5, pady=5)

    def perform_search(model, brand):
        if not model and not brand:
            messagebox.showerror("Search Error", "Please enter a model or a brand to perform the search.")
            return
        if not model:
            messagebox.showerror("Search Error", "Please enter a valid model.")
            return
        elif not brand:
            messagebox.showerror("Search Error", "Please enter a valid brand.")
            return
        # Close the search window
        search_window.destroy()

        # Perform the search with the given model and brand
        search_results = list(c.execute("SELECT * FROM phones WHERE model=? AND brand=?", (model, brand)))
        if search_results:
            # Create a new window to display search results
            results_window = tk.Toplevel(root)
            results_window.title("Search Results")
            custom_style = ttk.Style()
            custom_style.configure("Custom.Treeview", background="#007EA7", foreground="#00171F", fieldbackground="#007EA7")
            custom_style.map("Custom.Treeview", background=[("selected", "#F9D5E5")], foreground=[("selected", "black")])
            # Create the list of phones widget
            search_list = ttk.Treeview(results_window,style="Custom.Treeview", columns=("model", "brand", "price", "stock"))
            search_list.heading("model", text="Model")
            search_list.heading("brand", text="Brand")
            search_list.heading("price", text="Price")
            search_list.heading("stock", text="Stock")
            
            # Configure the style for the tags
            search_list.tag_configure("low_stock", background="#D54441")

            # Add the search results to the list of phones widget
            for result in search_results:
                if result[3] < 20:
                    # Add a tag to the row if stock is low
                    search_list.insert("", "end", values=result, tags=("low_stock",))
                else:
                    search_list.insert("", "end", values=result)

            # Add the widgets to the search results window
            search_list.pack(padx=5, pady=5)
        else:
            messagebox.showerror("Search Results", f"No results found for {brand} {model}.")

def remove_phone():
    # Create a new window for the remove dialog
    remove_window = tk.Toplevel(root)
    remove_window.title("Remove Phones")
    remove_window.configure(bg="#87CEFA")

    # Create the widgets for the remove dialog
    model_label = ttk.Label(remove_window, text="Model:", background="#87CEFA")
    model_entry = ttk.Entry(remove_window)
    brand_label = ttk.Label(remove_window, text="Brand:", background="#87CEFA")
    brand_entry = ttk.Entry(remove_window)
    remove_button = ttk.Button(remove_window, text="Remove", command=lambda: perform_remove(model_entry.get(), brand_entry.get()), style='Colorful.TButton')

    # Create a custom style for the remove button
    remove_style = ttk.Style()
    remove_style.configure("Colorful.TButton", font=("Arial", 12), foreground="white", background="#0070C0", padding=10)

    # Add the widgets to the remove window
    model_label.pack(padx=5, pady=5)
    model_entry.pack(padx=5, pady=5)
    brand_label.pack(padx=5, pady=5)
    brand_entry.pack(padx=5, pady=5)
    remove_button.pack(padx=5, pady=5)

    def perform_remove(model, brand):
        # Check if model and brand are valid
        if not model and not brand:
            messagebox.showerror("Remove Error", "Please enter a model or a brand to perform.")
            return
        if not model:
            messagebox.showerror("Remove Error", "Please enter a valid model.")
            return
        elif not brand:
            messagebox.showerror("Remove Error", "Please enter a valid brand.")
            return

        # Close the remove window
        remove_window.destroy()

        # Perform the remove with the given model and brand
        remove_results = c.execute("DELETE FROM phones WHERE model=? AND brand=?", (model, brand)).rowcount
        conn.commit()
        clear_entries()

        if remove_results > 0:
            messagebox.showinfo("Success", f"Your {model} {brand} has been removed!")
        else:
            messagebox.showerror("Remove Error", f"No results found for {model} {brand}.")
def sell_phone():
    # Create a new window for the sell dialog
    sell_window = tk.Toplevel(root)
    sell_window.title("Sell Phones")
    sell_window.configure(bg="#87CEFA")
    
    # Create the widgets for the sell dialog
    model_label = ttk.Label(sell_window, text="Model:", background="#87CEFA")
    model_entry = ttk.Entry(sell_window)
    brand_label = ttk.Label(sell_window, text="Brand:", background="#87CEFA")
    brand_entry = ttk.Entry(sell_window)
    quantity_label = ttk.Label(sell_window, text="Quantity:", background="#87CEFA")
    quantity_entry = ttk.Entry(sell_window)
    sell_button = ttk.Button(sell_window, text="Sell", command=lambda: perform_sell(model_entry.get(), brand_entry.get(), quantity_entry.get()), style='Colorful.TButton')
    # Create a custom style for the sell button
    sell_style = ttk.Style()
    sell_style.configure("Colorful.TButton", font=("Arial", 12), foreground="white", background="#0070C0", padding=10)
    # Add the widgets to the sell window
    model_label.pack(padx=5, pady=5)
    model_entry.pack(padx=5, pady=5)
    brand_label.pack(padx=5, pady=5)
    brand_entry.pack(padx=5, pady=5)
    quantity_label.pack(padx=5, pady=5)
    quantity_entry.pack(padx=5, pady=5)
    sell_button.pack(padx=5, pady=5)

    def perform_sell(model, brand, quantity):
        if not model and not brand and not quantity:
            messagebox.showerror("Sell Error", "Please enter a model, a brand and quantity to perform.")
            return
        if not model and not brand:
            messagebox.showerror("Sell Error", "Please enter a model and a brand to perform.")
            return
        if not model:
            messagebox.showerror("Sell Error", "Please enter a valid model.")
            return
        elif not brand:
            messagebox.showerror("Sell Error", "Please enter a valid brand.")
            return
        try:
            quantity = int(quantity)
            if quantity <= 0:
                raise messagebox.showerror("Sell Error", "Quantity must be a positive number.")
        except ValueError:
            messagebox.showerror("Sell Error", "Invalid quantity entered.")
            return

        # Close the sell window
        sell_window.destroy()

        # Perform the sell with the given model, brand, and quantity
        c.execute("UPDATE phones SET stock=stock - ? WHERE model=? AND brand=?", (quantity, model, brand))
        if c.rowcount > 0:
            conn.commit()
            clear_entries()
            messagebox.showinfo("Success", f"You sold {quantity} {brand} {model}!")
        else:
            messagebox.showerror("Sell Error", f"No results found for {brand} {model}.")

def restock_phone():
    # Create a new window for the restock dialog
    restock_window = tk.Toplevel(root)
    restock_window.title("Restock Phones")
    restock_window.configure(bg="#87CEFA") 

    # Create the widgets for the restock dialog
    model_label = ttk.Label(restock_window, text="Model:",background="#87CEFA")
    model_entry = ttk.Entry(restock_window)
    brand_label = ttk.Label(restock_window, text="Brand:",background="#87CEFA")
    brand_entry = ttk.Entry(restock_window)
    quantity_label = ttk.Label(restock_window, text="Quantity:",background="#87CEFA")
    quantity_entry = ttk.Entry(restock_window)
    restock_button = ttk.Button(restock_window, text="Restock", command=lambda: perform_restock(model_entry.get(), brand_entry.get(), quantity_entry.get()), style='Colorful.TButton')
    # Create a custom style for the sell button
    restock_style = ttk.Style()
    restock_style.configure("Colorful.TButton", font=("Arial", 12), foreground="white", background="#0070C0", padding=10)
    # Add the widgets to the restock window
    model_label.pack(padx=5, pady=5)
    model_entry.pack(padx=5, pady=5)
    brand_label.pack(padx=5, pady=5)
    brand_entry.pack(padx=5, pady=5)
    quantity_label.pack(padx=5, pady=5)
    quantity_entry.pack(padx=5, pady=5)
    restock_button.pack(padx=5, pady=5)

    def perform_restock(model, brand, quantity):
        if not model and not brand and not quantity:
            messagebox.showerror("Restock Error", "Please enter a model, a brand and quantity to perform.")
            return
        if not model and not brand:
            messagebox.showerror("Restock Error", "Please enter a model and a brand to perform.")
            return
        if not model:
            messagebox.showerror("Restock Error", "Please enter a valid model.")
            return
        elif not brand:
            messagebox.showerror("Restock Error", "Please enter a valid brand.")
            return
        try:
            quantity = int(quantity)
            if quantity <= 0:
                raise messagebox.showerror("Restock Error", "Quantity must be a positive number.")
        except ValueError:
            messagebox.showerror("Restock Error", "Invalid quantity entered.")
            return

        # Check if the model and brand are in the database
        c.execute("SELECT * FROM phones WHERE model=? AND brand=?", (model, brand))
        if c.fetchone() is None:
            messagebox.showerror("Restock Error", f"No results found for {brand} {model}.")
            return

        # Update the stock of the phone in the database
        c.execute("UPDATE phones SET stock=stock + ? WHERE model=? AND brand=?", (quantity, model, brand))
        conn.commit()
        clear_entries()
        messagebox.showinfo("Success", f"You restocked {quantity} {brand} {model}!")
        
        # Close the restock window
        restock_window.destroy()
        
def exit_program():
    root.destroy()

def clear_entries():
    model_entry.delete(0, tk.END)
    brand_entry.delete(0, tk.END)
    price_entry.delete(0, tk.END)
    stock_entry.delete(0, tk.END)

# Define the input fields
model_label = ttk.Label(root, text="Model")
model_entry = ttk.Entry(root)
brand_label = ttk.Label(root, text="Brand")
brand_entry = ttk.Entry(root)
price_label = ttk.Label(root, text="Price")
price_entry = ttk.Entry(root)
stock_label = ttk.Label(root, text="Stock")
stock_entry = ttk.Entry(root)


# Create the main window
root.geometry("800x600")
root.config(background="#00A8E8")

# Define a custom style for the widgets
custom_style = ttk.Style()

# Define a color scheme for the custom style
custom_style.configure("Custom.TButton", 
                        background="#008080", 
                        foreground="#ffffff", 
                        font=("Montserrat", 12),
                        borderwidth=0,
                        padx=10,
                        pady=5)
custom_style.map("Custom.TButton",
                    background=[("active", "#003459")],
                    foreground=[("active", "#ffffff")],
                    font=[("active", ("Montserrat", 12, "bold"))]
                    )

custom_style.configure("Custom.TLabel", 
                        background="#00171F", 
                        foreground="#003459", 
                        font=("Montserrat", 12),
                        padding=10)

# Apply the custom style to the widgets
ttk.Style().theme_use("clam")
ttk.Style().configure(".", font=("Montserrat", 12), background="#00A8E8", foreground="#00171F")
ttk.Style().configure("TEntry", padding=10, relief="flat", fieldbackground="#ffffff")
ttk.Style().configure("TCombobox", padding=10, relief="flat", fieldbackground="#3b3f4a")
ttk.Style().configure("TButton", padding=10, relief="flat", background="#007EA7", foreground="#00171F", font=("Montserrat", 12,))

# Create the widgets for the main window
title_label = ttk.Label(root, text="Phone Inventory System", style="Custom.TLabel")
# Define the buttons with styles and commands
add_phone_button = ttk.Button(root, text="Add Phone", style="Custom.TButton", command=open_add_phone_window)
list_button = ttk.Button(root, text="List Phones", style="Custom.TButton", command=list_phones)
search_button = ttk.Button(root, text="Search Phone", style="Custom.TButton", command=search_phone)
remove_button = ttk.Button(root, text="Remove Phone", style="Custom.TButton", command=remove_phone)
sell_button = ttk.Button(root, text="Sell Phone", style="Custom.TButton", command=sell_phone)
restock_button = ttk.Button(root, text="Restock Phone", style="Custom.TButton", command=restock_phone)
exit_button = ttk.Button(root, text="Exit", style="Custom.TButton", command=exit_program)


# Add the buttons to the main window
add_phone_button.pack(padx=10, pady=10)
list_button.pack(padx=10, pady=10)
search_button.pack(padx=10, pady=10)
remove_button.pack(padx=10, pady=10)
sell_button.pack(padx=10, pady=10)
restock_button.pack(padx=10, pady=10)
exit_button.pack(padx=10, pady=10)

# Run the main loop
root.mainloop()

# Close the database connection when the program is done
conn.close()