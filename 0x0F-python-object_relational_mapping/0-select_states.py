#!/usr/bin/python3
import MySQLdb
from sys import argv


db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
cursor = db.cursor()
cursor.execute("SELECT * FROM states ORDER BY id;")
m = cursor.fetchall()
for i in m:
    print(i)
