from Gui import Screen, Label, Frame, Button, BasicColors
from tkinter import PhotoImage, ttk, Toplevel, Entry, messagebox

class CustomerScreen(Screen):
    def __init__(self, master, shopController):
        """Init screen"""
        super().__init__(master, BasicColors.WHITE)

        self.logo_image = PhotoImage(file="./Image/mobile_store.png")
        self.image_label = Label(self, image=self.logo_image, background=BasicColors.WHITE)
        self.image_label.pack()
        self.app_name = Label(self, "Customer", background=BasicColors.WHITE)
        self.app_name.pack()
        self.shopController = shopController
        self.createCustomerTable()
        
    def createCustomerTable(self):
        """Create the customer table view"""
        self.customer_table_frame = Frame(self, width=1000, height=1000, background=BasicColors.WHITE)
        self.customer_table_frame.pack()
        self.customer_table_frame.pack_propagate(False)
        self.customer_table = ttk.Treeview(self.customer_table_frame)
        self.customer_table["columns"] = ("id", "name", "dob", "phone_number", "email")
        self.customer_table.column("#0", width=0, stretch=False)
        self.customer_table.column("id", width=80)
        self.customer_table.column("name", width=200)
        self.customer_table.column("dob", width=100)
        self.customer_table.column("phone_number", width=150)
        self.customer_table.column("email", width=150)

        # Create headings
        self.customer_table.heading("#0", text="")
        self.customer_table.heading("id", text="ID", anchor="w")
        self.customer_table.heading("name", text="Name", anchor="w")
        self.customer_table.heading("dob", text="DoB", anchor="w")
        self.customer_table.heading("phone_number", text="Phone_Number", anchor="w")
        self.customer_table.heading("email", text="Email", anchor="w")
        self.customer_table.pack(fill="x", expand=True)

        self.latest_id = 0
        self.getList()
        
        self.add_button = Button(self,
            self.addCustomerPopup,
            "ADD +", 
            width=10,
            height=2,
            background="black",
            foreground="white",
            activebackground="black",
            activeforeground="white"
        )
        self.remove_button = Button(self,
            self.deleteCustomer,
            "REMOVE x", 
            width=10,
            height=2,
            background="black",
            foreground="white",
            activebackground="black",
            activeforeground="white"
        )
        self.save_button = Button(self,
            self.save,
            "SAVE CHANGES", 
            width=10,
            height=2,
            background="black",
            foreground="white",
            activebackground="black",
            activeforeground="white"
        )
        self.add_button.pack()
        self.remove_button.pack(pady=5)
        self.save_button.pack()

    def save(self):
        self.shopController.saveCustomers()

    def deleteCustomer(self):
        customer_id_to_delete = self.customer_table.selection()
        for customer_id in customer_id_to_delete:
            self.shopController.removeCustomer(self.customer_table.item(customer_id)["values"][0])
        self.getList()

    def clearAll(self):
        self.latest_id = 0
        for s in self.customer_table.get_children():
            self.customer_table.delete(s)

    def getList(self):
        self.clearAll()
        for customer in self.shopController.getCustomersList():
            self.customer_table.insert(parent="", index="end", iid=self.latest_id, text="", values=customer)
            self.latest_id += 1
        
    def addCustomerPopup(self):
        self.add_customer_window = Toplevel()
        self.add_customer_window.title("Add a customer")
        self.add_customer_window.geometry("500x300")
        self.add_customer_window.resizable(False, False)
        self.add_customer_window.grab_set()
        
        self.add_customer_window.grid_columnconfigure(0, weight=1)
        self.add_customer_window.grid_columnconfigure(1, weight=4)
        self.add_customer_window.grid_rowconfigure(0, weight=1)
        self.add_customer_window.grid_rowconfigure(1, weight=1)
        self.add_customer_window.grid_rowconfigure(2, weight=1)
        self.add_customer_window.grid_rowconfigure(3, weight=1)
        self.add_customer_window.grid_rowconfigure(4, weight=1)
        self.add_customer_window.grid_rowconfigure(5, weight=1)
        self.add_customer_window.grid_rowconfigure(6, weight=1)
        
        id_label = Label(self.add_customer_window, "ID:", background=BasicColors.WHITE)
        name_label = Label(self.add_customer_window, "Name:", background=BasicColors.WHITE)
        dob_label = Label(self.add_customer_window, "Dob:", background=BasicColors.WHITE)
        phone_number_label = Label(self.add_customer_window, "Phone_Number:", background=BasicColors.WHITE)
        email_label = Label(self.add_customer_window, "Email:", background=BasicColors.WHITE)
        
        id_label.grid(row=0, column=0, sticky="nsw")
        name_label.grid(row=1, column=0, sticky="nsw")
        dob_label.grid(row=2, column=0, sticky="nsw")
        phone_number_label.grid(row=3, column=0, sticky="nsw")
        email_label.grid(row=4, column=0, sticky="nsw")

        id_entry = Entry(self.add_customer_window)
        name_entry = Entry(self.add_customer_window)
        dob_entry = Entry(self.add_customer_window)
        phone_number_entry = Entry(self.add_customer_window)
        email_entry = Entry(self.add_customer_window)
        
        id_entry.grid(row=0, column=1, sticky="nsew")
        name_entry.grid(row=1, column=1, sticky="nsew")
        dob_entry.grid(row=2, column=1, sticky="nsew")
        phone_number_entry.grid(row=3, column=1, sticky="nsew")
        email_entry.grid(row=4, column=1, sticky="nsew")

        def saveCustomer():
            try:
                customer_data = {
                    "id": id_entry.get(),
                    "name": name_entry.get(),
                    "dob": dob_entry.get(),
                    "phone_number": phone_number_entry.get(),
                    "email": email_entry.get()
                }
                self.shopController.addCustomer(customer_data)
                self.add_customer_window.destroy()
                self.getList()
            except Exception as e:
                messagebox.showerror("Failed to add customer", str(e))

        save_button = Button(self.add_customer_window,
            saveCustomer,
            "SAVE", 
            background="black",
            foreground="white",
            activebackground="black",
            activeforeground="white"                 
        )
        cancel_button = Button(self.add_customer_window,
            lambda: self.add_customer_window.destroy(),
            "cancel", 
            background="black",
            foreground="white",
            activebackground="black",
            activeforeground="white"                 
        )

        save_button.grid(row=5, column=0, columnspan=2, sticky="nsew", pady=5)
        cancel_button.grid(row=6, column=0, columnspan=2, sticky="nsew")
