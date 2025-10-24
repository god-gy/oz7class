use testdatabase;
create TABLE users(
	id int primary key AUTO_INCREMENT,
    password varchar(4),
    name varchar(3),
    gesnder ENUM('male', 'female'),
    email VARCHAR(15),
    birthday char(6),
    age TINYINT,
    company ENUM('samsung', 'lg', 'hyundai')
);
create table boards(
	id int primary key AUTO_INCREMENT,
    title varchar(5),
    content varchar(10),
    likes int check(likes between 1 and 100),
    ing char(1) default 'c',
    created date,
    user_id int,
    FOREIGN KEY(user_id) REFERENCES users(id)
);