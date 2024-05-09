-- Q1: Retrieve names, emails of all customers
SELECT FirstName, LastName, Email
FROM Customers;

-- Q2: List all orders with their order dates and corresponding customer names
SELECT o.OrderID, o.OrderDate, c.FirstName, c.LastName
FROM Orders o
JOIN Customers c ON o.CustomerID = c.CustomerID;

-- Q3: Insert a new customer record into the "Customers" table
INSERT INTO Customers (FirstName, LastName, Email, Address)
VALUES ('Varun', 'Sinha', 'varun.sinha6@gmail.com', 'Mumbai');

SELECT * FROM Customers;

UPDATE Customers
SET Phone = '9825786541'
WHERE FirstName = 'Varun' AND LastName = 'Sinha';

-- Q4: Update price by 10%
UPDATE Products
SET Price = Price * 1.1
WHERE ProductID BETWEEN 1 AND 11;

SELECT * FROM Products;

-- Q5: Delete specific order
DELETE FROM OrderDetails WHERE OrderID = 5;
DELETE FROM Orders WHERE OrderID = 5;

-- Q6: Insert new entry in orders table
INSERT INTO Orders VALUES (11, 11, '2023-07-12', 63400);

-- Q7: Update Contact information in Customer Table
UPDATE Customers
SET Email = 'varun.sinha5@outlook.com', Address = 'Indore'
WHERE FirstName = 'Varun' AND LastName = 'Sinha';

-- Q8: Recalculate Total Cost of each order
UPDATE Orders
SET TotalAmount = (
    SELECT SUM(od.Quantity * p.Price)
    FROM OrderDetails od
    JOIN Products p ON od.ProductID = p.ProductID
    WHERE od.OrderID = Orders.OrderID
);

-- Q9: Delete Orders from from one specific customer
DELETE FROM OrderDetails
WHERE OrderID IN (
    SELECT OrderID
    FROM Orders
    WHERE CustomerID = 5
);

DELETE FROM Orders
WHERE CustomerID = 4;

-- Q10: Insert new Product in Products table
INSERT INTO Products VALUES (11, 'Smart TV', '42 inch Android enabled TV with 4 year updates', 47650);

-- Q12: Number of Orders from each customer.
SELECT c.CustomerID, c.FirstName, c.LastName, COUNT(o.OrderID) AS NumberOfOrders
FROM Customers c
LEFT JOIN Orders o ON c.CustomerID = o.CustomerID
GROUP BY c.CustomerID, c.FirstName, c.LastName;

