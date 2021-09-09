SELECT employees.LastName, 
	   employees.FirstName, 
       COUNT(orders.OrderID) as Number_of_Orders,
FROM Orders as orders
JOIN Employees as employees
ON orders.EmployeeID = employees.EmployeeID
GROUP BY employees.LastName, employees.FirstName
ORDER BY Number_of_Orders DESC
