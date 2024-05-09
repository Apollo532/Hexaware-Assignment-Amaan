CREATE DATABASE TechShop;

USE TechShop;

CREATE TABLE Customers (
    CustomerID INT AUTO_INCREMENT PRIMARY KEY,
    FirstName VARCHAR(20) NOT NULL,
    LastName VARCHAR(20),
    Email VARCHAR(45) NOT NULL,
    Phone VARCHAR(20),
    Address VARCHAR(80) NOT NULL
);

CREATE TABLE Products (
    ProductID INT PRIMARY KEY,
    ProductName VARCHAR(100),
    Description TEXT,
    Price DECIMAL(10, 2)
);

CREATE TABLE Orders (
    OrderID INT PRIMARY KEY,
    CustomerID INT,
    OrderDate DATE,
    TotalAmount DECIMAL(10, 2),
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
);

CREATE TABLE OrderDetails (
    OrderDetailID INT PRIMARY KEY,
    OrderID INT,
    ProductID INT,
    Quantity INT,
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID),
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID)
);

CREATE TABLE Inventory (
    InventoryID INT PRIMARY KEY,
    ProductID INT,
    QuantityInStock INT,
    LastStockUpdate DATE,
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID)
);

INSERT INTO Customers (FirstName, LastName, Email, Phone, Address)
VALUES
    ('Liam', 'Johnson', 'liam.johnson@gmail.com', '123-456-7890', '123 Main St, Anytown, USA'),
    ('Olivia', 'Smith', 'olivia.smith@yahoo.com', '456-789-0123', '456 Elm St, Anycity, USA'),
    ('Aarav', 'Garcia', 'aarav.garcia@outlook.com', '789-012-3456', '789 Oak St, Anystate, USA'),
    ('Emma', 'Martinez', 'emma.martinez@gmail.com', '321-654-9870', '321 Maple St, Anyvillage, USA'),
    ('Sophia', 'Lee', 'sophia.lee@yahoo.com', '654-987-0123', '654 Cedar St, Anysuburb, USA'),
    ('William', 'Wang', 'william.wang@gmail.com', '987-012-3456', '987 Pine St, Anyhamlet, USA'),
    ('Ava', 'Kim', 'ava.kim@yahoo.com', '111-222-3333', '111 Oak St, Anycity, USA'),
    ('Noah', 'Nguyen', 'noah.nguyen@outlook.com', '444-555-6666', '444 Elm St, Anystate, USA'),
    ('Isabella', 'Brown', 'isabella.brown@gmail.com', '777-888-9999', '777 Maple St, Anytown, USA'),
    ('Sophie', 'Lopez', 'sophie.lopez@yahoo.com', '000-111-2222', '000 Cedar St, Anyvillage, USA');
    

INSERT INTO Products (ProductID, ProductName, Description, Price)
VALUES
    (1, 'Smartphone', 'Smartphone with high-resolution camera', 599.99),
    (2, 'Laptop', 'Thin and lightweight laptop with SSD storage', 999.99),
    (3, 'Headphones', 'Wireless noise-canceling headphones', 199.99),
    (4, 'Smart Watch', 'Fitness tracker with heart rate monitor', 149.99),
    (5, 'Tablet', '10-inch tablet with retina display', 399.99),
    (6, 'Digital Camera', 'Mirrorless digital camera with 4K video recording', 799.99),
    (7, 'Gaming Console', 'Next-gen gaming console with VR support', 499.99),
    (8, 'Bluetooth Speaker', 'Portable Bluetooth speaker with long battery life', 79.99),
    (9, 'External Hard Drive', '1TB external hard drive with USB 3.0', 69.99),
    (10, 'Wireless Router', 'Dual-band wireless router for high-speed internet', 129.99);
    

INSERT INTO Orders (OrderID, CustomerID, OrderDate, TotalAmount)
VALUES
    (1, 1, '2023-11-05', 249.99),
    (2, 2, '2023-11-07', 799.99),
    (3, 3, '2023-11-20', 149.99),
    (4, 4, '2023-12-12', 399.99),
    (5, 5, '2023-12-15', 999.99),
    (6, 6, '2023-12-18', 79.99),
    (7, 7, '2023-12-20', 129.99),
    (8, 8, '2024-01-14', 499.99),
    (9, 9, '2024-01-26', 129.99),
    (10, 10, '2024-02-17', 69.99),
    (11, 1, '2024-02-24', 149.99),
    (12, 2, '2024-03-05', 129.99),
    (13, 3, '2024-03-19', 399.99),
    (14, 4, '2024-04-04', 199.99),
    (15, 5, '2024-04-18', 999.99);
    

INSERT INTO OrderDetails (OrderDetailID, OrderID, ProductID, Quantity) VALUES
(1, 1, 3, 2),
(2, 2, 6, 1),
(3, 3, 3, 3),
(4, 4, 5, 2),
(5, 5, 2, 1),
(6, 6, 4, 4),
(7, 7, 7, 3),
(8, 8, 1, 1),
(9, 9, 9, 2),
(10, 10, 10, 5),
(11, 11, 2, 2),
(12, 12, 3, 1),
(13, 13, 5, 3),
(14, 14, 8, 2),
(15, 15, 7, 1);

INSERT INTO Inventory (InventoryID, ProductID, QuantityInStock, LastStockUpdate) VALUES
(1, 1, 50, '2023-11-05'),
(2, 2, 30, '2023-11-07'),
(3, 3, 80, '2023-11-20'),
(4, 4, 20, '2023-12-12'),
(5, 5, 60, '2023-12-15'),
(6, 6, 40, '2023-12-18'),
(7, 7, 25, '2023-12-20'),
(8, 8, 70, '2024-01-14'),
(9, 9, 55, '2024-01-26'),
(10, 10, 45, '2024-02-17');

SELECT * FROM Customers;
SELECT * FROM Products;
SELECT * FROM Orders;
SELECT * FROM OrderDetails;
SELECT * FROM Inventory;















