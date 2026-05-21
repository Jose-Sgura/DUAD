CREATE TABLE IF NOT EXISTS Categories (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT NOT NULL,
    Description TEXT
);

CREATE TABLE IF NOT EXISTS Products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    Product_Code TEXT NOT NULL,
    Name TEXT NOT NULL,
    Price REAL DEFAULT 0,
    Entry_Date DATE,
    Brand TEXT,
    Stock INTEGER DEFAULT 0,
    Category_id INTEGER NOT NULL,
    FOREIGN KEY (Category_id) REFERENCES Categories(id)
);

CREATE TABLE IF NOT EXISTS Payment_Methods (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    Method_type TEXT NOT NULL,
    Bank_name TEXT
);

CREATE TABLE IF NOT EXISTS Invoices (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    Bill_Number INTEGER,
    Purchase_Date DATE,
    Total_Amount REAL DEFAULT 0,
    Payment_id INTEGER,
    FOREIGN KEY (Payment_id) REFERENCES Payment_Methods(id)
);

CREATE TABLE IF NOT EXISTS Invoice_Products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    Invoice_id INTEGER NOT NULL,
    Product_id INTEGER NOT NULL,
    Quantity INTEGER DEFAULT 0,
    Total_Amount REAL DEFAULT 0,
    FOREIGN KEY (Invoice_id) REFERENCES Invoices(id),
    FOREIGN KEY (Product_id) REFERENCES Products(id)
);

CREATE TABLE IF NOT EXISTS Cart (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    Email TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS Cart_Products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    Cart_id INTEGER NOT NULL,
    Product_id INTEGER NOT NULL,
    Quantity REAL DEFAULT 0,
    FOREIGN KEY (Cart_id) REFERENCES Cart(id),
    FOREIGN KEY (Product_id) REFERENCES Products(id)
);

CREATE TABLE IF NOT EXISTS Reviews (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    Product_code TEXT NOT NULL,
    Comment TEXT,
    Rating INTEGER CHECK(Rating >= 1 AND Rating <= 5),
    Date DATE,
    product_id INTEGER NOT NULL,
    FOREIGN KEY (product_id) REFERENCES Products(id)
);

INSERT INTO Categories (Name) VALUES ('Tecnologia');
INSERT INTO Categories (Name) VALUES ('Libros');
INSERT INTO Categories (Name) VALUES ('Electrodomesticos');

INSERT INTO Products (Product_Code, Name, Price, Entry_Date, Brand, Stock, Category_id) VALUES ('B001', 'The Great Gatsby', 30000.0, '2023-01-15', 'Scribner', 100, 1);
INSERT INTO Products (Product_Code, Name, Price, Entry_Date, Brand, Stock, Category_id) VALUES ('B002', '1984', 80000.0, '2023-01-16', 'Secker & Warburg', 150, 2);
INSERT INTO Products (Product_Code, Name, Price, Entry_Date, Brand, Stock, Category_id) VALUES ('B003', 'The Three-Body Problem', 100.0, '2023-01-17', 'Tor Books', 0, 3);
INSERT INTO Products (Product_Code, Name, Price, Entry_Date, Brand, Stock, Category_id) VALUES ('B004', 'Harry Potter', 45000.0, NULL, NULL, 155, 1);
INSERT INTO Products (Product_Code, Name, Price, Entry_Date, Brand, Stock, Category_id) VALUES ('B005', 'Maze Runner', 70000.0, NULL, NULL, 205, 2);
INSERT INTO Products (Product_Code, Name, Price, Entry_Date, Brand, Stock, Category_id) VALUES ('B006', 'Raton Perez', 35000.0, NULL, NULL, 140, 3);
INSERT INTO Products (Product_Code, Name, Price, Entry_Date, Brand, Stock, Category_id) VALUES ('B007', 'Harry Potter 2', 55000.0, NULL, NULL, 75, 1);
INSERT INTO Products (Product_Code, Name, Price, Entry_Date, Brand, Stock, Category_id) VALUES ('B008', 'Harry Potter 3', 20000.0, NULL, NULL, 111, 2);
INSERT INTO Products (Product_Code, Name, Price, Entry_Date, Brand, Stock, Category_id) VALUES ('B009', 'History of London', 78000.0, NULL, NULL, 156, 3);
INSERT INTO Products (Product_Code, Name, Price, Entry_Date, Brand, Stock, Category_id) VALUES ('B010', 'Horror Movies', 46000.0, NULL, NULL, 210, 1);

INSERT INTO Payment_Methods (Method_type, Bank_name) VALUES ('Tarjeta', 'BAC');
INSERT INTO Payment_Methods (Method_type, Bank_name) VALUES ('PayPal', NULL);
INSERT INTO Payment_Methods (Method_type, Bank_name) VALUES ('Transferencia', 'Scotiabank');


INSERT INTO Invoices (Bill_Number, Purchase_Date, Total_Amount, Payment_id) VALUES (1001, '2025-01-15', 60000.0, 1);
INSERT INTO Invoices (Bill_Number, Purchase_Date, Total_Amount, Payment_id) VALUES (1002, '2025-01-16', 700000.0, 2);
INSERT INTO Invoices (Bill_Number, Purchase_Date, Total_Amount, Payment_id) VALUES (1003, '2025-01-17', 200000.0, 3);

INSERT INTO Invoice_Products (Invoice_id, Product_id, Quantity, Total_Amount) VALUES (1, 1, 2, 60000.0);
INSERT INTO Invoice_Products (Invoice_id, Product_id, Quantity, Total_Amount) VALUES (2, 2, 5, 400000.0);
INSERT INTO Invoice_Products (Invoice_id, Product_id, Quantity, Total_Amount) VALUES (3, 3, 2, 200000.0);
INSERT INTO Invoice_Products (Invoice_id, Product_id, Quantity, Total_Amount) VALUES (2, 3, 3, 300000.0);

INSERT INTO Cart (Email) VALUES ('jose@email.com');
INSERT INTO Cart (Email) VALUES ('maria@email.com');

INSERT INTO Cart_Products (Cart_id, Product_id, Quantity) VALUES (1, 1, 2);
INSERT INTO Cart_Products (Cart_id, Product_id, Quantity) VALUES (1, 2, 1);
INSERT INTO Cart_Products (Cart_id, Product_id, Quantity) VALUES (2, 3, 3);

INSERT INTO Reviews (Product_code, Comment, Rating, Date, product_id) VALUES ('B001', 'Excelente libro', 5, '2025-01-20', 1);
INSERT INTO Reviews (Product_code, Comment, Rating, Date, product_id) VALUES ('B002', 'Muy bueno', 4, '2025-01-21', 2);
INSERT INTO Reviews (Product_code, Comment, Rating, Date, product_id) VALUES ('B003', 'Regular', 3, '2025-01-22', 3);
