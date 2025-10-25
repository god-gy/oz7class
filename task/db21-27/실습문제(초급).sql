use classicmodels;

-- 생성(CREATE)
INSERT INTO customers(customerNumber, customerName, contactLastName, contactFirstName, phone, addressLine1, city, country)
VALUES ('500005', '꿍쓰','김', '라', '01012345678', '개성로123', '개성', '북한');
INSERT INTO products(productCode, productName, productLine)
VALUES('N0_1999', '1999 moya', 'Motorcycles' );
INSERT INTO offices(officeCode, city, phone)
VALUES('100', 'NYC', '0212345678' );
INSERT INTO orders(orderNumber, orderDate, customerNumber)
VALUES('500005', '2025-01-29', '500005' );
INSERT INTO orderdetails(orderNumber, productCode)
VALUES('500005', 'N0_1999');
INSERT INTO payments(customerNumber, checkNumber)
VALUES('500005', 'MOYA003');
INSERT INTO productlines(productLine)
VALUES('Doll');
INSERT INTO customers(customerNumber, customerName, contactLastName, contactFirstName, phone, addressLine1, city, country)
VALUES ('500007', '먼지','신', '개', '01087654321', '강남쓰', '서울', '대한민국');
INSERT INTO products(productCode, productName, productLine)
VALUES('N0_30000', '뿌요열차', 'Trains' );

-- 읽기 (READ) 
SELECT * FROM customers;
SELECT * FROM products;
SELECT firstName, lastName, jobTitle FROM employees;
SELECT city, addressLine1, addressLine2, state, country FROM offices;
SELECT * FROM orders ORDER BY orderDate DESC LIMIT 10;
SELECT * FROM orderdetails WHERE orderNumber = '10100';
SELECT * FROM payments WHERE customerNumber = '103';
SELECT productLine, textDescription FROM productlines;
SELECT * FROM customers WHERE city = '개성';
SELECT * FROM products WHERE buyPrice BETWEEN 90 AND 100;

-- 갱신 (UPDATE)
UPDATE customers SET addressLine1 = '종로쓰' WHERE customerNumber = '500007';
UPDATE products SET buyPrice = 300 WHERE productCode = 'N0_30000';
UPDATE employees SET jobTitle = 'VP Sales' WHERE employeeNumber = '1702';
UPDATE offices SET phone = '03112345678' WHERE officeCode = '100';
UPDATE orders SET status = 'Shipped' WHERE orderNumber = '500005';
UPDATE orderdetails SET quantityOrdered = 100 WHERE orderNumber = '10100' AND productCode = 'S18_2248';
UPDATE payments SET amount = 800 WHERE customerNumber = '500005';
UPDATE productlines SET textDescription = '대충설명임' WHERE productLine = 'Doll';
UPDATE customers SET email= '이 테이블엔 이메일 정보가 없음 ㅋㅎㅋㅎ' WHERE customerNumber = '500007';
UPDATE products
SET buyPrice = CASE productCode 
	WHEN 'N0_1999' THEN '1000'
    WHEN 'N0_30000' THEN '3000'
END
WHERE productCode IN ('N0_1999', 'N0_30000');

-- 삭제 (DELETE)
DELETE FROM customers WHERE customerNumber = '500007';
DELETE FROM products WHERE productCode = 'N0_30000';
# employeeNumber는 외래키로 지정되어있어서 오류남. 종속된 값을 먼저 변경 후 삭제해야하지만.. 귀찮
DELETE FROM employees WHERE employeeNumber = '1002';
DELETE FROM offices WHERE officeCode = '100';
# orderNumber도 외래키. 디테일 먼저 지우면 오더도 지워짐.
DELETE FROM orders WHERE orderNumber = '10100';
DELETE FROM orderdetails WHERE orderNumber = '10100';
DELETE FROM payments WHERE customerNumber = '500005';
DELETE FROM productlines WHERE productLine = 'Doll';
# 안전모드라 안됨. SET SQL_SAFE_UPDATES = 0; 쓰고하면 됨.
DELETE FROM customers WHERE city = '개성';
# productLine 외래키.
DELETE FROM products WHERE productLine = 'Motorcycles';
