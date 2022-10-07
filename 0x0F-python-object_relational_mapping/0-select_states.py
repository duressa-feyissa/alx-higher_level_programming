#!/usr/bin/python3
import MySQLdb
from sys import argv


if __name__ == "__main__":
    host = 'localhost'
    port = 3306
    db = MySQLdb.connect(host=host, user=argv[1], passwd=argv[2],
                         db=argv[3], port=port)
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id;")
    m = cursor.fetchall()
    cur.close()
    db.close()
    for i in m:
        print(i)
