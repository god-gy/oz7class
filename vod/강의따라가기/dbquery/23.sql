-- 서브쿼리
-- 특정 금액 이상의 주문: 500달러 이상의 총 주문 금액을 기록한 주문들을 조회하세요.
SELECT orderNumber, SUM(quantityOrdered * priceEach) AS totalAmount
FROM orderdetails
GROUP BY orderNumber
HAVING totalAmount > 500;

-- 평균 이상 결제 고객: 평균 결제 금액보다 많은 금액을 결제한 고객들의 목록을 조회하세요.
SELECT customerNumber, SUM(amount) AS totalPayment
FROM payments
GROUP BY customerNumber
HAVING totalPayment > (SELECT AVG(amount) FROM payments);

-- 주문 없는 고객: 아직 주문을 하지 않은 고객의 목록을 조회하세요.
SELECT customerName
FROM customers
WHERE customerNumber NOT IN (SELECT customerNumber FROM orders);

-- 최대 매출 고객: 가장 많은 금액을 지불한 고객의 이름과 총 결제 금액을 조회하세요.
SELECT c.customerName, SUM(od.quantityOrdered * od.priceEach) AS totalSpent
FROM customers c
JOIN orders o ON c.customerNumber = o.customerNumber
JOIN orderdetails od ON o.orderNumber = od.orderNumber
GROUP BY c.customerName
ORDER BY totalSpent DESC
LIMIT 1;

-- 데이터 수정 및 관
-- 신규 고객 추가: 'customers' 테이블에 새로운 고객을 추가하는 쿼리를 작성하세요.
INSERT INTO customers (customerName, contactLastName, contactFirstName, phone, addressLine1, addressLine2, city, state, postalCode, country, salesRepEmployeeNumber, creditLimit)
VALUES ('New Customer', 'Lastname', 'Firstname', '123-456-7890', '123 Street', 'Suite 1', 'City', 'State', 'PostalCode', 'Country', 1002, 50000.00);

-- 제품 가격 변경: 'Classic Cars' 제품 라인의 모든 제품 가격을 10% 인상하는 쿼리를 작성하세요.
UPDATE products
SET buyPrice = buyPrice * 1.10
WHERE productLine = 'Classic Cars';

-- 고객 데이터 업데이트: 특정 고객의 이메일 주소를 변경하는 쿼리를 작성하세요.
UPDATE customers
SET email = 'newemail@example.com'
WHERE customerNumber = 103;

-- 직원 전보: 특정 직원을 다른 사무실로 이동시키는 쿼리를 작성하세요.
UPDATE employees
SET officeCode = '2'
WHERE employeeNumber = 1002;
