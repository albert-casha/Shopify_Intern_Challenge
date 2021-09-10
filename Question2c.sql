SELECT details.ProductID,
       details.Quantity,
       details.ProductName,
       COUNT(details.Quantity) as Number_of_orders,
       SUM(details.Quantity) as total_quantity
FROM (SELECT Orders.OrderID
	FROM Orders
	JOIN Customers
 	ON Orders.CustomerID = Customers.CustomerID
	WHERE Customers.Country = 'Germany'
    ) german_orders
LEFT JOIN (Select Orderdetails.OrderID, 
	   Orderdetails.ProductID, 
	   Orderdetails.Quantity, 
	   Products.ProductID, 
	   Products.ProductName
           FROM Orderdetails
           JOIN Products
           ON Orderdetails.ProductID = Products.ProductID) details
ON german_orders.OrderID = details.OrderID
GROUP BY ProductID
ORDER BY total_quantity DESC
