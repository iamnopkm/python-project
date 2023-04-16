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
def validate_price():
    try:
        float(price_entry.get())
        return True
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid price.")
        return False

def validate_stock():
    try:
        int(stock_entry.get())
        return True
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid stock quantity.")
        return False

def add_phone():
    if validate_price() and validate_stock():
        model = model_entry.get()
        brand = brand_entry.get()
        price = float(price_entry.get())
        stock = int(stock_entry.get())
        c.execute("INSERT INTO phones VALUES (?, ?, ?, ?)", (model, brand, price, stock))
        messagebox.showinfo("Success", f"Your {brand} {model} has been added successfully!")
        conn.commit()
        clear_entries()
        list_phones()

# Add the validation functions to the input fields
price_entry = ttk.Entry(root)
stock_entry = ttk.Entry(root)
price_entry.config(validate="key", validatecommand=validate_price)
stock_entry.config(validate="key", validatecommand=validate_stock)

def list_phones():
    # Create a new window for the table
    table_window = tk.Toplevel(root)
    table_window.title("Phone Store Inventory")
    
    # Create a new Treeview widget in the new window
    phones_list = ttk.Treeview(table_window, columns=("model", "brand", "price", "stock"))
    phones_list.heading("model", text="Model")
    phones_list.heading("brand", text="Brand")
    phones_list.heading("price", text="Price")
    phones_list.heading("stock", text="Stock")
    
    # Populate the Treeview widget with the data from the database
    for row in c.execute("SELECT * FROM phones"):
        phones_list.insert("", "end", values=row)
    
    # Add the Treeview widget to the new window
    phones_list.pack()

def search_phone():
    model = model_entry.get()
    if search_results := list(
        c.execute("SELECT * FROM phones WHERE model=?", (model,))
    ):
        # Create a new window to display search results
        search_window = tk.Toplevel(root)
        search_window.title("Search Results")

        # Create the list of phones widget
        search_list = ttk.Treeview(search_window, columns=("model", "brand", "price", "stock"))
        search_list.heading("model", text="Model")
        search_list.heading("brand", text="Brand")
        search_list.heading("price", text="Price")
        search_list.heading("stock", text="Stock")

        # Add the search results to the list of phones widget
        for result in search_results:
            search_list.insert("", "end", values=result)

        # Add the widgets to the search window
        search_list.pack(padx=5, pady=5)
    else:
        messagebox.showerror("Search Results", f"No results found for {model}.")

def remove_phone():
    model = model_entry.get()
    c.execute("DELETE FROM phones WHERE model=?", (model,))
    conn.commit()
    clear_entries()
    list_phones()
    messagebox.showinfo("Success", f"Your {model} has been removed!")

def sell_phone():
    model = model_entry.get()
    c.execute("UPDATE phones SET stock=stock - 1 WHERE model=?", (model,))
    conn.commit()
    messagebox.showinfo("Success", f"Your {model} has been sold!")

def restock_phone():
    model = model_entry.get()
    amount = int(stock_entry.get())
    c.execute("UPDATE phones SET stock=stock + ? WHERE model=?", (amount,model))
    conn.commit()
    list_phones()

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

# Define the buttons
add_button = ttk.Button(root, text="Add Phone", command=add_phone)
list_button = ttk.Button(root, text="List Phones", command=list_phones)
search_button = ttk.Button(root, text="Search Phone", command=search_phone)
remove_button = ttk.Button(root, text="Remove Phone", command=remove_phone)
sell_button = ttk.Button(root, text="Sell Phone", command=sell_phone)
restock_button = ttk.Button(root, text="Restock Phone", command=restock_phone)


# Add the widgets to the main window
model_label.grid(row=0, column=0, padx=5, pady=5)
model_entry.grid(row=0, column=1, padx=5, pady=5)
brand_label.grid(row=1, column=0, padx=5, pady=5)
brand_entry.grid(row=1, column=1, padx=5, pady=5)
price_label.grid(row=2, column=0, padx=5, pady=5)
price_entry.grid(row=2, column=1, padx=5, pady=5)
stock_label.grid(row=3, column=0, padx=5, pady=5)
stock_entry.grid(row=3, column=1, padx=5, pady=5)
add_button.grid(row=4, column=0, padx=5, pady=5)
list_button.grid(row=4, column=1, padx=5, pady=5)
search_button.grid(row=5, column=0, padx=5, pady=5)
remove_button.grid(row=5, column=1, padx=5, pady=5)
sell_button.grid(row=6, column=0, padx=5, pady=5)
restock_button.grid(row=6, column=1, padx=5, pady=5)


# Run the main loop
root.mainloop()

# Close the database connection when the program is done
conn.close()