class Customer:
    def __init__(self):
        self.name = ""
        self.customer_id = ""
        self.PhoneNum = ""
        self.phone_model_information = ""
        self.phone_brand_information = ""
    
        
    def takeCustomerInfo(self, info = {}):
        self.name = info["name"]
        self.customer_id = info["id"]
        self.PhoneNum = info["phone number"]
        self.phone_model_information = info["phone model sold information"]
        self.phone_brand_information = info["phone brand sold information"]
        return self.customer_id
   
    def __str__(self):
        return f"Customer: {self.name} | {self.customer_id} | {self.PhoneNum} | {self.phone_model_information} | {self.phone_brand_information}" 