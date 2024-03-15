#!/usr/bin/python3
"""
A script that lists all states from the database hbtn_0e_0_usa.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Connect to the MySQL server
    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=db_name)
    
    # Create a cursor object to execute SQL queries
    cursor = db.cursor()
    
    # Execute the SQL query to get the states sorted by id
    cursor.execute("SELECT * FROM states ORDER BY id ASC;")
    
    # Fetch and print all the results
    for row in cursor.fetchall():
        print(row)
    
    # Close the cursor and the connection
    cursor.close()
    db.close()