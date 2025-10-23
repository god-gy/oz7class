-- 모든 사용자와 그들이 만든 주문을 조회합니다. 사용자와 주문 테이블 간의 user_id를 기준으로 매칭된 행을 반환합니다.
select * from users
inner join orders on users.user_id = orders.user_id;

-- 사용자 테이블의 모든 행을 포함하고, 주문 테이블과 매칭되는 경우 해당 주문 정보를 포함합니다.
select * from users
left join orders
on users.user_id = orders.user_id;

-- 주문 테이블의 모든 행을 포함하고, 사용자 테이블과 매칭되는 경우 해당 사용자 정보를 포함합니다.
select * from users
	RIGHT join orders
	on users.user_id = orders.user_id;