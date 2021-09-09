SELECT shippers.ShipperName, 
		COUNT(ShipperName) as Number_of_orders
FROM Shippers as shippers
JOIN Orders as orders
ON shippers.ShipperID = orders.ShipperID
GROUP BY ShipperName
