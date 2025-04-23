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