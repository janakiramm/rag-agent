-- Drop database if it already exists
DROP DATABASE IF EXISTS ecommerce;

-- Create database
CREATE DATABASE ecommerce;
USE ecommerce;

-- Create categories table
CREATE TABLE categories (
    category_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create products table
CREATE TABLE products (
    product_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    price DECIMAL(10, 2) NOT NULL,
    stock INT NOT NULL,
    category_id INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (category_id) REFERENCES categories(category_id)
);

-- Create orders table
CREATE TABLE orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    product_id INT NOT NULL,
    customer_id INT NOT NULL,
    quantity INT NOT NULL,
    total_amount DECIMAL(10, 2) NOT NULL,
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);

-- Insert data into categories
INSERT INTO categories (name, description) VALUES
('Electronics', 'Devices and gadgets'),
('Clothing', 'Apparel and accessories'),
('Home & Kitchen', 'Household items and kitchenware');

-- Insert data into products
INSERT INTO products (name, description, price, stock, category_id) VALUES
('Smartphone', 'Latest model smartphone', 699.99, 50, 1),
('Laptop', 'High performance laptop', 999.99, 30, 1),
('Headphones', 'Noise-cancelling headphones', 199.99, 100, 1),
('T-shirt', 'Cotton t-shirt', 19.99, 200, 2),
('Jeans', 'Denim jeans', 49.99, 150, 2),
('Jacket', 'Leather jacket', 149.99, 75, 2),
('Blender', 'High speed blender', 89.99, 40, 3),
('Cookware Set', 'Non-stick cookware set', 129.99, 20, 3),
('Vacuum Cleaner', 'Powerful vacuum cleaner', 149.99, 25, 3);

-- Insert data into orders
INSERT INTO orders (product_id, customer_id, quantity, total_amount, order_date) VALUES
(1, 1, 2, 1399.98, '2023-04-10'),
(3, 1, 1, 199.99, '2023-04-15'),
(2, 1, 1, 999.99, '2023-05-01'),
(5, 2, 3, 149.97, '2023-05-20'),
(8, 2, 1, 129.99, '2023-06-05'),
(4, 3, 5, 99.95, '2023-06-15'),
(7, 3, 2, 179.98, '2023-06-25'),
(9, 4, 1, 149.99, '2023-06-28'),
(6, 4, 1, 149.99, '2023-06-30');