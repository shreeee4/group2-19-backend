import mysql.connector
from datetime import date
from process_slither import process_vulnerabilities
from database import *

# Open the file and read the vulnerabilities
vulnerabilities = process_vulnerabilities()

db_config = database_config()
structure = database_structure()
vulnerabilitiy_statements = valnrabilaties_insert()

try:
    # Establish a connection to the MySQL server
    conn = mysql.connector.connect(**db_config)
    print("Connection established")
    # Create a cursor object
    cursor = conn.cursor()
    print("Cursor created")

    # Check if all the tables exist, create them if not
    for create_table_statements in structure:
        cursor.execute(create_table_statements)

    print("Tables Created")

    # Check if the Vulnerabilities table is empty
    cursor.execute("SELECT COUNT(*) FROM Vulnerabilities")
    print("Count executed")
    Vulnerabilitiy_amount = cursor.fetchone()[0]
    if Vulnerabilitiy_amount == 0:
        for create_vulnerability_statement in vulnerabilitiy_statements:
            cursor.execute(create_vulnerability_statement)
        print("Vulnerability table populated")

    # gets the date the report was made
    report_date = date.today()
    report_date = report_date.strftime("%Y-%m-%d")

    # still need to get the contract name from the contract
    contract_name = 'Sample.sol'

    # Insert report into the 'reports' table
    cursor.execute(
        f"INSERT INTO Reports (contract_name, audit_date) VALUES ('{contract_name}', '{report_date}')"
    )
    print("Report table populated")
    vulnerability_id_list = []
    for vulnerabilitie_name in vulnerabilities:
        cursor.execute(
            f"SELECT vulnerability_id FROM Vulnerabilities WHERE vulnerability_name = '{vulnerabilitie_name}'")
        vulnerabilitieID = cursor.fetchone()[0]
        vulnerability_id_list.append(vulnerabilitieID)

    cursor.execute("SELECT MAX(report_id) FROM reports")
    report_number = cursor.fetchone()[0]
    # insert report vulnerability into report vulnerabilities table
    for vulnerability in vulnerability_id_list:
        query = "INSERT INTO ReportVulnerabilities (report_id, vulnerability_id) VALUES (%s, %s)"
        data = (report_number, vulnerability)
        cursor.execute(query, data)

    # Commit changes and close the cursor and connection
    conn.commit()
    cursor.close()
    conn.close()

    print("Vulnerabilities inserted into the database.")

except mysql.connector.Error as err:
    print(f"Error: {err}")
except Exception as e:
    print(f"Error: {e}")
