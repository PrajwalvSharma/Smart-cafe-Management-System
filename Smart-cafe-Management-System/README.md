# ☕ Smart Cafe Management System

A console-based Smart Cafe Management System developed using **Python** and **MySQL**. This project allows cafe staff to manage menu items, place customer orders, generate bills, and maintain records efficiently.

## 🚀 Features

* ➕ Add new menu items
* ❌ Remove existing menu items
* 📋 View complete menu
* 🧾 Place customer orders
* 💰 Automatic bill generation
* 🔄 Reset menu and order records
* 🗄️ MySQL database integration
* 🔍 Duplicate item validation

## 🛠️ Technologies Used

* Python 3
* MySQL
* MySQL Connector for Python
* MySQL Workbench

## 📂 Project Structure

```
Smart-Cafe-Management-System/
│
├── smart_cafe.py
├── README.md
└── database.sql
```

## 🗃️ Database Setup

### Create Database

```sql
CREATE DATABASE cafe_db;
USE cafe_db;
```

### Create Menu Table

```sql
CREATE TABLE menu (
    id INT AUTO_INCREMENT PRIMARY KEY,
    item_name VARCHAR(100) UNIQUE NOT NULL,
    price DECIMAL(10,2) NOT NULL
);
```

### Create Orders Table

```sql
CREATE TABLE orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    item_id INT,
    quantity INT NOT NULL,
    total_price DECIMAL(10,2) NOT NULL,
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (item_id) REFERENCES menu(id)
    ON DELETE CASCADE
);
```

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/Smart-Cafe-Management-System.git
cd Smart-Cafe-Management-System
```

### 2. Install Required Package

```bash
pip install mysql-connector-python
```

### 3. Configure Database Connection

Update the database credentials in the Python file:

```python
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="cafe_db"
)
```

### 4. Run the Program

```bash
python smart_cafe.py
```

## 📸 Sample Menu

```
===== SMART CAFE SYSTEM =====

1. Add Item
2. Remove Item
3. View Menu
4. Place Order
5. Reset Menu
6. Exit
```

## 📖 Functionalities

### Add Item

Allows administrators to add new food or beverage items to the menu.

### Remove Item

Deletes selected menu items from the database.

### View Menu

Displays all available menu items with their IDs and prices.

### Place Order

Creates customer orders and automatically generates the bill.

### Reset Menu

Clears menu and order data while resetting ID counters.

## 🎯 Learning Outcomes

* Python Programming
* Database Connectivity using MySQL Connector
* CRUD Operations
* SQL Queries
* Console-Based Application Development
* Database Management

## 👨‍💻 Author

**Prajwal V Sharma**

Electronics and TeleCommunication Engineering (ETE)

## 📜 License

This project is developed for educational and learning purposes.
