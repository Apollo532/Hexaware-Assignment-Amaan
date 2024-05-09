USE Techshop;

-- Q1: Retrieve Customer Information
SELECT O.OrderID,
       O.OrderDate,
       C.FirstName AS CustomerFirstName,
       C.LastName AS CustomerLastName,
       C.Email AS CustomerEmail,
       C.Phone AS CustomerPhone,
       C.Address AS CustomerAddress
FROM Orders O
JOIN Customers C ON O.CustomerID = C.CustomerID;


-- Q2: Revenue from each product
SELECT P.ProductName, SUM(OD.Quantity * P.Price) AS TotalRevenue
FROM OrderDetails OD
JOIN Products P ON OD.ProductID = P.ProductID
GROUP BY P.ProductName;


-- Q3: List customers who have made at least one purchase
SELECT C.FirstName, C.LastName, C.Phone, C.Email
FROM Customers AS C
JOIN Orders O ON O.CustomerID = C.CustomerID
GROUP BY C.CustomerID;


-- Q4: Top Product
SELECT P.ProductName, SUM(OD.Quantity) AS TotalQuantityOrdered
FROM OrderDetails OD
JOIN Products P ON OD.ProductID = P.ProductID
GROUP BY P.ProductName
ORDER BY TotalQuantityOrdered DESC
LIMIT 1;


-- Q5: Invalid query - schema inconsistency


-- Q6: Average Order Value
SELECT C.FirstName, C.LastName, AVG(O.TotalAmount) AS AverageOrderValue
FROM Orders O JOIN Customers C ON O.CustomerID = C.CustomerID
GROUP BY C.CustomerID;


-- Q7: Customer with most revenue
SELECT O.OrderID,
       C.FirstName,
       C.LastName,
       C.Email,
       C.Phone,
       C.Address,
       SUM(OD.Quantity * P.Price) AS TotalRevenue
FROM Orders O
JOIN OrderDetails OD ON O.OrderID = OD.OrderID
JOIN Products P ON OD.ProductID = P.ProductID
JOIN Customers C ON O.CustomerID = C.CustomerID
GROUP BY O.OrderID, C.CustomerID
ORDER BY TotalRevenue DESC
LIMIT 1;


-- Q8: Product and count of orders
SELECT P.ProductID,
       P.ProductName,
       COUNT(OD.OrderDetailID) AS NumberOfOrders
FROM Products P
LEFT JOIN OrderDetails OD ON P.ProductID = OD.ProductID
GROUP BY P.ProductID, P.ProductName;


-- Q9: List Customers who purchased a specific product
SELECT DISTINCT C.CustomerID,
       C.FirstName,
       C.LastName,
       C.Email,
       C.Phone,
       C.Address
FROM Customers C
JOIN Orders O ON C.CustomerID = O.CustomerID
JOIN OrderDetails OD ON O.OrderID = OD.OrderID
JOIN Products P ON OD.ProductID = P.ProductID
WHERE P.ProductName = 'Laptop';


-- Q10: Revenue from all orders in a time frame
SELECT SUM(TotalAmount) AS TotalRevenue
FROM Orders
WHERE OrderDate >= '2022-08-01' AND OrderDate <= '2023-07-31';
