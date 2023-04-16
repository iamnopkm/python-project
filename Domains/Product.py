class Product:
    def __init__(self):
        self.model = ""
        self.brand = ""
        self.price = ""
        self.stock = 0
    
    def takeProductInfo(self, info = {}):
        self.model = info["model"]
        self.brand = info["brand"]
        self.price = info["price"]
        self.stock = info["stock"]
    
    def __str__(self):
        return f"Product: {self.model} | {self.brand} | {self.price} | {self.stock} |" 
    