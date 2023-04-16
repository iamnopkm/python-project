from tkinter import *
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as messagebox
import sqlite3
from PIL import Image,ImageTk

# Define the main window
root = tk.Tk()
root.title("Phone Store Management")

# Define the database connection
conn = sqlite3.connect('phone_store.db')
c = conn.cursor()

# Create the table if it doesn't exist
c.execute('''CREATE TABLE IF NOT EXISTS phones
            (model text, brand text, price real, stock integer)''')
c.execute('''CREATE TABLE IF NOT EXISTS customers
            (id text, name text, phonenum text, phonebrandsold text, phonemodelsold text)''')
conn.commit()


# Define the validation functions
def add_customer():
    add_customer_window = tk.Toplevel(root)
    add_customer_window.title("Add Customer")
    add_customer_window.configure(bg="#FFCAD4")

    name_label = Label(add_customer_window, text="Name:", bg="#FFCAD4", fg="black")
    name_entry = Entry(add_customer_window)
    name_label.grid(row=0, column=0, padx=10, pady=10)
    name_entry.grid(row=0, column=1, padx=10, pady=10)

    customer_id_label = Label(add_customer_window, text="Id:", bg="#FFCAD4", fg="black")
    customer_id_entry = Entry(add_customer_window)
    customer_id_label.grid(row=1, column=0, padx=10, pady=10)
    customer_id_entry.grid(row=1, column=1, padx=10, pady=10)

    phone_number_label = Label(add_customer_window, text="Phone Number: ", bg="#FFCAD4", fg="black")
    phone_number_entry = Entry(add_customer_window)
    phone_number_label.grid(row=2, column=0, padx=10, pady=10)
    phone_number_entry.grid(row=2, column=1, padx=10, pady=10)

    phone_model_information_label = Label(add_customer_window, text="Phone Model Sold Information: ", bg="#FFCAD4", fg="black")
    phone_model_information_entry = Entry(add_customer_window)
    phone_model_information_label.grid(row=3, column=0, padx=10, pady=10)
    phone_model_information_entry.grid(row=3, column=1, padx=10, pady=10)
    
    phone_brand_information_label = Label(add_customer_window, text="Phone Brand Sold Information: ", bg="#FFCAD4", fg="black")
    phone_brand_information_entry = Entry(add_customer_window)
    phone_brand_information_label.grid(row=4, column=0, padx=10, pady=10)
    phone_brand_information_entry.grid(row=4, column=1, padx=10, pady=10)
    
    def perform_add_customer():
        name = name_entry.get().strip()
        customer_id = customer_id_entry.get()
        PhoneNum = phone_number_entry.get()
        phone_model_information= phone_model_information_entry.get().strip()
        phone_brand_information= phone_brand_information_entry.get().strip()
        
        if not name:
            messagebox.showerror("Error", "Please enter a valid name.")
            return
        if name.isdigit():
            return messagebox.showerror("Error", "Customer's name can't have number.")
        
        if not customer_id:
            messagebox.showerror("Error", "Please enter a valid ID.")
            return
        
        if customer_id:
            search_test = list(c.execute("SELECT * FROM customers WHERE id=?", (customer_id,)))
            if search_test:
                messagebox.showerror("Add Error", "ID existed. Please enter a valid ID.")
                return
            
        if not PhoneNum:
            messagebox.showerror("Add Error", "Invalid phone number entered.")
            return
        if PhoneNum:
            PhoneNumInt = int(PhoneNum)
            if PhoneNumInt < 0:
                raise messagebox.showerror("Add Error", "Phone number must be a positive number.")
        if len(PhoneNum) not in {10, 8}:
                raise messagebox.showerror("Add Error", "Phone number must have 10 numbers.")
            
        if not phone_model_information:
            messagebox.showerror("Error", "Please enter a valid phone model sold information.")
            return
        
        if not phone_brand_information:
            messagebox.showerror("Error", "Please enter a valid phone brand sold information.")
            return
        
        search_results = list(c.execute("SELECT * FROM phones WHERE model=? AND brand=?", (phone_model_information, phone_brand_information)))
        if search_results:
            c.execute("UPDATE phones SET stock=stock - 1 WHERE model=? AND brand=?", (phone_model_information, phone_brand_information))
        if c.rowcount > 0:
            messagebox.showinfo("Success", f"You have sold {phone_brand_information} {phone_model_information} to {name}!")
            c.execute("INSERT INTO customers VALUES (?, ?, ?, ?, ?)", (customer_id, name, PhoneNum, phone_brand_information, phone_model_information))
            conn.commit()
            add_customer_window.destroy()
        else:
            messagebox.showerror("Search Results", f"No results found for {phone_brand_information} {phone_model_information}.")
    add_button = Button(add_customer_window, text="Add", command=perform_add_customer,borderwidth=3, bg="#F4ACB7", fg="white", font=("VNI-Vari", 12, "bold"))
    add_button.grid(row=5, column=1,columnspan=2, pady=10)
    def cancel_add():
        add_customer_window.destroy()
    cancel_button = Button(add_customer_window, text="Cancel", command=cancel_add,borderwidth=3, bg="#D00050", fg="white", font=("VNI-Vari", 12, "bold"))
    cancel_button.grid(row=5, column=0,columnspan=1, pady=10)
