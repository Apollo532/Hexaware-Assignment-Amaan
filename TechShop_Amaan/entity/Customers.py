class Customers:
    def __init__(self, customer_id: int, first_name: str, last_name: str, email: str, phone: str, address: str):
        self.__CustomerID = customer_id
        self.__FirstName = first_name
        self.__LastName = last_name
        self.__Email = email
        self.__Phone = phone
        self.__Address = address

    def get_customer_id(self):
        return self.__CustomerID

    def get_first_name(self):
        return self.__FirstName

    def get_last_name(self):
        return self.__LastName

    def get_email(self):
        return self.__Email

    def get_phone(self):
        return self.__Phone

    def get_address(self):
        return self.__Address

    def set_first_name(self, first_name):
        self.__FirstName = first_name

    def set_last_name(self, last_name):
        self.__LastName = last_name

    def set_email(self, email):
        self.__Email = email

    def set_phone(self, phone):
        self.__Phone = phone

    def set_address(self, address):
        self.__Address = address

'''
    def calculateTotalOrders(self):
        pass

    def getCustomerDetails(self):
        pass

    def updateCustomerInfo(self):
        pass
'''