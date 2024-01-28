#!/usr/bin/python3
"""Script that takes in the name of a state as an argument and
lists all cities of that state, using the database hbtn_0e_4_usa
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
    # cursor.execute("SELECT * FROM cities")
    # cursor.execute("DELETE FROM cities WHERE id > 15")
    cursor.execute("""SELECT cities.name FROM cities
                      JOIN states ON cities.state_id = states.id
                      WHERE states.name = %s
                      ORDER BY cities.id ASC""", (args[4],))
    query_rows = cursor.fetchall()
    for i, row in enumerate(query_rows):
        print(*row, end=', ' if i < len(query_rows) - 1 else '\n')

    connection.commit()
    cursor.close()
    connection.close()