def edit_customer():
    edit_customer_window = tk.Toplevel(root)
    edit_customer_window.title("Edit Customer")
    edit_customer_window.configure(bg="#FFCAD4")

    # Create the widgets for the edit dialog
    name_label = Label(edit_customer_window, text="Name:", bg="#FFCAD4", fg="black")
    name_entry = Entry(edit_customer_window)
    name_label.grid(row=0, column=0, padx=10, pady=10)
    name_entry.grid(row=0, column=1, padx=10, pady=10)

    customer_id_label = Label(edit_customer_window, text="ID:", bg="#FFCAD4", fg="black")
    customer_id_entry = Entry(edit_customer_window)
    customer_id_label.grid(row=1, column=0, padx=10, pady=10)
    customer_id_entry.grid(row=1, column=1, padx=10, pady=10)
    
    edit_button = Button(edit_customer_window, text="Edit", command=lambda: perform_customer_edit(name_entry.get(), customer_id_entry.get()), borderwidth=3, bg="#F4ACB7", fg="white", font=("VNI-Vari", 12, "bold"))
    edit_button.grid(row=3, column=1,columnspan=2, pady=10)
    def cancel_add():
        edit_customer_window.destroy()
    cancel_button = Button(edit_customer_window, text="Cancel", command=cancel_add,borderwidth=3, bg="#D00050", fg="white", font=("VNI-Vari", 12, "bold"))
    cancel_button.grid(row=3, column=0,columnspan=1, padx=50, pady=10)
    
    def perform_customer_edit(name,customer_id):
        # Check if name and customer_id are valid
        if not name and not customer_id:
            messagebox.showerror("Edit Error", "Please enter both name and ID to perform.")
            return
        if not name:
            messagebox.showerror("Edit Error", "Please enter a valid name.")
            return
        if name.isdigit():
            return messagebox.showerror("Error", "Customer's name can't have number.")
        elif not customer_id:
            messagebox.showerror("Edit Error", "Please enter a valid id.")
            return
        # Close the edit window
        search_edit_results = list(c.execute("SELECT * FROM customers WHERE name=? AND id=?", (name,customer_id)))
        if search_edit_results:
            def perform_edit_name():
                edit_name_window = tk.Toplevel(root)
                edit_name_window.title("Edit Name")
                edit_name_window.configure(bg="#FFCAD4")
                
                new_name_label = Label(edit_name_window, text="New Name:", bg="#FFCAD4", fg="black")
                new_name_entry = Entry(edit_name_window)
                new_name_label.grid(row=0, column=0, padx=10, pady=10)
                new_name_entry.grid(row=0, column=1, padx=10, pady=10)
                
                edit_name = Button(edit_name_window, text="Confirm", command=lambda: update_name(new_name_entry.get()), bg="#F4ACB7", borderwidth=3, fg="white", font=("VNI-Vari", 12, "bold"))
                edit_name.grid(row=1, column=1, columnspan=2, pady=10)
                def cancel_add():
                    edit_name_window.destroy()
                cancel_button = Button(edit_name_window, text="Cancel", command=cancel_add,borderwidth=3, bg="#D00050", fg="white", font=("VNI-Vari", 12, "bold"))
                cancel_button.grid(row=1, column=0,columnspan=1, padx=50, pady=10)
                
                def update_name(new_name):
                    edit_customer_window.destroy()
                    if not new_name:
                        messagebox.showerror("Error", "Please enter a valid name.")
                        return
                    if new_name.isdigit():
                        return messagebox.showerror("Error", "Customer's name can't have number.")
                    edit_name_results = c.execute("UPDATE customers SET name=? WHERE id=?", (new_name,customer_id)).rowcount
                    if edit_name_results > 0:
                        messagebox.showinfo("Success", f"You have change {name} into {new_name}!")
                        conn.commit()
                        edit_name_window.destroy()
            def perform_edit_id():
                edit_id_window = tk.Toplevel(root)
                edit_id_window.title("Edit ID")
                edit_id_window.configure(bg="#FFCAD4")
                
                new_id_label = Label(edit_id_window, text="New ID:", bg="#FFCAD4", fg="black")
                new_id_entry = Entry(edit_id_window)
                new_id_label.grid(row=0, column=0, padx=10, pady=10)
                new_id_entry.grid(row=0, column=1, padx=10, pady=10)
                
                edit_id = Button(edit_id_window, text="Confirm", command=lambda: update_id(new_id_entry.get()), bg="#F4ACB7", borderwidth=3, fg="white", font=("VNI-Vari", 12, "bold"))
                edit_id.grid(row=1, column=1, columnspan=2, pady=10)
                def cancel_add():
                    edit_id_window.destroy()
                cancel_button = Button(edit_id_window, text="Cancel", command=cancel_add,borderwidth=3, bg="#D00050", fg="white", font=("VNI-Vari", 12, "bold"))
                cancel_button.grid(row=1, column=0,columnspan=1, padx=50, pady=10)
                
                def update_id(new_id):
                    edit_options_window.destroy()
                    if not new_id:
                        messagebox.showerror("Error", "Please enter a valid id.")
                        return
                    if new_id:
                        search_test = list(c.execute("SELECT * FROM customers WHERE id=?", (new_id,)))
                        if search_test:
                            messagebox.showerror("Add Error", "ID existed. Please enter a valid ID.")
                            return
                    edit_id_results = c.execute("UPDATE customers SET id=? WHERE name=?", (new_id,name)).rowcount
                    if edit_id_results > 0:
                        messagebox.showinfo("Success", f"You have change ID {customer_id} into {new_id}!")
                        conn.commit()
                        edit_id_window.destroy()
            def perform_edit_phonenum():
                edit_phone_num_window = tk.Toplevel(root)
                edit_phone_num_window.title("Edit Phone Number")
                edit_phone_num_window.configure(bg="#FFCAD4")
                
                new_phone_num_label = Label(edit_phone_num_window, text="New Phone Number:", bg="#FFCAD4", fg="black")
                new_phone_num_entry = Entry(edit_phone_num_window)
                new_phone_num_label.grid(row=0, column=0, padx=10, pady=10)
                new_phone_num_entry.grid(row=0, column=1, padx=10, pady=10)
                
                edit_phone_num = Button(edit_phone_num_window, text="Confirm", command=lambda: update_phone_num(new_phone_num_entry.get()), bg="#F4ACB7", borderwidth=3, fg="white", font=("VNI-Vari", 12, "bold"))
                edit_phone_num.grid(row=1, column=1, columnspan=2, pady=10)
                def cancel_add():
                    edit_phone_num_window.destroy()
                cancel_button = Button(edit_phone_num_window, text="Cancel", command=cancel_add,borderwidth=3, bg="#D00050", fg="white", font=("VNI-Vari", 12, "bold"))
                cancel_button.grid(row=1, column=0,columnspan=1, padx=50, pady=10)
                
                def update_phone_num(new_phone_num):
                    edit_options_window.destroy()
                    if not new_phone_num:
                        messagebox.showerror("Error", "Please enter a valid phone number.")
                        return
                    if new_phone_num:
                        PhoneNumInt = int(new_phone_num)
                        if PhoneNumInt < 0:
                            raise messagebox.showerror("Add Error", "Phone number must be a positive number.")
                    if len(new_phone_num) not in {10, 8}:
                            raise messagebox.showerror("Add Error", "Phone number must have 10 numbers.")
                        
                    edit_phone_num_results = c.execute("UPDATE customers SET phonenum=? WHERE id=?", (new_phone_num,customer_id)).rowcount
                    if edit_phone_num_results > 0:
                        messagebox.showinfo("Success", f"You have change {name}'s number into {new_phone_num}!")
                        conn.commit()
                        edit_phone_num_window.destroy()
            def perform_edit_model_brand():
                edit_model_and_brand_window = tk.Toplevel(root)
                edit_model_and_brand_window.title("Edit Model And Brand")
                edit_model_and_brand_window.configure(bg="#FFCAD4")
                
                model_label = Label(edit_model_and_brand_window, text="New Model:", bg="#FFCAD4", fg="black")
                model_entry = Entry(edit_model_and_brand_window)
                model_label.grid(row=0, column=0, padx=10, pady=10)
                model_entry.grid(row=0, column=1, padx=10, pady=10)

                brand_label = Label(edit_model_and_brand_window, text="New Brand:", bg="#FFCAD4", fg="black")
                brand_entry = Entry(edit_model_and_brand_window)
                brand_label.grid(row=1, column=0, padx=10, pady=10)
                brand_entry.grid(row=1, column=1, padx=10, pady=10)
                
                edit_model_brand = Button(edit_model_and_brand_window, text="Confirm", command=lambda: update_model_brand(model_entry.get(),brand_entry.get()), bg="#F4ACB7", borderwidth=3, fg="white", font=("VNI-Vari", 12, "bold"))
                edit_model_brand.grid(row=2, column=1,columnspan=2, pady=10)
                def cancel_add():
                    edit_model_and_brand_window.destroy()
                cancel_button = Button(edit_model_and_brand_window, text="Cancel", command=cancel_add,borderwidth=3, bg="#D00050", fg="white", font=("VNI-Vari", 12, "bold"))
                cancel_button.grid(row=2, column=0,columnspan=1, padx=50, pady=10)
                
                def update_model_brand(new_model,new_brand):
                    edit_options_window.destroy()
                    if not new_model and not new_brand:
                        messagebox.showerror("Error", "Please enter a valid model and brand.")
                        return
                    if new_brand and not new_model:
                        messagebox.showerror("Error","Please enter a valid model.")
                        return
                    elif new_model and not new_brand:
                        messagebox.showerror("Error", "Please enter a valid brand.")
                        return
                    search_model_brand_results = list(c.execute("SELECT * FROM phones WHERE model=? and brand=?", (new_model,new_brand)))
                    if search_model_brand_results:
                        edit_model_brand_results = c.execute("UPDATE customers SET phonemodelsold=? AND phonebrandsold=? WHERE id=?", (new_model,new_brand,customer_id)).rowcount
                        if edit_model_brand_results > 0:
                            messagebox.showinfo("Success", f"You have change model and brand name into {new_brand} {new_model}!")
                            conn.commit()
                            edit_model_and_brand_window.destroy()
                    else:
                        messagebox.showerror("Edit Error",f"There's no {new_brand} {new_model} in shop. Please try again.")
            
            def cancel_add():
                edit_options_window.destroy()
            
            edit_options_window = tk.Toplevel(root)
            edit_options_window.title("Edit Options")
            edit_options_window.configure(bg="#FFCAD4")
            edit_options_window.grid_columnconfigure((0,1), weight=1)

            edit_name = Button(edit_options_window, text="Edit Name", command=perform_edit_name, bg="#9D8189", borderwidth=3, fg="white", font=("VNI-Vari", 12, "bold"))
            edit_name.grid(row=1, column=0, pady=10,sticky="ew")
            edit_id = Button(edit_options_window, text="Edit ID", command=perform_edit_id, bg="#9D8189", borderwidth=3, fg="white", font=("VNI-Vari", 12, "bold"))
            edit_id.grid(row=2, column=1, pady=10,sticky="ew")
            edit_phonenumber = Button(edit_options_window, text="Edit Phone Number", command=perform_edit_phonenum, bg="#9D8189", borderwidth=3, fg="white", font=("VNI-Vari", 12, "bold"))
            edit_phonenumber.grid(row=2, column=0, pady=10, sticky="ew")
            edit_model = Button(edit_options_window, text="Edit Phone Sold Model And Brand", command=perform_edit_model_brand, bg="#9D8189", borderwidth=3, fg="white", font=("VNI-Vari", 12, "bold"))
            edit_model.grid(row=1, column=1, pady=10, sticky = "ew")
            cancel_button = Button(edit_options_window, text="Cancel", command=cancel_add,borderwidth=3, bg="#D00050", fg="white", font=("VNI-Vari", 12, "bold"))
            cancel_button.grid(row=3, column=0,columnspan=2, pady=10)
        else:
            messagebox.showerror("Edit Error",f"No one have ID {customer_id} and Name {name}")
        


    
