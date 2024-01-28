#!/usr/bin/python3
"""script that takes in arguments and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument. But this time, write one
that is safe from MySQL injections!
"""
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
    query = """SELECT * FROM states
               WHERE name LIKE BINARY %s
               ORDER BY id"""
    data = (args[4], )
    cursor.execute(query, data)

    query_rows = cursor.fetchall()
    for row in query_rows:
        print(row)

    cursor.close()
    connection.close()
