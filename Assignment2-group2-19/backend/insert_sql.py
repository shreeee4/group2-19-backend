import mysql.connector
import random
import json
from datetime import date
from process_slither import process_vulnerabilities
from database import *

# gets Database connection configuration and table configuration from database.py
db_config = db_config_statements()
structure = database_structure()
vulnerabilitiy_statements = valnrabilaties_insert()

# Open the file and read the list of references (vulnerabilities)
vulnerabilitie_names = process_vulnerabilities()

try:

    # Establish a connection to the MySQL server
    conn = mysql.connector.connect(**db_config)

    # Create a cursor object
    cursor = conn.cursor()

    # Check if all the tables exist, create it if not
    cursor.execute(structure)

    # check if the Vulnerabilities table is empty, fill with list of Vulnerabilities if it is
    cursor.execute("SELECT COUNT(*) FROM Vulnerabilities")
    Vulnerabilitiy_amount = cursor.fetchone()[0]
    if Vulnerabilitiy_amount == 0:
        cursor.execute(vulnerabilitiy_statements)

    #checks the database to get the latest report number(if there are none sets it to 1000) and adds 1 to it to create the next report number
    cursor.execute("SELECT MAX(report_number) FROM reports")
    max_report_number = cursor.fetchone()[0]
    if max_report_number is None:
        report_number = 1000
    else:
        report_number = max_report_number + 1

    # gets the date the report was made(today)
    report_date= date.today()
    report_date = report_date.strftime("%d/%m/%Y")
    
    #still need to get the contract name from the contract
    contract_name =''
    
    # inserts the report into the 'Reports' table 
    cursor.execute(f"INSERT INTO Reports (report_number, vulnerability_id) VALUES ({report_number}, {contract_name}, {report_date})")
    vulnerabilities = []
    for vulnerabilitie_name in vulnerabilitie_names:
        cursor.execute(f"SELECT vulnerability_id FROM Vulnerabilities WHERE vulnerability_name = {vulnerabilitie_name}")
        vulnerabilitieID = cursor.fetchone()[0]
        vulnerabilities.append(vulnerabilitieID)
    
    # Insert the report vulnerabilitiy connections into the 'ReportVulnerabilities' table
    for vulnerability in vulnerabilities:
        query = "INSERT INTO ReportVulnerabilities (report_number, vulnerability_id) VALUES (%s, %s)"
        data = (report_number, vulnerability)
        cursor.execute(query, data)

    # Commit changes and close the cursor and connection
    conn.commit()
    cursor.close()
    conn.close()

    print("Vulnerabilities inserted into the database.")

except mysql.connector.Error as err:
    print(f"Error: {err}")
