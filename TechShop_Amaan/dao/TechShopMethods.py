from dao.ITechShopMethods import ITechShopMethods
from util.DBConnector import DBConnector
from entity.Customers import Customers
from datetime import date
from Exceptions.CustomExceptions import *


class TechShopMethods(ITechShopMethods):

    def customerRegistration(self, customer):
        try:
            conn = DBConnector.openConnection()
            cs = conn.cursor()
            # Checking valid input of data.
            # first name and last name
            if any(char.isdigit() for char in customer.get_first_name()) or any(
                    char.isdigit() for char in customer.get_last_name()):
                raise InvalidDataException('Invalid First or Last Name')

            # phone number
            if any(char.isalpha() for char in customer.get_phone()):
                raise InvalidDataException('Invalid Phone Number')

            # email
            if '@' not in customer.get_email():
                raise InvalidDataException('Invalid Email')

            # Insert customer data into the database
            cs.execute("""INSERT INTO Customers (FirstName, LastName, Email, Phone, Address)
                           VALUES (%s, %s, %s, %s, %s)""",
                       (customer.get_first_name(), customer.get_last_name(), customer.get_email(),
                        customer.get_phone(), customer.get_address()))
            conn.commit()
            print('Customer created successfully.\n')
        except InvalidDataException as e:
            conn.rollback()
            print(e)
        finally:
            DBConnector.closeConnection(conn, cs)

    def productCatalog(self, choice):
        def checkIfProductExists(product_id):
            conn = DBConnector.openConnection()
            cs = conn.cursor()
            cs.execute("""SELECT COUNT(*) FROM Products 
                           WHERE ProductID = %s """, (product_id,))
            count = cs.fetchone()[0]
            cs.close()
            return count > 0

        def updateProductInfo():
            product_id = int(input('Enter product ID: '))
            if checkIfProductExists(product_id):
                price = float(input('Enter New Price: '))
                descr = input('Enter new description: ')
                categ = input('Enter changed Category: ')
                conn = DBConnector.openConnection()
                cs = conn.cursor()
                cs.execute(""" UPDATE Products SET Price = %s, Description = %s, Category = %s
                               WHERE ProductID = %s""",
                           (price, descr, categ, product_id))
                conn.commit()
                cs.close()
                print('Product information updated successfully')
            else:
                print('Product Not found')

        def showAllProducts():
            conn = DBConnector.openConnection()
            cs = conn.cursor()
            try:
                cs.execute("SELECT * FROM Products")
                print("Product details:")
                for row in cs.fetchall():
                    print(row)
            finally:
                DBConnector.closeConnection(conn, cs)

        def productInStock():
            product_id = int(input('Enter product ID: '))
            conn = DBConnector.openConnection()
            cs = conn.cursor()
            try:
                if checkIfProductExists(product_id):
                    cs.execute("SELECT QuantityInStock FROM Inventory WHERE ProductID = %s", (product_id,))
                    quantity = cs.fetchone()[0]
                    if quantity > 0:
                        print(f'Product in stock: {quantity}')
                    else:
                        print('Product not in stock')

                else:
                    print("Product not found")
            finally:
                DBConnector.closeConnection(conn, cs)

        if choice == 1:
            updateProductInfo()
        elif choice == 2:
            showAllProducts()
        elif choice == 3:
            productInStock()
        else:
            print('Incorrect choice, please select a valid option')

    def manageOrders(self, customer_id, choice):

        def createOrder():
            try:
                conn = DBConnector.openConnection()
                cs = conn.cursor()

                product_id = int(input('Enter product ID: '))
                quantity = int(input('Enter quantity: '))
                order_date = date.today()
                # Checking for Invalid input for product data
                if product_id == '' or quantity == '':
                    raise IncompleteOrderException("Incomplete order. Please enter all details.")

                # Checking if product exists, otherwise throwing an exception
                cs.execute("SELECT Price FROM Products WHERE ProductID = %s", (product_id,))
                row = cs.fetchone()
                if not row:
                    raise ProductNotFoundException('Product not found.')

                price = row[0]
                total_amount = price * quantity

                # Checking available stock
                cs.execute("SELECT QuantityInStock FROM Inventory WHERE ProductID = %s", (product_id,))
                current_quantity = cs.fetchone()[0]
                if current_quantity < quantity:
                    raise InsufficientStockException('Insufficient stock.')

                cs.execute("SELECT OrderID FROM Orders ORDER BY OrderID DESC LIMIT 1")
                order_id = cs.fetchone()[0] + 1

                cs.execute("SELECT OrderDetailID FROM OrderDetails ORDER BY OrderDetailID DESC LIMIT 1")
                order_detail_id = cs.fetchone()[0] + 1

                # Updating OrderDetails and Orders tables.
                cs.execute(""" INSERT INTO Orders(OrderID, CustomerId, OrderDate, TotalAmount, Status)
                               VALUES (%s, %s, %s, %s, %s)""",
                           (order_id, customer_id, order_date, total_amount, 'Pending'))

                cs.execute(""" INSERT INTO OrderDetails (OrderDetailID, OrderID, ProductID, Quantity)
                               VALUES(%s, %s, %s, %s)""", (order_detail_id, order_id, product_id, quantity))

                # Updating stock quantity
                new_quantity = current_quantity - quantity
                cs.execute(""" UPDATE Inventory SET QuantityInStock = %s WHERE ProductID = %s""",
                           (new_quantity, product_id))

                conn.commit()
                print('Order Created Successfully')

            except (ProductNotFoundException, InsufficientStockException, IncompleteOrderException) as e:
                print(e)
            except Exception as e:
                conn.rollback()
                print('Error creating Order:', e)
            finally:
                DBConnector.closeConnection(conn, cs)

        def getOrderDetails():
            try:
                conn = DBConnector.openConnection()
                cs = conn.cursor()
                cs.execute("""SELECT OD.OrderDetailID, OD.OrderID, OD.ProductID, OD.Quantity, O.OrderDate 
                               FROM OrderDetails OD
                               JOIN Orders O ON O.OrderID = OD.OrderID
                               WHERE O.CustomerID = %s""", (customer_id,))
                orders = cs.fetchall()
                print(f"You've ordered {len(orders)} times, below are those order details:")
                for order in orders:
                    print()
                    print(f"Order Detail ID: {order[0]}")
                    print(f"Order ID: {order[1]}")
                    print(f"Product ID: {order[2]}")
                    print(f"Quantity: {order[3]}")
                    print(f"Order Date: {order[4]}")
                    print()
                conn.commit()
            except Exception as e:
                conn.rollback()
                raise e
            finally:
                DBConnector.closeConnection(conn, cs)


        def cancelOrder():
            print('Here are your orders: \n')
            getOrderDetails()
            order_id = int(input('Select an order to cancel: '))
            try:
                conn = DBConnector.openConnection()
                cs = conn.cursor()

                # Get orders related to that order id
                cs.execute("SELECT ProductID, Quantity FROM OrderDetails WHERE OrderID = %s", (order_id,))
                order_details = cs.fetchall()

                # Delete the order and its details
                cs.execute("DELETE FROM OrderDetails WHERE OrderID = %s", (order_id,))
                cs.execute("DELETE FROM Orders WHERE OrderID = %s", (order_id,))
                conn.commit()
                print('Order Canceled.')

                # Restoring the stock
                for product_id, quantity in order_details:
                    cs.execute("SELECT QuantityInStock FROM Inventory WHERE ProductID = %s", (product_id,))
                    current_quantity = cs.fetchone()[0]
                    new_quantity = current_quantity + quantity
                    cs.execute("""UPDATE Inventory SET QuantityInStock = %s
                                   WHERE ProductID = %s""", (new_quantity, product_id))

                conn.commit()
                print('Stock restored successfully.')
            except Exception as e:
                conn.rollback()
                print('Error canceling order:', e)
            finally:
                DBConnector.closeConnection(conn, cs)

        if choice == 1:
            createOrder()
        elif choice == 2:
            getOrderDetails()
        elif choice == 3:
            cancelOrder()
        else:
            print('Incorrect choice, please try again.\n')

    def trackOrder(self, order_id, choice):
        def showStatus():
            try:
                conn = DBConnector.openConnection()
                cs = conn.cursor()
                cs.execute("SELECT Status FROM Orders WHERE OrderID = %s", (order_id,))
                status = cs.fetchone()[0]
                print("Your order status: ", status)
                conn.commit()
            except Exception as e:
                conn.rollback()
                raise e
            finally:
                DBConnector.closeConnection(conn, cs)

        def updateStatus():
            status = input('Enter status (Shipped/Pending): ')
            if status.lower() in ['shipped', 'pending']:
                try:
                    conn = DBConnector.openConnection()
                    cs = conn.cursor()
                    cs.execute("UPDATE Orders SET Status = %s WHERE OrderID = %s", (status, order_id))
                    print('Status Updated\n')
                    conn.commit()
                except Exception as e:
                    conn.rollback()
                    raise e
                finally:
                    DBConnector.closeConnection(conn, cs)
            else:
                print('Enter valid status. Try again')

        def updateQuantity():
            try:
                new_quantity = int(input("Enter the new quantity: "))
                conn = DBConnector.openConnection()
                cs = conn.cursor()

                # Get the previous quantity from OrderDetails
                cs.execute("SELECT ProductID, Quantity FROM OrderDetails WHERE OrderID = %s", (order_id,))
                product_id, prev_quantity = cs.fetchone()

                # Update the quantity in OrderDetails
                cs.execute("UPDATE OrderDetails SET Quantity = %s WHERE OrderID = %s", (new_quantity, order_id))

                # Update the quantity in Inventory
                cs.execute("UPDATE Inventory SET QuantityInStock = QuantityInStock + %s WHERE ProductID = %s",
                           (prev_quantity - new_quantity, product_id))

                # Update the total amount in Orders based on the new quantity and price per unit
                cs.execute("SELECT Price FROM Products WHERE ProductID = %s", (product_id,))
                price_per_unit = cs.fetchone()[0]
                new_total_amount = price_per_unit * new_quantity
                cs.execute("UPDATE Orders SET TotalAmount = %s WHERE OrderID = %s", (new_total_amount, order_id))

                conn.commit()
                print("Quantity updated successfully.")
            except Exception as e:
                conn.rollback()
                print("Error updating quantity:", e)
            finally:
                DBConnector.closeConnection(conn, cs)

        def applyDiscount():
            try:
                discount = int(input("Enter the discount amount: "))
                conn = DBConnector.openConnection()
                cs = conn.cursor()

                # Update the TotalAmount in Orders after applying discount
                cs.execute("SELECT TotalAmount FROM Orders WHERE OrderID = %s", (order_id,))
                total_amount = cs.fetchone()[0]
                new_total_amount = total_amount - discount
                cs.execute("UPDATE Orders SET TotalAmount = %s WHERE OrderID = %s", (new_total_amount, order_id))

                conn.commit()
                print("Discount applied successfully.")
            except Exception as e:
                conn.rollback()
                print("Error applying discount:", e)
            finally:
                DBConnector.closeConnection(conn, cs)

        if choice == 1:
            showStatus()
        elif choice == 2:
            updateStatus()
        elif choice == 3:
            updateQuantity()
        elif choice == 4:
            applyDiscount()
        else:
            print('Incorrect choice,please try again.\n')

    def inventoryManagement(self, choice):
        def addProduct():
            conn = DBConnector.openConnection()
            cs = conn.cursor()
            cs.execute('SELECT ProductID FROM Products ORDER BY ProductID DESC LIMIT 1')
            product_id = cs.fetchone()[0] + 1
            cs.execute('SELECT InventoryID FROM Inventory ORDER BY InventoryID DESC LIMIT 1')
            inventory_id = cs.fetchone()[0] + 1
            try:
                product_name = input('Enter product name: ')
                desc = input('Enter product description: ')
                price = float(input('Enter product price: '))
                quantity = int(input('Enter quantity in stock: '))
                category = input('Enter Product Category: ')
                last_stock_date = date.today()
                cs.execute("INSERT INTO Products VALUES (%s, %s, %s, %s, %s)",
                           (product_id, product_name, desc, price, category))
                cs.execute("INSERT INTO Inventory VALUES (%s, %s, %s, %s)",
                           (inventory_id, product_id, quantity, last_stock_date))
                conn.commit()
                print('Product Added Succesfully')
            except Exception as e:
                conn.rollback()
                raise e
            finally:
                DBConnector.closeConnection(conn, cs)

        def addToInventory():
            product_id = int(input('Enter product id: '))
            new_quantity = int(input('Enter quantity to be added: '))
            try:
                conn = DBConnector.openConnection()
                cs = conn.cursor()
                cs.execute("SELECT QuantityInStock FROM Inventory WHERE ProductID = %s", (product_id,))
                quantity_in_stock = cs.fetchone()[0]
                print('Quantity in stock: ', quantity_in_stock)
                quantity = quantity_in_stock + new_quantity
                cs.execute("UPDATE Inventory SET QuantityInStock = %s WHERE ProductID = %s", (quantity, product_id))
                print(f'Quantity updated for Product ID {product_id}, new quantity of units in stock is: {quantity}')
                conn.commit()
            except Exception as e:
                conn.rollback()
                raise e
            finally:
                DBConnector.closeConnection(conn, cs)

        def removeProduct():
            item = int(input('Enter product id you want to remove (product ID): '))
            try:
                conn = DBConnector.openConnection()
                cs = conn.cursor()
                cs.execute("DELETE FROM Inventory WHERE ProductID = %s", (item,))
                cs.execute("DELETE FROM Products WHERE ProductID = %s", (item,))
                conn.commit()
                print('Removed items successfully')
            except Exception as e:
                conn.rollback()
                raise e
            finally:
                DBConnector.closeConnection(conn, cs)

        def listLowStockProducts():
            try:
                threshold = 10
                conn = DBConnector.openConnection()
                cs = conn.cursor()
                cs.execute('''SELECT P.ProductID, P.ProductName, I.QuantityInStock
                   FROM Products AS P JOIN Inventory AS I ON P.ProductID = I.ProductID 
                   WHERE I.QuantityInStock < %s''', (threshold,))
                low_stock_products = cs.fetchall()
                if low_stock_products:
                    print("Products with below 10 units remaining:")
                    for product in low_stock_products:
                        print(f"Product ID: {product[0]}, Product Name: {product[1]}, Quantity in Stock: {product[2]}")
                else:
                    print("No products found with quantities below 10.")
            except Exception as e:
                print("Error listing low stock products:", e)
            finally:
                DBConnector.closeConnection(conn, cs)

        def listOutOfStockProducts():
            try:
                conn = DBConnector.openConnection()
                cs = conn.cursor()
                cs.execute("SELECT ProductID, ProductName FROM Products WHERE ProductID NOT IN "
                           "(SELECT ProductID FROM Inventory)")
                out_of_stock_products = cs.fetchall()
                if out_of_stock_products:
                    print("Out of Stock Products:")
                    for product in out_of_stock_products:
                        print(f"Product ID: {product[0]}, Product Name: {product[1]}")
                else:
                    print("No out of stock products found.")
            except Exception as e:
                print("Error encountered: Unable to show out of stock products:", e)
            finally:
                DBConnector.closeConnection(conn, cs)


        def removeFromInventory():
            try:
                product_id = int(input("Enter rpoduct id: "))
                quantity = int(input("Enter quantity to remove: "))
                conn = DBConnector.openConnection()
                cs = conn.cursor()
                cs.execute("SELECT QuantityInStock FROM Inventory WHERE ProductID = %s", (product_id,))
                current_quantity = cs.fetchone()[0]
                if current_quantity is not None and current_quantity >= quantity:
                    new_quantity = current_quantity - quantity
                    cs.execute("UPDATE Inventory SET QuantityInStock = %s WHERE ProductID = %s",
                               (new_quantity, product_id))
                    conn.commit()
                    print(f"Removed {quantity} units from the inventory for Product ID {product_id}.")
                else:
                    print("Failed to remove from inventory: Insufficient stock.")
            except Exception as e:
                conn.rollback()
                print("Error removing from inventory:", e)
            finally:
                DBConnector.closeConnection(conn, cs)

        if choice == 1:
            addProduct()
        elif choice == 2:
            addToInventory()
        elif choice == 3:
            removeProduct()
        elif choice == 4:
            listLowStockProducts()
        elif choice == 5:
            listOutOfStockProducts()
        elif choice == 6:
            removeFromInventory()
        else:
            print('Incorrect choice, please try again.\n')

    def salesReport(self, choice):
        try:
            conn = DBConnector.openConnection()
            cs = conn.cursor()
            query = """SELECT P.ProductID, P.ProductName, P.Price, SUM(OD.Quantity) AS UnitsSold, SUM(OD.Quantity)*P.Price AS TotalRevenue
                       FROM Products P
                       LEFT JOIN OrderDetails OD ON OD.ProductID = P.ProductID
                       GROUP BY P.ProductID, P.ProductName, P.Price"""
            cs.execute(query)
            rows = cs.fetchall()

            print('Sales Report:')
            print("Product ID | Product Name | Price | Units Sold | Revenue")
            for row in rows:
                print(f"{row[0]} | {row[1]} | {row[2]} | {row[3]} | {row[4]}")

        except Exception as e:
            raise e

        finally:
            DBConnector.closeConnection(conn, cs)

    def updateCustomer(self, customer_id, choice):
        def updateDetails():
            email = input('Enter new email: ')
            phone = input('Enter new phone number: ')
            address = input('Enter new address: ')
            try:
                conn = DBConnector.openConnection()
                cs = conn.cursor()
                cs.execute("SELECT * FROM Customers WHERE CustomerID = %s", (customer_id,))
                customer_details = cs.fetchone()
                if customer_details:
                    customer = Customers(*customer_details)  # Passing the row returned from cursor as argument to Customer class instance
                    customer.set_email(email)
                    customer.set_phone(phone)
                    customer.set_address(address)
                    cs.execute("""UPDATE Customers SET Email = %s, Phone = %s, Address = %s
                                    WHERE CustomerID = %s""",
                               (customer.get_email(), customer.get_phone(), customer.get_address(), customer_id))
                    conn.commit()
                    print("Customer details updated")
                else:
                    print("Customer not found")
            except Exception as e:
                conn.rollback()
                raise e
            finally:
                DBConnector.closeConnection(conn, cs)

        def showDetails():
            try:
                conn = DBConnector.openConnection()
                cs = conn.cursor()
                cs.execute("SELECT * FROM Customers WHERE CustomerID = %s", (customer_id,))
                detail = cs.fetchone()
                print('Customer ID: ', detail[0])
                print('First Name: ', detail[1])
                print('Last Name: ', detail[2])
                print('Email: ', detail[3])
                print('Phone: ', detail[4])
                print('Address: ', detail[5])
                conn.commit()
            except Exception as e:
                conn.rollback()
                raise e
            finally:
                DBConnector.closeConnection(conn, cs)

        if choice == 1:
            updateDetails()
        elif choice == 2:
            showDetails()
        else:
            print("Incorrect choice, please try again\n")

    def productSearchandRecommend(self, choice):
        def searchProduct():
            product_id = input('Enter a product id: ')
            try:
                conn = DBConnector.openConnection()
                cs = conn.cursor()
                cs.execute("SELECT * FROM Products WHERE ProductID = %s", (product_id,))
                rows = cs.fetchone()
                if rows:
                    print('A match has been found\n')
                    print('Product ID: ', rows[0])
                    print('Product Name: ', rows[1])
                    print('Product Description: ', rows[2])
                    print('Product Price: ', rows[3])
                else:
                    print('Product Not Found\n')

            except Exception as e:
                conn.rollback()
                raise e
            finally:
                DBConnector.closeConnection(conn, cs)

        def recommendProduct():
            product_id = input('Enter a product id: ')
            try:
                conn = DBConnector.openConnection()
                cs = conn.cursor()
                cs.execute("SELECT Category FROM Products WHERE ProductID = %s", (product_id,))
                category = cs.fetchone()[0]
                cs.execute("SELECT * FROM Products WHERE Category = %s", (category,))
                recommended_products = cs.fetchall()

                if recommended_products:
                    print('Here are the recommended products: \n')
                    for product in recommended_products:
                        print(product[1])
                else:
                    print('No recommendations')
            except Exception as e:
                conn.rollback()
                print("Error recommending products:", e)
            finally:
                DBConnector.closeConnection(conn, cs)

        if choice == 1:
            searchProduct()
        elif choice == 2:
            recommendProduct()
        else:
            print('Invalid choice. try again')
            return