def remove_customer():
    # Create a new window for the remove dialog
    remove_customer_window = tk.Toplevel(root)
    remove_customer_window.title("Remove Customer")
    remove_customer_window.configure(bg="#FFCAD4")

    # Create the widgets for the remove dialog
    name_label = Label(remove_customer_window, text="Name:", bg="#FFCAD4", fg="black")
    name_entry = Entry(remove_customer_window)
    name_label.grid(row=0, column=0, padx=10, pady=10)
    name_entry.grid(row=0, column=1, padx=10, pady=10)

    customer_id_label = Label(remove_customer_window, text="ID:", bg="#FFCAD4", fg="black")
    customer_id_entry = Entry(remove_customer_window)
    customer_id_label.grid(row=1, column=0, padx=10, pady=10)
    customer_id_entry.grid(row=1, column=1, padx=10, pady=10)

    remove_button = Button(remove_customer_window, text="Remove", command=lambda: perform_customer_remove(name_entry.get(), customer_id_entry.get()), borderwidth=3, bg="#F4ACB7", fg="white", font=("VNI-Vari", 12, "bold"))
    remove_button.grid(row=3, column=1,columnspan=2, pady=10)
    
    def cancel_add():
        remove_customer_window.destroy()
    cancel_button = Button(remove_customer_window, text="Cancel", command=cancel_add,borderwidth=3, bg="#D00050", fg="white", font=("VNI-Vari", 12, "bold"))
    cancel_button.grid(row=3, column=0,columnspan=1, padx=50, pady=10)

    def perform_customer_remove(name, customer_id):
        # Check if name and customer_id are valid
        if not name and not customer_id:
            messagebox.showerror("Remove Error", "Please enter both name and ID to perform.")
            return
        if not name:
            messagebox.showerror("Remove Error", "Please enter a valid name.")
            return
        if name.isdigit():
            return messagebox.showerror("Error", "Customer's name can't have number.")
        elif not customer_id:
            messagebox.showerror("Remove Error", "Please enter a valid id.")
            return

        # Perform the remove with the given name and id
        remove_results = c.execute("DELETE FROM customers WHERE name=? AND id=?", (name, customer_id)).rowcount
        conn.commit()
        if remove_results > 0:
            remove_customer_window.destroy()
            messagebox.showinfo("Success", f"Customer {customer_id} {name} has been removed!")
        else:
            messagebox.showerror("Remove Error", f"No results found for {customer_id} {name}.")
