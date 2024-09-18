import streamlit as st
import sqlite3

# Function to insert data into the database
def insert_data(name, father_name, address, class_data):
    # Connect to SQLite
    connection = sqlite3.connect('sqlite.db')  # SQLite database file

    cursor = connection.cursor()

    # Create table if it doesn't exist
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS user_data (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        father_name TEXT NOT NULL,
        address TEXT NOT NULL,
        class_data INTEGER NOT NULL
    )
    """)

    # Insert data into the table
    cursor.execute("""
    INSERT INTO user_data (name, father_name, address, class_data)
    VALUES (?, ?, ?, ?)
    """, (name, father_name, address, class_data))

    # Commit the transaction
    connection.commit()

    # Close the connection
    connection.close()

# Streamlit app
name = st.text_input("Enter your name")
father_name = st.text_input("Enter your father's name")
address = st.text_area("Enter your address")
class_data = st.selectbox("Enter your class", (1, 2, 3, 4, 5))

if st.button("Submit"):
    insert_data(name, father_name, address, class_data)
    st.success("Data submitted successfully!")
