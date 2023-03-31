from datetime import datetime

class Product:
    def __init__(self, name: str, type: str, amount: int, status: str, price: float) -> None:
        self.__p_name = name
        self.__p_type = type
        self.__p_price = price
        self.__p_amount = amount
        self.__p_status = status
        self.now = datetime.now()
    
    @property  
    def getPname(self) -> str:
        return self.__p_name
    @getPname.setter
    def setPname(self, name: str):
        self.__p_name = name
        
    @property
    def getPtype(self) -> str:
        return self.__p_type
    @getPtype.setter
    def setPtype(self, type: str):
        self.__p_type = type
        
        
    @property  
    def getPamount(self) -> int:
        return self.__p_amount
    @getPamount.setter
    def setPamount(self, amount: int):
        self.__p_amount = amount
        
    @property  
    def getPstatus(self) -> str:
        return self.__p_status
    @getPstatus.setter
    def setPstatus(self, status: str):
        self.__p_status = status
    
    @property
    def getPprice(self) -> float:
        return self.__p_price
    @getPprice.setter
    def setPprice(self, price: float):
        self.__p_price = price
        
    # def displayProduct(self):
    #     print("| {:^15} | {:^15} | {:^15} | {:^5}".format("Name", "Type", "Price", "Date and Time"))
    #     print("| {:^15} | {:^15} | {:^15} | {:^5}".format(self.__p_name, self.__p_type, self.__p_price, self.now.strftime("%d/%m/%Y %H:%M:%S")))
    
    def __str__(self):
        return f"Product: {self.__p_name} | {self.__p_type} | {self.__p_amount} | {self.__p_status} | {self.__p_price}" 
    
    def writeDataToFile(self, file):
        need_data = f"{self.__p_name}, {self.__p_type}, {self.__p_amount}, {self.__p_status}, {self.__p_price}"
        file.write(need_data)

    