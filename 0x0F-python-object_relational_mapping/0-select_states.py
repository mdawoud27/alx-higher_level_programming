#!/usr/bin/python3
"""script that lists all states from the database hbtn_0e_0_usa"""
import MySQLdb
import sys


if __name__ == '__main__':
    argvs = sys.argv

    connection = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argvs[1],
        password=argvs[2],
        database=argvs[3]
    )

    cursor = connection.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    query_rows = cursor.fetchall()

    for row in query_rows:
        print(row)

    cursor.close()
    connection.close()
