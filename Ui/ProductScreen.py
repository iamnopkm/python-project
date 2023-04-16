from Gui import Screen, Label, Frame, Button, BasicColors
from tkinter import PhotoImage, ttk, Toplevel, Entry, messagebox

class ProductScreen(Screen):
    def __init__(self, master, shopController):
        """Init screen"""
        super().__init__(master, BasicColors.PEACH)

        self.logo_image = PhotoImage(file="./Image/mobile_store.png")
        self.image_label = Label(self, image=self.logo_image, background=BasicColors.PEACH)
        self.image_label.pack()
        self.app_name = Label(self, "Product", background=BasicColors.PEACH)
        self.app_name.pack()
        self.shopController = shopController
        self.createProductTable()
        
    def createProductTable(self):
        """Create the product table view"""
        self.product_table_frame = Frame(self, width=800, height=200, background=BasicColors.PEACH)
        self.product_table_frame.pack()
        self.product_table_frame.pack_propagate(False)
        self.product_table = ttk.Treeview(self.product_table_frame)
        self.product_table["columns"] = ("id", "name", "branch", "price", "amount")
        self.product_table.column("#0", width=0, stretch=False)
        self.product_table.column("id", width=80)
        self.product_table.column("name", width=200)
        self.product_table.column("branch", width=200)
        self.product_table.column("price", width=200)
        self.product_table.column("amount", width=80)
        
        # Create headings
        self.product_table.heading("#0", text="")
        self.product_table.heading("id", text="ID", anchor="w")
        self.product_table.heading("name", text="Name", anchor="w")
        self.product_table.heading("branch", text="Branch", anchor="w")
        self.product_table.heading("price", text="Price", anchor="w")
        self.product_table.heading("amount", text="Amount", anchor="w")
        self.product_table.pack(fill="x", expand=True)

        self.latest_id = 0
        self.getList()
        
        self.add_button = Button(self,
            self.addProductPopup,
            "Add", 
            width=10,
            height=2,
            background="teal",
            foreground="navy",
            activebackground="black",
            activeforeground="white",
            padx=10,
            pady=10
        )
        self.remove_button = Button(self,
            self.deleteProduct,
            "Remove", 
            width=10,
            height=2,
            background="teal",
            foreground="navy",
            activebackground="black",
            activeforeground="white",
            padx=10,
            pady=10
        )
        self.save_button = Button(self,
            self.save,
            "Save", 
            width=10,
            height=2,
            background="teal",
            foreground="navy",
            activebackground="black",
            activeforeground="white",
            padx=10,
            pady=10
        )
        self.add_button.pack()
        self.remove_button.pack(pady=5)
        self.save_button.pack()

    def save(self):
        self.shopController.saveProducts()

    def deleteProduct(self):
        product_id_to_delete = self.product_table.selection()
        for product_id in product_id_to_delete:
            self.shopController.removeProduct(self.product_table.item(product_id)["values"][0])
        self.getList()

    def clearAll(self):
        self.latest_id = 0
        for s in self.product_table.get_children():
            self.product_table.delete(s)

    def getList(self):
        self.clearAll()
        for product in self.shopController.getProductsList():
            self.product_table.insert(parent="", index="end", iid=self.latest_id, text="", values=product)
            self.latest_id += 1
        
    def addProductPopup(self):
        self.add_product_window = Toplevel()
        self.add_product_window.title("Add a product")
        self.add_product_window.geometry("500x300")
        self.add_product_window.resizable(False, False)
        self.add_product_window.grab_set()
        
        self.add_product_window.grid_columnconfigure(0, weight=1)
        self.add_product_window.grid_columnconfigure(1, weight=4)
        self.add_product_window.grid_rowconfigure(0, weight=1)
        self.add_product_window.grid_rowconfigure(1, weight=1)
        self.add_product_window.grid_rowconfigure(2, weight=1)
        self.add_product_window.grid_rowconfigure(3, weight=1)
        self.add_product_window.grid_rowconfigure(4, weight=1)
        self.add_product_window.grid_rowconfigure(5, weight=1)
        self.add_product_window.grid_rowconfigure(6, weight=1)
        
        id_label = Label(self.add_product_window, "ID:", background=BasicColors.WHITE)
        name_label = Label(self.add_product_window, "Name:", background=BasicColors.WHITE)
        branch_label = Label(self.add_product_window, "Branch:", background=BasicColors.WHITE)
        price_label = Label(self.add_product_window, "Price:", background=BasicColors.WHITE)
        amount_label = Label(self.add_product_window, "Amount:", background=BasicColors.WHITE)

        id_label.grid(row=0, column=0, sticky="nsw")
        name_label.grid(row=1, column=0, sticky="nsw")
        branch_label.grid(row=2, column=0, sticky="nsw")
        price_label.grid(row=3, column=0, sticky="nsw")
        amount_label.grid(row=4, column=0, sticky="nsw")

        id_entry = Entry(self.add_product_window)
        name_entry = Entry(self.add_product_window)
        branch_entry = Entry(self.add_product_window)
        price_entry = Entry(self.add_product_window)
        amount_entry = Entry(self.add_product_window)
        
        
        id_entry.grid(row=0, column=1, sticky="nsew")
        name_entry.grid(row=1, column=1, sticky="nsew")
        branch_entry.grid(row=2, column=1, sticky="nsew")
        price_entry.grid(row=3, column=1, sticky="nsew")
        amount_entry.grid(row=4, column=1, sticky="nsew")

        def saveProduct():
            product_data = {
                "id": id_entry.get(),
                "name": name_entry.get(),
                "branch": branch_entry.get(),
                "price": float(price_entry.get()),
                "amount": int(amount_entry.get())
            }
            try:
                self.shopController.addProduct(product_data)
                self.add_product_window.destroy()
                self.getList()
            except Exception as e:
                messagebox.showerror("Failed to add product", str(e))

        save_button = Button(self.add_product_window,
            saveProduct,
            "SAVE", 
            background="black",
            foreground="white",
            activebackground="black",
            activeforeground="white"                 
        )
        cancel_button = Button(self.add_product_window,
            lambda: self.add_product_window.destroy(),
            "cancel", 
            background="black",
            foreground="white",
            activebackground="black",
            activeforeground="white"                 
        )

        save_button.grid(row=5, column=0, columnspan=2, sticky="nsew", pady=5)
        cancel_button.grid(row=6, column=0, columnspan=2, sticky="nsew")