def list_customer():
    # Create a new window for the table
    table_customer_window = tk.Toplevel(root)
    table_customer_window.title("Customers List")

    # Define a custom style for the Treeview widget
    custom_style = ttk.Style()
    custom_style.configure("Custom.Treeview", background="#FFCAD4", foreground="#00171F")
    custom_style.map("Custom.Treeview", background=[("selected", "#9D8189")], foreground=[("selected", "black")])

    # Create a new Treeview widget in the new window with the   custom style
    customers_list = ttk.Treeview(table_customer_window, style="Custom.Treeview", columns=("id", "name", "phonenum", "phonebrandsold", "phonemodelsold"))
    customers_list.heading("id", text="Customer ID")
    customers_list.heading("name", text="Customer Name")
    customers_list.heading("phonenum", text="Phone Number")
    customers_list.heading("phonebrandsold", text="Phone Brand Sold")
    customers_list.heading("phonemodelsold", text="Phone Model Sold")
    for row in c.execute("SELECT * FROM customers"):
        customers_list.insert("", "end", values=row)
    # Add the Treeview widget to the new window
    customers_list.pack()
def search_customer():
    # Create a new window for the search dialog
    search_customer_window = tk.Toplevel(root)
    search_customer_window.title("Search Customers")
    search_customer_window.configure(bg="#FFCAD4")

    # Create the widgets for the search dialog
    name_label = Label(search_customer_window, text="Name:", bg="#FFCAD4", fg="black")
    name_entry = Entry(search_customer_window)
    name_label.grid(row=0, column=0, padx=10, pady=10)
    name_entry.grid(row=0, column=1, padx=10, pady=10)

    customer_id_label = Label(search_customer_window, text="ID:", bg="#FFCAD4", fg="black")
    customer_id_entry = Entry(search_customer_window)
    customer_id_label.grid(row=1, column=0, padx=10, pady=10)
    customer_id_entry.grid(row=1, column=1, padx=10, pady=10)

    # Define a style for the search button
    search_button = Button(search_customer_window, text="Search", command=lambda: perform_search_customer(name_entry.get(), customer_id_entry.get()), borderwidth=3, bg="#F4ACB7", fg="white", font=("VNI-Vari", 12, "bold"))
    search_button.grid(row=3, column=1,columnspan=2, pady=10)
    
    def cancel_add():
        search_customer_window.destroy()
    cancel_button = Button(search_customer_window, text="Cancel", command=cancel_add,borderwidth=3, bg="#D00050", fg="white", font=("VNI-Vari", 12, "bold"))
    cancel_button.grid(row=3, column=0,columnspan=1, padx=50, pady=10)
    def search_table(self):
                search_customer_window.destroy()
                # Create a new window to display search results
                results_window = tk.Toplevel(root)
                results_window.title("Search Results")

                custom_style = ttk.Style()
                custom_style.configure("Custom.Treeview", background="#FFCAD4", foreground="#00171F")
                custom_style.map("Custom.Treeview", background=[("selected", "#9D8189")], foreground=[("selected", "black")])

                results_list = ttk.Treeview(results_window, style="Custom.Treeview", columns=("id", "name", "phonenum", "phonebrandsold", "phonemodelsold"))
                results_list.heading("id", text="Customer ID")
                results_list.heading("name", text="Customer Name")
                results_list.heading("phonenum", text="Phone Number")
                results_list.heading("phonebrandsold", text="Phone Brand Sold")
                results_list.heading("phonemodelsold", text="Phone Model Sold")
                for result in self:
                    results_list.insert("", "end", values=result)
                results_list.pack(padx=5, pady=5)
    def perform_search_customer(name, customer_id):
        # Perform the search with the given name and customer_id
        if not customer_id and name:
            search_results = list(c.execute("SELECT * FROM customers WHERE name=?", (name,)))
            if search_results:
                search_table(search_results)
            else:
                messagebox.showerror("Search Results", f"No results found for {name}.")
        elif not name and customer_id:
            search_results = list(c.execute("SELECT * FROM customers WHERE id=?", (customer_id,)))
            if search_results:
                search_table(search_results)
            else:
                messagebox.showerror("Search Results", f"No results found for ID {customer_id}.")
        elif name and customer_id:
            if name.isdigit():
                return messagebox.showerror("Error", "Customer name can't have number.")
            search_results = list(c.execute("SELECT * FROM customers WHERE name=? AND id=?", (name,customer_id)))
            if search_results:
                search_table(search_results)
            else:
                messagebox.showerror("Search Result", f"No results found for {name} with id {customer_id}")
        else:
            messagebox.showerror("Error","Please enter Name or ID to search.")

