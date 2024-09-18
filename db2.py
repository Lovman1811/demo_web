import sqlite3
conn=sqlite3.connect("sqlite.db")
conn.execute('''
        CREATE TABLE IF NOT EXISTS user_data (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        father_name VARCHAR(255),
        address TEXT,
        class_data INT)
        ''')
conn.close()

