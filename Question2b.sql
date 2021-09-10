SELECT Employees.LastName, 
       Employees.FirstName, 
       COUNT(Orders.OrderID) as Number_of_Orders
FROM Orders
JOIN Employees
ON Orders.EmployeeID = Employees.EmployeeID
GROUP BY Employees.LastName, Employees.FirstName
ORDER BY Number_of_Orders DESC
