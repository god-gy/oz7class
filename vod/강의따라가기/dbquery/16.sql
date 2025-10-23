use testdatabase;

UPDATE users
SET username = 'INSEOP'
WHERE user_id = 1;

-- 세이프모드 비활성화
SET SQL_SAFE_UPDATES = 0;

UPDATE users
SET username = 'SENIORS'
WHERE age = 25;

select row_count();

-- user의 age가 60 이상인 경우 'senior'로 username 설정, 
-- 그 외의 경우 username은 'young'로 설정
UPDATE users
SET username = CASE
    WHEN age >= 60 THEN 'senior_data'
    ELSE 'young_people'
END;

-- age가 30인 레코드 중에서 가장 나이가 어린 5명의 salary를 60000으로 수정
UPDATE users
SET username = 'top5_people'
WHERE age = 25
LIMIT 5;

-- 다른 서브쿼리 결과에 따라 업데이트
UPDATE products
SET price = price * 1.1
WHERE category_id IN (SELECT id FROM categories WHERE name = 'Electronics');

select * from users;