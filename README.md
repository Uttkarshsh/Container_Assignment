# 🚀 Streamlit + MySQL App with Docker Compose

This project demonstrates how to set up a **Streamlit** application that connects to a **MySQL** database using **Docker Compose**. It features a clean multi-container architecture, initializes the database with dummy data, and displays it through a Streamlit dashboard.

---

## 📁 Project Structure

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
🧰 Prerequisites
Docker & Docker Compose

Basic knowledge of Python, SQL, and Docker

⚙️ Getting Started
1️⃣ Clone the Repository
bash
Copy
Edit
git clone https://github.com/Uttkarshsh/Container_Assignment
cd streamlit-mysql-docker
2️⃣ Start the Application
bash
Copy
Edit
docker-compose up --build
This command will:

Build the custom MySQL image and initialize it using init.sql

Build and run the Streamlit app in a separate container

Connect both containers via a Docker network

🌐 Access the App
Once the containers are running, open your browser and navigate to:

🔗 http://localhost:8501

You’ll see a dashboard displaying data from the MySQL database.

📝 Streamlit App Code (backend/app.py)
python
Copy
Edit
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
🛢️ Database Initialization (db/init.sql)
sql
Copy
Edit
CREATE TABLE IF NOT EXISTS people (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    age INT
);

INSERT INTO people (name, age) VALUES
('Uttkarsh', 25),
('Dev', 30),
('Prashant', 28);
🐳 Docker Compose (docker-compose.yml)
yaml
Copy
Edit
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
📦 MySQL Commands (Manual Access)
To interact with the MySQL database inside the container, follow these steps:

🔐 Step 1: Enter the MySQL Shell
bash
Copy
Edit
docker exec -it mysql_container mysql -u user -p
When prompted for a password, enter:

bash
Copy
Edit
password
💾 Step 2: Select the Database
sql
Copy
Edit
USE testdb;
✅ Sample SQL Queries
🔽 Insert New Record
sql
Copy
Edit
INSERT INTO people (name, age) VALUES ('Aman', 24);
🔍 Read All Records
sql
Copy
Edit
SELECT * FROM people;
✏️ Update a Record
sql
Copy
Edit
UPDATE people SET age = 26 WHERE name = 'Uttkarsh';
❌ Delete a Record
sql
Copy
Edit
DELETE FROM people WHERE name = 'Dev';
💣 Drop the Table (⚠️ Be Careful)
sql
Copy
Edit
DROP TABLE people;
🚪 Exit the MySQL Shell
bash
Copy
Edit
exit;
🧼 Cleanup
To stop and remove all services and networks:

bash
Copy
Edit
docker-compose down
👨‍💻 Author
Made with ❤️ by Uttkarsh Sharma
