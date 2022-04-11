#!/usr/bin/python3
'''
comment
'''
import sys
import MySQLdb

def GetAllStates (username, password, my_db):
    '''list  cities'''
    db = MySQLdb.connect(host = "localhost",
                         user = username,
                         passwd = password,
                         db = my_db,
                         port = 3306)

    cursor = db.cursor()
    sql = "SELECT \
        cities.id, cities.name, states.name \
        FROM cities \
        JOIN states ON cities.state_id = states.id\
        ORDER BY cities.id"
    cursor.execute(sql)
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
