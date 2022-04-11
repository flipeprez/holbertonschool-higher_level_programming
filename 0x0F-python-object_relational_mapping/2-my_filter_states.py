#!/usr/bin/python3
'''
comment
'''
import sys
import MySQLdb

def GetAllStates (username, password, my_db, name_searched):
    '''list  states'''
    db = MySQLdb.connect(host = "localhost",
                         user = username,
                         passwd = password,
                         db = my_db,
                         port = 3306)

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name='{}'\
            ORDER BY id".format(name_searched))
    
    rows = cursor.fetchall()
    for row in rows:
        if (row[1] == name_searched):
            print(row)
    cursor.close()
    db.close()

if __name__ == "__main__":
    fsysargv0 = sys.argv[0]
    username = sys.argv[1]
    password = sys.argv[2]
    my_db = sys.argv[3]
    name_searched = sys.argv[4]
    GetAllStates(username, password, my_db, name_searched)
