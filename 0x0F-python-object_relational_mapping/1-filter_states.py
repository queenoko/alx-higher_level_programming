#!/usr/bin/python3

"""
The script lists all states with
`name` starting with the letter `N`
from database `hbtn_0e_0_usa`.
"""

import MySQLdb as db
from sys import argv

"""
Accessing the database and getting the states
from database.
"""

if __name__ == '__main__':
    db_connect = db.connect(host="localhost", port=3306,
                            user=argv[1], passwd=argv[2], db=argv[3])
    db_cursor = db_connect.cursor()

    db_cursor.execute(
        "SELECT * FROM states WHERE name LIKE BINARY 'N%' \
                ORDER BY states.id ASC")

    rows_selected = db_cursor.fetchall()

    for row in rows_selected:
        print(row)
