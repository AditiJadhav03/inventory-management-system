 Inventory Management System



1) Overview



This project is a command-line based Inventory Management System developed using  Python and SQLite.

It simulates a real retail store/warehouse system where products can be added, tracked, sold, and monitored for low stock.



The application allows a shop owner or warehouse staff to manage inventory efficiently and prevent stock shortages.


2) Features



- Add new products

-  View available inventory

- Update product quantity

- Search product by name

- Record product sales

- Low stock alert system



3) Technologies Used



-  Python

-  SQLite Database

-  Command Line Interface (CLI)



---



4)  How the System Works



1. Store manager adds products into inventory

2. Products are saved into a database

3. When a sale happens, stock automatically decreases

4. If stock goes below minimum level, the system shows a low stock alert.


This is similar to real retail store inventory software used in shops and warehouses.



---


5)  Project Structure





inventory-management-system/

│

├── main.py

├── database.py

├── inventory.db

├── screenshots/

└── README.md




6) Screenshots



 - Add Product
 - View Inventory
 -  Sale Recorded
 - Low Stock Alert




7) How to Run the Project



1) Install Python (version 3.x)

2) Download or clone this repository

3) Run the database setup:


python database.py


4) Start the program:


python main.py


---



 8) Use Case



Retail stores and warehouses use inventory systems to:



 Track available stock

 Prevent stock-outs

 Monitor product movement

 Maintain inventory records



---



9)  What This Project Demonstrates



Understanding of retail operations

Database-driven application

CRUD operations (Create, Read, Update, Delete)

Real-world business problem solving



