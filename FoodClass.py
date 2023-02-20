# Author:     Shepard Berry
# Class:      MIS-4322
# Assignment: Classes and OOP
# Due:        2/20/2023

class Customer:
    def __init__(self, customerid=0, name="", address="", email="", phone="", member_status=False):
        self.customerid = customerid
        self.name = name
        self.address = address
        self.email = email
        self.phone = phone
        self.member_status = member_status

    def get_customerid(self):
        return self.customerid
    
    def get_name(self):
        return self.name
    
    def get_address(self):
        return self.address
    
    def get_email(self):
        return self.email
    
    def get_phone(self):
        return self.phone
    
    def get_member_status(self):
        return self.member_status

class Transaction:
    def __init__(self, date="", item_name="", cost=0.0, customerid=0):
        self.date = date
        self.item_name = item_name
        self.cost = cost
        self.customerid = customerid

    def get_date(self):
        return self.date
    
    def get_item_name(self):
        return self.item_name
    
    def get_cost(self):
        return self.cost
    
    def get_customerid(self):
        return self.customerid