class InvalidDataException(Exception):
    def __init__(self, message="Invalid Data Entered"):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return self.message


class InsufficientStockException(Exception):
    def __init__(self, message='Insufficient Stock'):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return self.message


class ProductNotFoundException(Exception):
    def __init__(self, message="Product Not Found"):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return self.message


class IncompleteOrderException(Exception):
    def __init__(self, message="Incomplete details provided fro order. Check and Try again"):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return self.message