def open_add_phone_window():
    add_phone_window = tk.Toplevel(root)
    add_phone_window.title("Add Phone")
    add_phone_window.configure(bg="#FFCAD4")

    model_label = Label(add_phone_window, text="Model:", bg="#FFCAD4", fg="black")
    model_entry = Entry(add_phone_window)
    model_label.grid(row=0, column=0, padx=10, pady=10)
    model_entry.grid(row=0, column=1, padx=10, pady=10)

    brand_label = Label(add_phone_window, text="Brand:", bg="#FFCAD4", fg="black")
    brand_entry = Entry(add_phone_window)
    brand_label.grid(row=1, column=0, padx=10, pady=10)
    brand_entry.grid(row=1, column=1, padx=10, pady=10)

    price_label = Label(add_phone_window, text="Price:", bg="#FFCAD4", fg="black")
    price_entry = Entry(add_phone_window)
    price_label.grid(row=2, column=0, padx=10, pady=10)
    price_entry.grid(row=2, column=1, padx=10, pady=10)

    stock_label = Label(add_phone_window, text="Stock:", bg="#FFCAD4", fg="black")
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
        add_phone_window.destroy()
    

    add_button = Button(add_phone_window, text="Add", command=add_phone,borderwidth=3, bg="#F4ACB7", fg="white", font=("VNI-Vari", 12, "bold"))
    add_button.grid(row=4, column=1,columnspan=2, pady=10)
    
    def cancel_add():
        add_phone_window.destroy()
    cancel_button = Button(add_phone_window, text="Cancel", command=cancel_add,borderwidth=3, bg="#D00050", fg="white", font=("VNI-Vari", 12, "bold"))
    cancel_button.grid(row=4, column=0,columnspan=1, padx=50, pady=10)
    

