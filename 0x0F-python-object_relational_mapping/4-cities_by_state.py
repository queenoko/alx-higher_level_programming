#!/usr/bin/python3
"""
The script that lists all cities from
database `hbtn_0e_4_usa`.
"""

import MySQLdb as db
from sys import argv

if __name__ == '__main__':
    """
    This Access the database to get cities
    from database.
    """

    db_connect = db.connect(host="localhost", port=3306,
                            user=argv[1], passwd=argv[2], db=argv[3])

    with db_connect.cursor() as db_cursor:
        db_cursor.execute("SELECT cities.id, cities.name, states.name \
                                FROM cities JOIN states ON cities.state_id \
                                = states.id ORDER BY cities.id ASC")
        rows_selected = db_cursor.fetchall()

    if rows_selected is not None:
        for rowSe in rows_selected:
            print(rowSe)
