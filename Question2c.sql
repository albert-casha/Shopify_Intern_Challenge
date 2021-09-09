SELECT german_orders.OrderID,
       details.ProductID,
       details.Quantity,
       details.ProductName,
       COUNT(details.Quantity) as Number_of_orders,
       SUM(details.Quantity) as total_quantity
FROM (SELECT orders.*, customers.*
	FROM Orders as orders
	JOIN Customers as customers
 	ON orders.CustomerID = customers.CustomerID
	WHERE customers.Country = 'Germany'
    ) german_orders
LEFT JOIN (Select orderdetails.*, products.*
           FROM Orderdetails as orderdetails
           JOIN Products as products
           ON orderdetails.ProductID = products.ProductID) details
ON german_orders.OrderID = details.OrderID
GROUP BY ProductID
ORDER BY total_quantity DESC
