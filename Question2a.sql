SELECT Shippers.ShipperName, 
	   COUNT(ShipperName) as Number_of_orders
FROM Shippers
JOIN Orders
ON Shippers.ShipperID = Orders.ShipperID
WHERE Shippers.ShipperName = 'Speedy Express'
GROUP BY ShipperName