# Add the validation functions to the input fields


def list_phones():
    # Create a new window for the table
    table_window = tk.Toplevel(root)
    table_window.title("Phone Store Inventory")

    # Define a custom style for the Treeview widget
    custom_style = ttk.Style()
    custom_style.configure("Custom.Treeview", background="#FFCAD4", foreground="#00171F")
    custom_style.map("Custom.Treeview", background=[("selected", "#9D8189")], foreground=[("selected", "black")])

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
    phones_list.tag_configure("low_stock", background="#D00050")

    # Add the Treeview widget to the new window
    phones_list.pack()

def search_phone():
    # Create a new window for the search dialog
    search_window = tk.Toplevel(root)
    search_window.title("Search Phones")
    search_window.configure(bg="#FFCAD4")

    # Create the widgets for the search dialog
    model_label = Label(search_window, text="Model:", bg="#FFCAD4", fg="black")
    model_entry = Entry(search_window)
    model_label.grid(row=0, column=0, padx=10, pady=10)
    model_entry.grid(row=0, column=1, padx=10, pady=10)
    
    brand_label = Label(search_window, text="Brand:", bg="#FFCAD4", fg="black")
    brand_entry = Entry(search_window)
    brand_label.grid(row=1, column=0, padx=10, pady=10)
    brand_entry.grid(row=1, column=1, padx=10, pady=10)

    # Define a style for the search button
    search_button = Button(search_window, text="Search", command=lambda: perform_search(model_entry.get(), brand_entry.get()), borderwidth=3, bg="#F4ACB7", fg="white", font=("VNI-Vari", 12, "bold"))
    search_button.grid(row=3, column=1,columnspan=2, pady=10)
    
    def cancel_add():
        search_window.destroy()
    cancel_button = Button(search_window, text="Cancel", command=cancel_add,borderwidth=3, bg="#D00050", fg="white", font=("VNI-Vari", 12, "bold"))
    cancel_button.grid(row=3, column=0,columnspan=1, padx=50, pady=10)
    def search_table(self):
        # Create a new window to display search results
        search_window.destroy()
        results_window = tk.Toplevel(root)
        results_window.title("Search Results")
        custom_style = ttk.Style()
        custom_style.configure("Custom.Treeview", background="#FFCAD4", foreground="#00171F")
        custom_style.map("Custom.Treeview", background=[("selected", "#9D8189")], foreground=[("selected", "black")])
        # Create the list of phones widget
        search_list = ttk.Treeview(results_window,style="Custom.Treeview", columns=("model", "brand", "price", "stock"))
        search_list.heading("model", text="Model")
        search_list.heading("brand", text="Brand")
        search_list.heading("price", text="Price")
        search_list.heading("stock", text="Stock")
        
        # Configure the style for the tags
        search_list.tag_configure("low_stock", background="#D00050")

        # Add the search results to the list of phones widget
        for result in self:
            if result[3] < 20:
                # Add a tag to the row if stock is low
                search_list.insert("", "end", values=result, tags=("low_stock",))
            else:
                search_list.insert("", "end", values=result)
        # Add the widgets to the search results window
        search_list.pack(padx=5, pady=5)
    def perform_search(model, brand):
        if not brand and model:
            search_results = list(c.execute("SELECT * FROM phones WHERE model=?", (model,)))
            if search_results:
                search_table(search_results)
            else:
                messagebox.showerror("Search Results", f"No results found for {model}.")
        elif not model and brand:
            search_results = list(c.execute("SELECT * FROM phones WHERE brand=?", (brand,)))
            if search_results:
                search_table(search_results)
            else:
                messagebox.showerror("Search Results", f"No results found for {brand}.")
        elif model and brand:
            search_results = list(c.execute("SELECT * FROM phones WHERE model=? AND brand=?", (model, brand)))
            if search_results:
                search_table(search_results)
            else:
                messagebox.showerror("Search Results", f"No results found for {brand} {model}.")
        else:
            messagebox.showerror("Search Error", "Please enter a model or a brand to perform the search.")

