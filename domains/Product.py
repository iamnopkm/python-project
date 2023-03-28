import mysql.connector
from datetime import datetime

class Product:
    def __init__(self, name: str, type: str, price: float) -> None:
        self.__p_name = name
        self.__p_type = type
        self.__p_price = price
        self.now = datetime.now()
    
    #need amount and status of product
    
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
    def getPprice(self) -> float:
        return self.__p_price
    @getPprice.setter
    def setPprice(self, price: float):
        self.__p_price = price
        
    def displayProduct(self):
        print("| {:^15} | {:^15} | {:^15} | {:^5}".format("Name", "Type", "Price", "Time"))
        print("| {:^15} | {:^15} | {:^15} | {:^5}".format(self.__p_name, self.__p_type, self.__p_price, self.now.strftime("%d/%m/%Y %H:%M:%S")))
    
    
    
john = Product("Iphone 11", "Mobile Phone", 11000)
john._Product__p_name   
john.displayProduct() 
      
    