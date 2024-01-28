#!/usr/bin/python3
""""""
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
    query = """SELECT * FROM cities ORDER BY cities.id ASC"""
    cursor.execute(query)

    query_rows = cursor.fetchall()
    for row in query_rows:
        print(row)

    cursor.close()
    connection.close()