def remove_phone():
    # Create a new window for the remove dialog
    remove_window = tk.Toplevel(root)
    remove_window.title("Remove Phones")
    remove_window.configure(bg="#FFCAD4")

    # Create the widgets for the remove dialog
    model_label = Label(remove_window, text="Model:", bg="#FFCAD4", fg="black")
    model_entry = Entry(remove_window)
    model_label.grid(row=0, column=0, padx=10, pady=10)
    model_entry.grid(row=0, column=1, padx=10, pady=10)

    brand_label = Label(remove_window, text="Brand:", bg="#FFCAD4", fg="black")
    brand_entry = Entry(remove_window)
    brand_label.grid(row=1, column=0, padx=10, pady=10)
    brand_entry.grid(row=1, column=1, padx=10, pady=10)

    remove_button = Button(remove_window, text="Remove", command=lambda: perform_remove(model_entry.get(), brand_entry.get()), borderwidth=3, bg="#F4ACB7", fg="white", font=("VNI-Vari", 12, "bold"))
    remove_button.grid(row=3, column=1,columnspan=2, pady=10)
    
    def cancel_add():
        remove_window.destroy()
    cancel_button = Button(remove_window, text="Cancel", command=cancel_add,borderwidth=3, bg="#D00050", fg="white", font=("VNI-Vari", 12, "bold"))
    cancel_button.grid(row=3, column=0,columnspan=1, padx=50, pady=10)
    # Create a custom style for the remove button

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

        if remove_results > 0:
            messagebox.showinfo("Success", f"Your {model} {brand} has been removed!")
        else:
            messagebox.showerror("Remove Error", f"No results found for {model} {brand}.")
