import sys
sys.path.append('..')
from Domains import Product, Customer
from .Compress import *
import pickle
import os

class ShopController:
    """Mobile phone shop controler system"""

    def __init__(self):
        self.no_product = 0
        self.no_customer = 0

        self.products = []
        self.customers = []

        self.loadData()
      
    def loadData(self):
        """Load data into the system
        
        Try to load data about products, customers 
        else input the data
        """
        try:
            # Check if the data file exist
            if os.path.exists("./data/products.dat"):
                # File exist, decompressing the file, the output will be stored in ./data/ folder
                decompress("./data/products.dat")
                try:
                    # Open products file
                    with open("./data/products.txt", "rb") as products_file:
                        self.products = pickle.load(products_file)
                except Exception:
                    # Init products list to empty if products file does not exist
                    self.products = []

                try:
                    # Open customers file
                    with open("./data/customers.txt", "rb") as customers_file:
                        self.courses = pickle.load(customers_file)
                except Exception:
                    # Init customers list to empty if no courses file does not exist
                    self.customers = []

            else:
                raise FileNotFoundError()
        except FileNotFoundError:
            self.products = []
            self.customers = []

    def addProduct(self, product_info):
        """Add a product to the system
        
        product_info : {id: str, name: str, branch: str, price: float, amount: int}
        """
        if self.checkUniqueProduct(product_info["id"]):
            product = Product()
            product.takeProductInfo(product_info)
            self.products.append(product)
        else:
            raise Exception("ID already exist")
        
    def removeProduct(self, id):
        """Remove product with product id"""
        delete_index = None
        for index, product in enumerate(self.products):
            if product.p_id == id:
                delete_index = index
                break

        if delete_index != None:
            self.products.pop(delete_index)

    def checkUniqueProduct(self, id):
        """Check if a product is unique base on it's id"""
        for product in self.products:
            if product.p_id == id:
                return 0
        return 1

    def saveProducts(self):
        try:
            writeWithThread(self.products, "./data/products.txt")
            return 1
        except Exception as e:
            print(e)
            return 0

    def addCustomer(self, customer_info):
        """Add customer to the system

        customer_info : {id: str, name: str, dob: str, phone_number: str, email: str}
        """
        if self.checkUniqueCustomer(customer_info["id"]):
            customer = Customer()
            customer.takeCustomerInfo(customer_info)
            self.customers.append(customer)
    
    def removeCustomer(self, id):
        """Remove customer with customer id"""
        delete_index = None
        for index, customer in enumerate(self.customers):
            if customer.c_id == id:
                delete_index = index
                break

        if delete_index != None:
            self.customers.pop(delete_index)

    def checkUniqueCustomer(self, id):
        """Check if a customer is unique base on their id"""
        for customer in self.courses:
            if customer.c_id == id:
                return 0
        return 1

    def saveCustomers(self):
        try:
            writeWithThread(self.customers, "./data/customers.txt")
            return 1
        except Exception as e:
            print(e)
            return 0

    def getProductsList(self):
        products_data = []
        for product in self.products:
            products_data.append((product.p_id, product.p_name, product.p_branch, product.p_price, product.p_amount))
        return products_data

    def getCustomersList(self):
        customers_data = []
        for customer in self.customers:
            customers_data.append((customer.c_id, customer.c_name, customer.c_dob, customer.c_phone_number, customer.c_email))
        return customers_data

    
    def customerExist(self, id):
        """Check if the customer exist base on id
        
        Return 1 if exist, 0 if not
        """
        # Loop through the customers to check if the id exists 
        for customer in self.customers:
            if customer.c_id == id:
                return 1
        
        return 0
    
    def quit(self):
        data_files = ["./data/products.txt", "./data/customers.txt"]
        compress(data_files, "./data/products.dat")
        for file in data_files:
            os.remove(file)
        print("Exited")