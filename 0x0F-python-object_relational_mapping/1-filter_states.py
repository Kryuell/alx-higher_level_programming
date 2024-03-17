#!/usr/bin/python3
"""
Script to list all states with names starting with 'N' from the
database hbtn_0e_0_usa.
"""
import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Connect to the database
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password, db=db_name)
    cursor = db.cursor()

    # Execute the query to find states starting with 'N'
    cursor.execute("SELECT * FROM states ORDER BY states.id ASC")

    for row in cursor.fetchall():
        print(row)

    cursor.close()
    db.close()
