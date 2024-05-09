from entity.Customers import Customers
from dao.TechShopMethods import TechShopMethods

class TechShop:
    @staticmethod
    def main():
        while True:
            print('\nMENU')
            print('-----------------')
            print('1. Register a new Customer')
            print('2. Manage Product Catalogue')
            print('3. Place, View or Cancel Orders')
            print('4. Track and Edit Orders')
            print('5. Manage Inventory')
            print('6. View Sales Report')
            print('7. Update Customer Details')
            print('8. Search or Recommend a Product')
            print('9. Exit')

            choice = int(input('Enter your choice: '))

            if choice == 1:
                TechShop.customer_registration()
            elif choice == 2:
                TechShop.product_catalog_management()
            elif choice == 3:
                TechShop.order_action()
            elif choice == 4:
                TechShop.track_and_edit_orders()
            elif choice == 5:
                TechShop.inventory_management()
            elif choice == 6:
                TechShop.sales_report()
            elif choice == 7:
                TechShop.update_customer_details()
            elif choice == 8:
                TechShop.search_or_recommend_a_product()
            elif choice == 9:
                print('Exiting...')
                break
            else:
                print('Incorrect choice, please try again\n')

    @staticmethod
    def customer_registration():
        # Taking customer details
        first_name = input('Enter your first name: ')
        last_name = input('Enter your last name: ')
        email = input('Enter your email: ')
        phone = input('Enter your phone number: ')
        address = input('Enter your address: ')

        customer = Customers("", first_name, last_name, email, phone, address)
        TechShopMethods().customerRegistration(customer)

    @staticmethod
    def product_catalog_management():
        while True:
            print('\n1. Update Product Details')
            print('2. Show All Products')
            print('3. Search for product in stock')
            print('4. Exit')
            choice = int(input('Enter your choice: '))
            if choice == 4:
                print('Redirecting to Main Menu...\n')
                break
            else:
                TechShopMethods().productCatalog(choice)

    @staticmethod
    def order_action():
        customer_id = int(input('Enter Customer ID: '))
        while True:
            print('\n1. Create Order')
            print('2. Get Order Details')
            print('3. Cancel Order')
            print('4. Exit')
            choice = int(input('Enter your choice: '))
            if choice == 4:
                print('Redirecting to Main Menu...\n')
                break
            else:
                TechShopMethods().manageOrders(customer_id, choice)

    @staticmethod
    def track_and_edit_orders():
        order_id = int(input('Enter order id: '))
        while True:
            print('\n1. Display order status')
            print('2. Change Order Status')
            print('3. Update Order Quantity')
            print('4. Apply Discount on Order')
            print('5. Exit')
            choice = int(input('Enter your choice: '))
            if choice == 5:
                print('Redirecting to Main Menu...\n')
                break
            else:
                TechShopMethods().trackOrder(order_id, choice)

    @staticmethod
    def inventory_management():
        while True:
            print("\n1. Add New Product")
            print("2. Update/Add Product Stock")
            print("3. Remove Product that is being discontinued")
            print("4. Show products low in stock")
            print("5. Show out of stock products")
            print("6. Remove units of a product from stock")
            print("7. Exit")
            choice = int(input("Enter your choice: "))
            if choice == 7:
                print('Redirecting to Main Menu...')
                break
            else:
                TechShopMethods().inventoryManagement(choice)

    @staticmethod
    def sales_report():
        while True:
            print('1. Generate Sales Report')
            print('2. Exit')
            choice = int(input('Enter your choice: '))
            if choice == 2:
                print('Redirecting to Main Menu...')
                break
            else:
                TechShopMethods().salesReport(choice)

    @staticmethod
    def update_customer_details():
        customer_id = int(input('Enter customer id: '))
        while True:
            print("\n1. Update Customer Details")
            print("2. Get Customer Details")
            print("3. Exit")
            choice = int(input("Enter your choice: "))
            if choice == 3:
                print('Redirecting to Main Menu...')
                break
            else:
                TechShopMethods().updateCustomer(customer_id, choice)

    @staticmethod
    def search_or_recommend_a_product():
        while True:
            print('\n1. Search Product')
            print('2. Recommend Products')
            print('3. Exit')
            choice = int(input('Enter your choice: '))
            if choice == 3:
                print('Redirecting to Main Menu...')
                break
            else:
                TechShopMethods().productSearchandRecommend(choice)


if __name__ == '__main__':
    TechShop.main()
