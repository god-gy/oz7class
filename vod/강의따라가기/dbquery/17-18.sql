use testdatabase;

delete from users where age = 25;
delete from users where username = 'young_people' limit 1;

select * from users;

use testdatabase;

create table orders(
	order_id int primary key auto_increment,
    user_id int,
    product_name varchar(255),
    foreign key (user_id) references users(user_id)
);

delete from users;