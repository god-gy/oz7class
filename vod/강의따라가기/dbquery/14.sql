use testdatabase;

CREATE TABLE users(
	user_id INT PRIMARY KEY AUTO_INCREMENT,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INT
);

INSERT INTO users(username, email, age) VALUES('inseop', 'inseop@gmail.com', 25);

INSERT INTO users(username, email) VALUES('inseop2', 'inseop2@gmail.com');

INSERT INTO users (username, email, age) VALUES
    ('alice', 'alice@example.com', 30),
    ('bob', 'bob@example.com', 28),
    ('charlie', 'charlie@example.com', 35);

INSERT INTO users (username, email) VALUES
    ('david', 'david@example.com'),
    ('elena', 'elena@example.com');

INSERT IGNORE INTO users (username, email, age) VALUES ('john_doe', 'john@example.com', 25);

INSERT INTO users (username, email, age) VALUES ('john_doe', 'john@example.com', 100)
ON DUPLICATE KEY UPDATE age = 25;

INSERT INTO users SET username='tuna', email='tuna@example.com', age=25;

SELECT * FROM users;

