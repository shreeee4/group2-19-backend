import mysql.connector
import random
import json
from process_slither import process_vulnerabilities

# Database connection configuration
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "root",
    "database": "mypythondb"
}

# Open the file and read the list of references (vulnerabilities)
vulnerabilities = process_vulnerabilities()

try:
    # Establish a connection to the MySQL server
    conn = mysql.connector.connect(**db_config)

    # Create a cursor object
    cursor = conn.cursor()

    # Check if the 'reports' table exists, create it if not
    cursor.execute("CREATE TABLE IF NOT EXISTS reports ("
                   "report_id INT AUTO_INCREMENT PRIMARY KEY,"
                   "report_number INT,"
                   "vulnerability_name VARCHAR(255))")

    cursor.execute("SELECT MAX(report_number) FROM reports")
    max_report_number = cursor.fetchone()[0]
    if max_report_number is None:
        report_number = 1000
    else:
        report_number = max_report_number + 1

    # Insert vulnerabilities into the 'reports' table
    for vulnerability in vulnerabilities:
        query = "INSERT INTO reports (report_number, vulnerability_name) VALUES (%s, %s)"
        data = (report_number, vulnerability)
        cursor.execute(query, data)

    # Commit changes and close the cursor and connection
    conn.commit()
    cursor.close()
    conn.close()

    print("Vulnerabilities inserted into the database.")

except mysql.connector.Error as err:
    print(f"Error: {err}")
