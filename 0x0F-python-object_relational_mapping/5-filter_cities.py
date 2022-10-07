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
    cur.execute("SELECT cities.name"
                " FROM states JOIN cities"
                " ON cities.state_id = states.id"
                " WHERE states.name = '{}'"
                "ORDER BY cities.id;".format(argv[4]))
    m = cur.fetchall()
    cur.close()
    db.close()
    m = (list(map(str, [i[0] for i in m])))
    print(", ".join(m))
