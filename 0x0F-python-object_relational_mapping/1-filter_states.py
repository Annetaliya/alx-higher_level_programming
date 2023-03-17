#!/usr/bin/python3
""" a script that lists all states with a name starting with N"""

import MySQLdb
import sys

if __name__ == "__main__":
    mydb = MySQLdb.connect(
            host="localhost",
            user=sys.argv[1],
            password=sys.argv[2],
            port=3306,
            db=sys.argv[3]
            )

    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM states WHERE name LIKE 'N%'\
            ORDER BY states.id")
    rows = mycursor.fetchall()
    for row in rows:
        print(row)
    mycursor.close()
    mydb.close()
