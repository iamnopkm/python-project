from datetime import datetime

class Product:
    def __init__(self) -> None:
        self.p_id: str = ""
        self.p_name: str = ""
        self.p_branch: str = ""
        self.p_price: float = 0
        self.p_amount: int = 0
        self.now = datetime.now()
    
    def takeProductInfo(self, info = {}):
        self.p_id = info["id"]
        self.p_name = info["name"]
        self.p_branch = info["branch"]
        self.p_price = info["price"]
        self.p_amount = info["amount"]
        return self.p_id
    
    def __str__(self):
        return f"Product: {self.p_id} | {self.p_name} | {self.p_branch} | {self.p_price} | {self.p_amount} |" 
    
    def writeDataToFile(self, file):
        need_data = f"{self.p_id}, {self.p_name}, {self.p_branch}, {self.p_price}, {self.p_amount} |"
        file.write(need_data)

    