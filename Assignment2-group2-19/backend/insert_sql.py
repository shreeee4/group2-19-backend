import mysql.connector
from datetime import date
from process_slither import process_vulnerabilities
from database import *


def initialize_database():
    db_config = database_config()
    structure = database_structure()
    vulnerabilitiy_statements = valnrabilaties_insert()

    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        for create_table_statements in structure:
            cursor.execute(create_table_statements)

        cursor.execute("SELECT COUNT(*) FROM Vulnerabilities")
        Vulnerabilitiy_amount = cursor.fetchone()[0]
        if Vulnerabilitiy_amount == 0:
            for create_vulnerability_statement in vulnerabilitiy_statements:
                cursor.execute(create_vulnerability_statement)
                # commits the changes
        conn.commit()
        cursor.close()
        conn.close()

    except mysql.connector.Error as err:
        print(f"Database Initialization Error: {err}")
    except Exception as e:
        print(f"Database Initialization Error: {e}")


def insert_vulnerabilities_to_db(vulnerabilities):
    db_config = database_config()

    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        report_date = date.today().strftime("%Y-%m-%d")
        contract_name = 'Sample.sol'

        cursor.execute(
            f"INSERT INTO Reports (contract_name, audit_date) VALUES ('{contract_name}', '{report_date}')"
        )

        vulnerability_id_list = []
        for vulnerability_name in vulnerabilities:
            cursor.execute(
                f"SELECT vulnerability_id FROM Vulnerabilities WHERE vulnerability_name = '{vulnerability_name}'")
            vulnerability_id = cursor.fetchone()[0]
            vulnerability_id_list.append(vulnerability_id)

        cursor.execute("SELECT MAX(report_id) FROM reports")
        report_number = cursor.fetchone()[0]

        for vulnerability in vulnerability_id_list:
            query = "INSERT INTO ReportVulnerabilities (report_id, vulnerability_id) VALUES (%s, %s)"
            data = (report_number, vulnerability)
            cursor.execute(query, data)

        conn.commit()
        cursor.close()
        conn.close()

        return True  # Return True if vulnerabilities are inserted successfully

    except mysql.connector.Error as err:
        print(f"Vulnerability Insertion Error: {err}")
        return False  # Return False if an error occurs
    except Exception as e:
        print(f"Vulnerability Insertion Error: {e}")
        return False  # Return False if an error occurs
