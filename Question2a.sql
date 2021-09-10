SELECT shippers.ShipperName, 
		COUNT(ShipperName) as Number_of_orders
FROM Shippers
JOIN Orders
ON Shippers.ShipperID = Orders.ShipperID
GROUP BY ShipperName
