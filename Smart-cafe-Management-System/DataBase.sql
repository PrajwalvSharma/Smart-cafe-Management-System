CREATE DATABASE cafe_db;

USE cafe_db;


CREATE TABLE menu (
    id INT AUTO_INCREMENT PRIMARY KEY,
    item_name VARCHAR(100) UNIQUE NOT NULL,
    price DECIMAL(10,2) NOT NULL
);


CREATE TABLE orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    item_id INT,
    quantity INT NOT NULL,
    total_price DECIMAL(10,2) NOT NULL,
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (item_id) REFERENCES menu(id)
    ON DELETE CASCADE
);
select * from menu