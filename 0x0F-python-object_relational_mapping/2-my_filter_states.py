#!/usr/bin/python3
''' script lists all states from the db'''

import MySQLdb
from sys import argv


if __name__ == "__main__":
    host = 'localhost'
    port = 3306
    db = MySQLdb.connect(host=host, user=argv[1], passwd=argv[2],
                         db=argv[3], port=port)
    cur = db.cursor()
    cur.execute("""SELECT * FROM states WHERE name LIKE BINARY '{}'
                ORDER BY id;""".format(argv[4]))
    m = cur.fetchall()
    cur.close()
    db.close()
    for i in m:
        print(i)
