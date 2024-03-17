#!/usr/bin/python3
"""
A script that takes in an argument and displays all values in the states
table of the database hbtn_0e_0_usa where name matches the argument.
"""
import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name_searched = sys.argv[4]

    # Connect to the MySQL server
    db = MySQLdb.connect(host="localhost", user=username, passwd=password, db=db_name, port=3306)
    cursor = db.cursor()

    # Construct the query with the user input
    query = "SELECT * FROM states WHERE name LIKE %s ORDER BY id ASC"
    cursor.execute(query, (state_name_searched,))

    # Fetch and display the results
    for row in cursor.fetchall():
        if row[1] == state_name_searched:
            print(row)

    cursor.close()
    db.close()