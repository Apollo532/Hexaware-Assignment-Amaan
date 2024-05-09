from abc import ABC, abstractmethod


class ITechShopMethods(ABC):
    @abstractmethod
    def customerRegistration(self, customer):
        pass

    @abstractmethod
    def productCatalog(self, choice):
        pass

    @abstractmethod
    def manageOrders(self, customer, choice):
        pass

    @abstractmethod
    def trackOrder(self, order, choice):
        pass

    @abstractmethod
    def inventoryManagement(self, choice):
        pass

    @abstractmethod
    def salesReport(self, choice):
        pass

    @abstractmethod
    def updateCustomer(self, customer, choice):
        pass

    @abstractmethod
    def productSearchandRecommend(self, choice):
        pass