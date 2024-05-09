class Products:
    def __init__(self, product_id: int, product_name: str, desc: str, price: float):
        self.__ProductID = product_id
        self.__ProductName = product_name
        self.__Description = desc
        self.__Price = price

    def get_product_id(self):
        return self.__product_id

    def set_product_id(self, value: int):
        self.__product_id = value

    def get_product_name(self):
        return self.__product_name

    def set_product_name(self, value: str):
        self.__product_name = value

    def get_description(self):
        return self.__description

    def set_description(self, value: str):
        self.__description = value

    def get_price(self):
        return self.__price

    def set_price(self, value: float):
        if value > 0:
            self.__price = value

'''
    def getProductDetails(self):
        pass

    def updateProductInfo(self):
        pass

    def isProductInStock(self):
        pass
'''