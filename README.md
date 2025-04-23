# 🚀 Streamlit + MySQL App with Docker Compose

This project demonstrates how to set up a **Streamlit** application that connects to a **MySQL** database using **Docker Compose**. It features a clean multi-container architecture, initializes the database with dummy data, and displays it through a Streamlit dashboard.

---

## 📦 Prerequisites
- Docker & Docker Compose installed on your system ([Get Docker](https://docs.docker.com/get-docker/))
- Basic knowledge of Python, SQL, and Docker

---

## 🛠️ Project Structure

```bash
.
├── .venv/                 # (Optional) Python virtual environment
├── backend/               # Streamlit frontend application
│   ├── app.py             # Main Streamlit app script
│   └── Dockerfile         # Dockerfile for building the Streamlit image
├── db/                    # MySQL database setup
│   ├── init.sql           # SQL script to initialize and populate the DB
│   └── Dockerfile         # Dockerfile to customize the MySQL image
├── docker-compose.yml     # Docker Compose configuration to orchestrate services
└── README.md

```

🛠️ Step 1: Clone the Repository
Clone the project repository to your local machine.

Bash

git clone [https://github.com/Uttkarshsh/Container_Assignment](https://github.com/Uttkarshsh/Container_Assignment)
cd streamlit-mysql-docker
🛠️ Step 2: Start the Application
Use Docker Compose to build and run the entire application stack.

```bash
docker-compose up --build
```
This command will:

Build the custom MySQL image using the Dockerfile in the db directory and initialize it with the init.sql script.


Build the Streamlit application image using the Dockerfile in the backend directory.


Start both the MySQL and Streamlit containers and connect them via a Docker network defined in docker-compose.yml.


🌐 Step 3: Access the App

Once the containers are running, open your web browser and navigate to:
```bash

🔗 http://localhost:8501

```

You should see a Streamlit dashboard displaying the data fetched from the MySQL database.

📝 Streamlit App Code (backend/app.py)
```bash

Python

import streamlit as st
import mysql.connector

st.title("People Data from MySQL")

try:
    conn = mysql.connector.connect(
        host="db",
        user="user",
        password="password",
        database="testdb"
    )
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM people")
    data = cursor.fetchall()
    st.write("Fetched Data:")
    for row in data:
        st.write(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}")
except Exception as e:
    st.error(f"Error: {e}")


```
🛢️ Database Initialization (db/init.sql)
```bash


SQL

CREATE TABLE IF NOT EXISTS people (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    age INT
);

INSERT INTO people (name, age) VALUES
('Uttkarsh', 25),
('Dev', 30),
('Prashant', 28);

```
🐳 Docker Compose (docker-compose.yml)
```bash

YAML

version: '3.8'

services:
  db:
    build: ./db
    container_name: mysql_container
    restart: always
    environment:
      MYSQL_ROOT_PASSWORD: root
      MYSQL_DATABASE: testdb
      MYSQL_USER: user
      MYSQL_PASSWORD: password
    ports:
      - "3306:3306"
    networks:
      - mynetwork

  frontend:
    build: ./backend
    container_name: streamlit_container
    depends_on:
      - db
    ports:
      - "8501:8501"
    networks:
      - mynetwork

networks:
  mynetwork:
    driver: bridge


```
📦 MySQL Commands (Manual Access)
To interact with the MySQL database inside the container, you can use the following commands:



🔐 Step 1: Enter the MySQL Shell

```bash


docker exec -it mysql_container mysql -u user -p
When prompted for a password, enter:



```

password
💾 Step 2: Select the Database

SQL

USE testdb;
✅ Sample SQL Queries

🔽 Insert New Record


SQL
```bash

INSERT INTO people (name, age) VALUES ('Aman', 24);

```
🔍 Read All Records
```bash

SQL

SELECT * FROM people;
✏️ Update a Record

```
```bash

SQL

UPDATE people SET age = 26 WHERE name = 'Uttkarsh';
```

❌ Delete a Record
```bash
SQL

DELETE FROM people WHERE name = 'Dev';
```bash
```


💣 Drop the Table (⚠️ Be Careful)
```bash

SQL

DROP TABLE people;

```
🚪 Exit the MySQL Shell
```bash

Bash

exit;
```bash
```

🧹 Cleanup


To stop and remove all the Docker containers and the network created by Docker Compose, run:

Bash
```bash


docker-compose down


```
👨‍💻 Author
Made with ❤️ by Uttkarsh Sharma

🚀 Enjoy your Streamlit app connected to MySQL using Docker Compose! 🚀
