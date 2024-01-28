#!/usr/bin/python3
"""script that lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa"""
import MySQLdb
import sys


if __name__ == '__main__':
    args = sys.argv

    connection = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=args[1],
        password=args[2],
        database=args[3]
    )
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id")
    query_rows = cursor.fetchall()
    for row in query_rows:
        print(row)

    connection.commit()
    cursor.close()
    connection.close()
