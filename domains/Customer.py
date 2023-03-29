import mysql.connector
from datetime import datetime

class Customer:
    def __init__(self, name: str, dob: str, phone_number: str, email: str) -> None:
        self.__c_name = name
        self.__c_dob = dob
        self.__c_phone_number = phone_number
        self.__c_email = email
        self.now = datetime.now()
    
    
    @property  
    def getCname(self) -> str:
        return self.__C_name
    @getCname.setter
    def setCname(self, name: str):
        self.__c_name = name
        
    @property
    def getCdob(self) -> str:
        return self.__c_dob
    @getCdob.setter
    def setCdob(self, dob: str):
        self.__c_dob = dob
        
        
    @property  
    def getCphonenumber(self) -> int:
        return self.__c_phone_number
    @getCphonenumber.setter
    def setCphonenumber(self, phone_number: str):
        self.__c_phone_number = phone_number
        
    @property  
    def getCemail(self) -> str:
        return self.__c_email
    @getCemail.setter
    def setCemail(self, email: str):
        self.__c_email = email
        
    def displayProduct(self):
        print("| {:^15} | {:^15} | {:^15} | {:^15} | {:^5}".format("Name", "DoB", "Phone number", "Email", "Date and Time"))
        print("| {:^15} | {:^15} | {:^15} | {:^15} | {:^5}".format(self.__c_name, self.__c_dob, self.__c_phone_number, self.__c_email, self.now.strftime("%d/%m/%Y %H:%M:%S")))
    

# test    
john = Customer("Jhony nguye", "12-09-2003", "0998832213", "test@gmail.com")
john.displayProduct()

    