#!/usr/bin/python3
""" A safe script that takes an argument and displays
all values in the states table
"""
import MySQLdb
from sys import argv


if __name__ == '__main__':
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=argv[1],
            passwd=argv[2],
            db=argv[3]
            )
    cursor = db.cursor()

    cursor.execute("SELECT * FROM states WHERE name LIKE \
            BINARY %(name)s ORDER BY states.id ASC", {'name': argv[4]})

    selected = cursor.fetchall()

    for select in selected:
        print(select)
