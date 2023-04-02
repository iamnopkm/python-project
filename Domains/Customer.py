from datetime import datetime

class Customer:
    def __init__(self) -> None:
        self.c_id: str = ""
        self.c_name: str = ""
        self.c_dob: str = ""
        self.c_phone_number: str = ""
        self.c_email: str = ""
        self.now = datetime.now()
    
        
    def takeCustomerInfo(self, info):
        self.c_id = info["id"]
        self.c_name = info["name"]
        self.c_dob = info["dob"]
        self.c_phone_number = info["phone_number"]
        self.c_email = info["email"]
   
    def __str__(self):
        return f"Customer: {self.c_id} | {self.c_name} | {self.c_dob} | {self.c_phone_number} | {self.c_email}" 
    
    def writeDataToFile(self, file):
        need_data = f"{self.c_id}, {self.c_name}, {self.c_dob}, {self.c_phone_number}, {self.c_email}"
        file.write(need_data)
