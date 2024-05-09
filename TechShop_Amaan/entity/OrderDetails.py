import datetime
from entity.Products import *
from entity.Orders import *

class OrderDetails:
    def __init__(self, order_detail_id: int, order: Orders, product: Products, quantity: int):
        self.__OrderDetailID = order_detail_id
        self.__Order = order
        self.__Product = product
        self.__Quantity = quantity

    def get_order_detail_id(self):
        return self.__OrderDetailID

    def set_order_detail_id(self, value: int):
        self.__OrderDetailID = value

    def get_order(self):
        return self.__Order

    def set_order(self, value: Orders):
        self.__Order = value

    def get_product(self):
        return self.__Product

    def set_product(self, value: Products):
        self.__Product = value

    def get_quantity(self):
        return self.__Quantity

    def set_quantity(self, value: int):
        if value > 0:
            self.__Quantity = value


'''

    def calculateSubtotal(self):
        pass

    def getOrderDetailInfo(self):
        pass

    def updateQuantity(self):
        pass

    def addDiscount(self):
        pass
'''