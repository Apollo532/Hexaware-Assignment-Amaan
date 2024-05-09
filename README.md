### TechShop Project Overview

The TechShop project is an e-commerce application designed to manage a technology store's operations, including customer registration, product management, order placement, order tracking, inventory management, sales reporting, and customer account management. The project is implemented in Python, utilizing object-oriented programming concepts and a MySQL database for data storage.

### Project Structure

- **Main Module**: The `main.py` file serves as the entry point of the application, providing a command-line interface (CLI) for users to interact with different functionalities of the TechShop system.
  
- **DAO Module**: The `dao` package contains modules responsible for data access operations. Each DAO (Data Access Object) class interfaces with the database to perform CRUD (Create, Read, Update, Delete) operations related to specific entities such as customers, products, orders, and inventory.

- **Entity Module**: The `entity` package includes classes representing entities such as customers, products, and orders. These classes define the structure of the corresponding database tables and provide methods for interacting with the data.

- **Exceptions Module**: The `Exceptions.py` file defines custom exception classes used to handle specific error scenarios within the application, such as invalid data, insufficient stock, and incomplete orders.

- **Util Module**: The `util` package contains utility classes and functions used across the application, such as database connection management (`DBConnector.py`) and database utility functions (`DBUtil.py`).

### Functionality

The TechShop application offers the following functionalities:

1. **Customer Registration**: Allows new customers to register by providing their details such as name, email, phone, and address.
   
2. **Product Management**: Enables the management of the product catalog, including updating product information such as price and description, checking product availability, and viewing all products.

3. **Order Placement and Tracking**: Allows customers to place orders, track the status of their orders, and cancel orders if needed.

4. **Inventory Management**: Provides functionality for managing product inventory, including adding new products, updating stock quantities, removing discontinued products, and listing low or out-of-stock products.

5. **Sales Reporting**: Generates sales reports to analyze product performance, including total units sold and revenue generated for each product.

6. **Customer Account Management**: Allows customers to update their account details such as email, phone number, and address.

7. **Product Search and Recommendation**: Enables customers to search for specific products by ID and provides recommendations based on the product's category.
