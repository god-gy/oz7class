use testdatabase;

select * from users;
select DISTINCT age FROM users;
select age, age*100 as age100 from users;

select * from users ORDER BY age;
select * from users ORDER BY age desc;
SELECT * FROM users ORDER BY age ASC, username DESC;

select * from users where age >=35;
select * from users where username = 'john_doe';

select * from users
where username = 'inseop' and
age = 25;

select * from users
WHERE not age = 20;

select * from users
WHERE age between 26 and 50 limit 1;

select * from users limit 9,3;

select age, count(*) as age_count from users GROUP BY age;

-- 나이가 30 이상인 경우 '성인', 미만인 경우 '미성년자'로 변환하여 조회
SELECT
  username,
  age,
  CASE WHEN age >= 30 THEN '성인' ELSE '미성년자' END AS age_group
FROM users;

-- 나이에 따라 내림차순으로 순위 부여하여 조회
SELECT
  username,
  age,
  ROW_NUMBER() OVER (ORDER BY age DESC) AS 'rank'
FROM users;