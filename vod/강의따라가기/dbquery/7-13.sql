create user 'fishbread_user'@'localhost' identified by '0000';
grant all privileges on *.* to 'fishbread_user'@'localhost';
flush privileges;
show grants for 'fishbread_user'@'localhost';

create database fishbread_db;
use fishbread_db;

create table users(
	user_id int primary key auto_increment,
    name varchar(255) not null,
    age int not null,
    email varchar(100) unique,
    is_business boolean default false
);

create table orders(
	order_id int primary key auto_increment,
    user_id int,
    order_date date,
    amount decimal(10,2),
	foreign key (user_id) references users(user_id)	
);

create table inventory(
	item_id int primary key auto_increment,
    item_name varchar(255) not null,
    quantity int not null
);

create table sales(
	sale_id int primary key auto_increment,
    order_id int,
    item_id int,
    quantity_sold int not null,
    foreign key (order_id) references orders(order_id),
    foreign key (item_id) references inventory(item_id)
);

create table daily_sales(
	date date primary key,
    total_sales decimal(10,2) not null
);





