SELECT Customers.Name AS Customer, 
Books.Name AS Book,
COALESCE(Authors.Name, 'No Author') AS Author, 
Rents.State AS Status
FROM Rents
INNER JOIN Customers ON Rents.Customer_ID = Customers.ID
INNER JOIN Books ON Rents.Book_ID = Books.ID
LEFT JOIN Authors ON Books.Author_ID = Authors.ID;