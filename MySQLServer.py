import mysql.connector
from mysql.connector import errorcode

# Database configuration
config = {
    'user': 'root',           # Replace with your MySQL username
    'password': 'your_password',  # Replace with your MySQL password
    'host': 'localhost'       # Adjust if your MySQL server is remote
}

try:
    # Connect to MySQL server
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()

    # Try to create the database
    try:
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")
    except mysql.connector.Error as err:
        print(f"Failed creating database: {err}")

except mysql.connector.Error as err:
    print(f"Error connecting to MySQL: {err}")

finally:
    # Clean up
    if 'cursor' in locals():
        cursor.close()
    if 'conn' in locals() and conn.is_connected():
        conn.close()
