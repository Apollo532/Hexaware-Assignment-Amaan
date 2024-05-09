from entity.Products import *
import datetime

class Inventory:
    def __init__(self, inventory_id: int, product: Products, quantity_in_stock, last_stock_update):
        self.__InventoryID = inventory_id
        self.__Product = product
        self.__QuantityInStock = quantity_in_stock
        self.__LastStockUpdate = last_stock_update

    def get_inventory_id(self):
        return self.__InventoryID

    def set_inventory_id(self, value: int):
        self.__InventoryID = value

    def get_product(self):
        return self.__Product

    def set_product(self, value: Products):
        self.__Product = value

    def get_quantity_in_stock(self):
        return self.__QuantityInStock

    def set_quantity_in_stock(self, value: int):
        if value > 0:
            self.__QuantityInStock = value

    def get_last_stock_update(self) -> datetime:
        return self.__LastStockUpdate

    def set_last_stock_update(self, value: datetime):
        self.__LastStockUpdate = value


'''
    # def GetProduct(self):
        pass

    def GetQuantityInStock(self):
        pass

    # def AddToInventory(quantity: int):
        pass

    def RemoveFromInventory(quantity: int):
        pass

    # def UpdateStockQuantity(newQuantity: int):
        pass

    # def IsProductAvailable(quantityToCheck: int):
        pass

    #def GetInventoryValue(self):
        pass

    #def ListLowStockProducts(threshold: int):
        pass

    #def ListOutOfStockProducts(self):
        pass

    # def ListAllProducts(self):
        pass '''