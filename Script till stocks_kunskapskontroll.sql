CREATE DATABASE IF NOT EXISTS stocks_kunskapskontroll;
USE stocks_kunskapskontroll;

CREATE TABLE IF NOT EXISTS financials(
financials_id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
profit_margin INT,
valuation INT
);

INSERT INTO financials(financials_id, profit_margin, valuation)
VALUES
	(101, 17, 14),
    (102, 4.95, 10.97),
    (103, 10, 11.65),
    (104, 54, 9.59),
    (105, 53, 8.94),
    (106, 22.58, 24.4),
    (107, 10.18, 11.18);

CREATE TABLE IF NOT EXISTS stocks(
stock_id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
financials_id INT NOT NULL,
`company_name` CHAR(45),
created_at DATETIME
);

INSERT INTO stocks(stock_id, financials_id, `company_name`, created_at)
VALUES 
	(1, 101, "Sandvik", "2022-08-01 12:00"), 
    (2, 102, "Skanska", "2022-08-02 12:00"),
    (3, 103, "Husqvarna", "2022-08-03 12:00"),
    (4, 104, "SEB", "2022-08-04 12:00"),
    (5, 105, "Handelsbanken", "2022-08-05 12:00"),
    (6, 106, "Epiroc", "2022-08-06 12:00"),
    (7, 107, "Volvo", "2022-08-07 12:00");

ALTER TABLE stocks ADD CONSTRAINT FOREIGN KEY(financials_id) REFERENCES financials(financials_id);


CREATE TABLE IF NOT EXISTS business(
stock_id INT NOT NULL,
`industry` CHAR(45)
);

INSERT INTO business(stock_id, `industry`)
VALUES
	(1, "industri"),
    (2, "bygg"),
    (3, "industri"),
    (4, "bank"),
    (5, "bank"),
    (6, "industri"),
    (7, "industri");

ALTER TABLE business ADD CONSTRAINT FOREIGN KEY(stock_id) REFERENCES stocks(stock_id);

/* Nu är det dags att pusha in data i de sista tabellerna */

CREATE TABLE IF NOT EXISTS shareholders(
shareholder_id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
`shareholder_name` CHAR(45) NOT NULL
);

INSERT INTO shareholders(shareholder_id, `shareholder_name`)
VALUES
	(1, "Industrivärden"),
    (2, "Lundbergföretagen"),
    (3, "Investor");

CREATE TABLE IF NOT EXISTS stocks_shareholders(
stocks_shareholders_id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
stock_id INT NOT NULL,
shareholder_id INT NOT NULL
);

INSERT INTO stocks_shareholders(stocks_shareholders_id, stock_id, shareholder_id)
VALUES
	(1, 1, 1),
    (2, 1, 2),
    (3, 2, 1),
    (4, 2, 2),
    (5, 3, 2),
    (6, 3, 3),
    (7, 4, 3),
    (8, 5, 1),
    (9, 5, 2),
    (10, 6, 3),
    (11, 7, 1);

ALTER TABLE stocks_shareholders ADD CONSTRAINT FOREIGN KEY(stock_id) REFERENCES stocks(stock_id);
ALTER TABLE stocks_shareholders ADD CONSTRAINT FOREIGN KEY(shareholder_id) REFERENCES shareholders(shareholder_id);

ALTER TABLE company_about_csv
ADD about_id INT PRIMARY KEY AUTO_INCREMENT NOT NULL;

UPDATE company_about_csv
SET ceo = 'Carina Lundegård'
WHERE about_id = 5;

DELETE FROM company_about_csv
WHERE about_id = 7;



