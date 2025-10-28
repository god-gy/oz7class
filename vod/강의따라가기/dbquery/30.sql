-- 문제: 배우 'GUINESS PENELOPE'가 출연한 모든 영화의 제목을 조회하시오.
SELECT f.title
FROM film f
JOIN film_actor fa ON f.film_id = fa.film_id
JOIN actor a ON fa.actor_id = a.actor_id
WHERE a.first_name = 'PENELOPE' AND a.last_name = 'GUINESS';

-- 문제: 각 카테고리별로 몇 개의 영화가 있는지 조회하시오.
SELECT c.name, COUNT(fc.film_id) as number_of_films
FROM category c
JOIN film_category fc ON c.category_id = fc.category_id
GROUP BY c.name;

-- 문제: 고객 ID가 5인 고객의 모든 대여 기록을 조회하시오.
SELECT r.rental_date, f.title
FROM rental r
JOIN inventory i ON r.inventory_id = i.inventory_id
JOIN film f ON i.film_id = f.film_id
WHERE r.customer_id = 5;

-- 문제: 가장 최근에 데이터베이스에 추가된 10개의 영화 제목을 조회하시오.
SELECT title, release_year
FROM film
ORDER BY release_year DESC
LIMIT 10;

-- 1. **특정 영화에 출연한 배우 목록 조회**
-- 'ACADEMY DINOSAUR' 영화에 출연한 모든 배우의 이름을 조회하시오.
SELECT a.first_name, a.last_name
FROM actor a
JOIN film_actor fa ON a.actor_id = fa.actor_id
JOIN film f ON fa.film_id = f.film_id
WHERE f.title = 'ACADEMY DINOSAUR';

-- 2. **특정 영화를 대여한 고객 목록 조회**
-- 'ACADEMY DINOSAUR' 영화를 대여한 모든 고객의 이름을 조회하시오.
SELECT DISTINCT c.first_name, c.last_name
FROM customer c
JOIN rental r ON c.customer_id = r.customer_id
JOIN inventory i ON r.inventory_id = i.inventory_id
JOIN film f ON i.film_id = f.film_id
WHERE f.title = 'ACADEMY DINOSAUR';

-- 3. **모든 고객과 그들이 가장 최근에 대여한 영화 조회**
-- 각 고객별로 가장 최근에 대여한 영화의 제목을 조회하시오.
SELECT c.customer_id, c.first_name, c.last_name, MAX(r.rental_date) as last_rental_date, f.title
FROM customer c
JOIN rental r ON c.customer_id = r.customer_id
JOIN inventory i ON r.inventory_id = i.inventory_id
JOIN film f ON i.film_id = f.film_id
GROUP BY c.customer_id, c.first_name, c.last_name, f.title;

-- 4. **각 영화별 평균 대여 기간 조회**
-- 각 영화별 평균 대여 기간을 일 단위로 계산하시오.
SELECT f.title, AVG(DATEDIFF(r.return_date, r.rental_date)) as avg_rental_period
FROM film f
JOIN inventory i ON f.film_id = i.film_id
JOIN rental r ON i.inventory_id = r.inventory_id
GROUP BY f.title
ORDER BY avg_rental_period DESC;
