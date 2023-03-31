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
        
    def takeData(self, data):
        self.__c_name = data["Name"]
        self.__c_dob = data["Dob"]
        self.__c_phone_number = data["Phone number"]
        self.__c_email = data["Email"]
   
    # def displayProduct(self):
    #     print("| {:^15} | {:^15} | {:^15} | {:^15} | {:^5}".format("Name", "DoB", "Phone number", "Email", "Date and Time"))
    #     print("| {:^15} | {:^15} | {:^15} | {:^15} | {:^5}".format(self.__c_name, self.__c_dob, self.__c_phone_number, self.__c_email, self.now.strftime("%d/%m/%Y %H:%M:%S")))
   
    def __str__(self):
        return f"Customer: {self.__c_name} | {self.__c_dob} | {self.__c_phone_number} | {self.__c_email}" 
    
    def writeDataToFile(self, file):
        need_data = f"{self.__c_name}, {self.__c_dob}, {self.__c_phone_number}, {self.__c_email}"
        file.write(need_data)
