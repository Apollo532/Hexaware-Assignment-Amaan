import datetime
from entity.Customers import *

class Orders:
    def __init__(self, order_id: int, customer: Customers, order_date: datetime, tot_amount: float):
        self.__OrderID = order_id
        self.__customer = customer
        self.__OrderDate = order_date
        self.__TotalAmount = tot_amount

    def get_order_id(self) -> int:
        return self.__OrderID

    def set_order_id(self, value: int):
        self.__OrderID = value

    def get_customer(self) -> Customers:
        return self.__customer

    def set_customer(self, value: Customers):
        self.__customer = value

    def get_order_date(self) -> datetime:
        return self.__OrderDate

    def set_order_date(self, value: datetime):
        self.__OrderDate = value

    def get_total_amount(self):
        return self.__TotalAmount

    def set_total_amount(self, value: float):
        if value > 0:
            self.__TotalAmount = value


'''
    def calculateTotalAmount(self):
        pass

    def getOrderDetails(self):
        pass

    def updateOrderStatus(self):
        pass

    def cancelOrder(self):
        pass
'''