def restock_phone():
    # Create a new window for the restock dialog
    restock_window = tk.Toplevel(root)
    restock_window.title("Restock Phones")
    restock_window.configure(bg="#FFCAD4") 

    # Create the widgets for the restock dialog
    model_label = Label(restock_window, text="Model:", bg="#FFCAD4", fg="black")
    model_entry = Entry(restock_window)
    model_label.grid(row=0, column=0, padx=10, pady=10)
    model_entry.grid(row=0, column=1, padx=10, pady=10)

    brand_label = Label(restock_window, text="Brand:", bg="#FFCAD4", fg="black")
    brand_entry = Entry(restock_window)
    brand_label.grid(row=1, column=0, padx=10, pady=10)
    brand_entry.grid(row=1, column=1, padx=10, pady=10)
    
    quantity_label = Label(restock_window, text="Quantity:", bg="#FFCAD4", fg="black")
    quantity_entry = Entry(restock_window)
    quantity_label.grid(row=2, column=0, padx=10, pady=10)
    quantity_entry.grid(row=2, column=1, padx=10, pady=10)
    
    restock_button = Button(restock_window, text="Restock", command=lambda: perform_restock(model_entry.get(), brand_entry.get(),quantity_entry.get()), borderwidth=3, bg="#F4ACB7", fg="white", font=("VNI-Vari", 12, "bold"))
    restock_button.grid(row=3, column=1,columnspan=1, pady=10)
    
    def cancel_add():
        restock_window.destroy()
    cancel_button = Button(restock_window, text="Cancel", command=cancel_add,borderwidth=3, bg="#D00050", fg="white", font=("VNI-Vari", 12, "bold"))
    cancel_button.grid(row=3, column=0,columnspan=1, padx=50, pady=10)

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
        messagebox.showinfo("Success", f"You restocked {quantity} {brand} {model}!")
        
        # Close the restock window
        restock_window.destroy()
        
def exit_program():
    root.destroy()



# Create the main window
root.geometry("1440x826")
root.config(background="#FFCAD4")
root.grid_columnconfigure((0,1), weight=1)
# image1 = Image.open("E:\github\Kiwie\python-project\domains\MobilePhone\Phone.png")
# image1 = image1.resize((1440,826))
# # test = ImageTk.PhotoImage(image1)
# label1 = tk.Label(image=test)
# label1.image = test
# label1.place(x=0,y=0)

add_phone_button = Button(root, text="Add Phone", command=open_add_phone_window, bg="#9D8189", borderwidth=3, fg="white", font=("VNI-Vari", 12, "bold"))
add_phone_button.grid(row=4, column=0, pady=10)
remove_button = Button(root, text="Remove Phone", command=remove_phone, bg="#9D8189", borderwidth=3, fg="white", font=("VNI-Vari", 12, "bold"))
remove_button.grid(row=5, column=0, pady=10)
search_button = Button(root, text="Search Phone", command=search_phone, bg="#9D8189", borderwidth=3, fg="white", font=("VNI-Vari", 12, "bold"))
search_button.grid(row=6, column=0, pady=10)
restock_button = Button(root, text="Restock Phone", command=restock_phone, bg="#9D8189", borderwidth=3, fg="white", font=("VNI-Vari", 12, "bold"))
restock_button.grid(row=7, column=0, pady=10)
list_button = Button(root, text="List Phones", command=list_phones, bg="#9D8189", borderwidth=3, fg="white", font=("VNI-Vari", 12, "bold"))
list_button.grid(row=8, column=0, pady=10)

add_customer_button = Button(root, text="Add Customer", command=add_customer, bg="#9D8189", borderwidth=3, fg="white", font=("VNI-Vari", 12, "bold"))
add_customer_button.grid(row=4, column=1, pady=10)
remove_customer_button = Button(root, text="Remove Customer", command=remove_customer, bg="#9D8189", borderwidth=3, fg="white", font=("VNI-Vari", 12, "bold"))
remove_customer_button.grid(row=5, column=1,columnspan=1, pady=10)
search_customer_button = Button(root, text="Search Customer", command=search_customer, bg="#9D8189", borderwidth=3, fg="white", font=("VNI-Vari", 12, "bold"))
search_customer_button.grid(row=6, column=1, pady=10)
edit_customer_button = Button(root, text="Edit Customer", command=edit_customer, bg="#9D8189", borderwidth=3, fg="white", font=("VNI-Vari", 12, "bold"))
edit_customer_button.grid(row=7, column=1, pady=10)
list_customer_button = Button(root, text="List Customers", command=list_customer, bg="#9D8189", borderwidth=3, fg="white", font=("VNI-Vari", 12, "bold"))
list_customer_button.grid(row=8, column=1, pady=10)
exit_button = Button(root, text="Exit Program", command=exit_program, bg="#D00050", fg="white", borderwidth=3, font=("VNI-Vari", 12, "bold"))
exit_button.grid(row=10, column=0,columnspan=2, pady=10)


# Run the main loop
root.mainloop()

# Close the database connection when the program is done
conn.close()