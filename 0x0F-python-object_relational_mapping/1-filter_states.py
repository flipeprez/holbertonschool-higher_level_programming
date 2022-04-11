#!/usr/bin/python3
'''
comment
'''
import sys
import MySQLdb

def GetAllStates (username, password, my_db):
    '''list  states'''
    db = MySQLdb.connect(host = "localhost",
                         user = username,
                         passwd = password,
                         db = my_db,
                         port = 3306)

    cursor = db.cursor()
    cursor.execute("SELECT * FROM `states` WHERE `name` REGEXP '^N' ORDER BY id")
    rows = cursor.fetchall()
    for row in rows:
        print (row)
    cursor.close()
    db.close()

if __name__ == "__main__":
    fsysargv0 = sys.argv
    username = sys.argv[1]
    password = sys.argv[2]
    my_db = sys.argv[3]
    GetAllStates(username, password, my_db)
