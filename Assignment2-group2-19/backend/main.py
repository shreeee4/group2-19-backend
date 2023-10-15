# Scott Lee 103994562
from fastapi import FastAPI, HTTPException, File, UploadFile, Path
import os
import re
import mysql.connector
from process_slither import process_vulnerabilities
from fastapi.responses import RedirectResponse
from fastapi.responses import JSONResponse
# assuming initialize_database is defined in insert_sql.py
from insert_sql import insert_vulnerabilities_to_db, initialize_database
# Needed to configure CORS on your FastAPI server to allow requests from the frontend domain or origin.
from fastapi.middleware.cors import CORSMiddleware
import mysql.connector  # Import the MySQL connector library

app = FastAPI()

db_config = {
    "host": "localhost",
    "user": "root",
    "password": "root",
    "database": "mypythondb"
}

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def startup_event():
    # Initialize your database here
    initialize_database()


# In your main.py (API file)

@app.get("/reports/{report_id}")
async def get_report_details(report_id: int):
    db_config = {
        "host": "localhost",
        "user": "root",
        "password": "root",
        "database": "mypythondb"
    }

    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)

        # Fetching related vulnerabilities using JOIN clauses
        cursor.execute("""
            SELECT v.* 
            FROM Report r
            JOIN ReportVulnerabilities rv ON r.report_id = rv.report_id
            JOIN Vulnerabilities v ON rv.vulnerability_id = v.vulnerability_id
            WHERE r.report_id = %s
        """, (report_id,))

        vulnerabilities = cursor.fetchall()
        if not vulnerabilities:
            return {"error": "No vulnerabilities found for the given report."}

        cursor.close()
        conn.close()

        return {"report_id": report_id, "vulnerabilities": vulnerabilities}

    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return {"error": "Database error"}

    except Exception as e:
        print(f"Error: {e}")
        return {"error": "Server error"}


@app.post("/audit/")
async def create_audit(file: UploadFile = File(...)):
    # Ensure the file is a .sol file
    file_ext = os.path.splitext(file.filename)[1]
    if file_ext != '.sol':
        raise HTTPException(
            status_code=400, detail="Invalid file type. Please upload a .sol file.")

    # Save the uploaded file
    file_location = f"uploaded_contracts/{file.filename}"
    with open(file_location, "wb+") as file_object:
        file_object.write(file.file.read())

    # Process vulnerabilities using Slither (process_slither module)
    vulnerabilities = process_vulnerabilities(file_location)
    if not vulnerabilities:
        raise HTTPException(
            status_code=500, detail="Error in processing vulnerabilities.")

    # Insert vulnerabilities to the database (insert_sql module)
    is_inserted = insert_vulnerabilities_to_db(vulnerabilities)
    if not is_inserted:
        raise HTTPException(
            status_code=500, detail="Error in inserting vulnerabilities to database.")
    #report_id = fetch_report_id_from_database()
    # return RedirectResponse(f"/reports/{report_id}")
