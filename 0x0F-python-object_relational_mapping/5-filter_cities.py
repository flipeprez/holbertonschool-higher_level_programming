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
    cursor.execute("SELECT\
            cities.name\
            FROM cities\
            JOIN states ON cities.state_id = states.id \
            WHERE states.name=(%s)\
            ORDER BY states.id", [name_searched])
    
    rows = cursor.fetchall()
    cty =''
    for row in rows:
        for col in row:
            cty += (col) + ', '
    print(cty[:-2])

    cursor.close()
    db.close()

if __name__ == "__main__":
    fsysargv0 = sys.argv[0]
    username = sys.argv[1]
    password = sys.argv[2]
    my_db = sys.argv[3]
    name_searched = sys.argv[4]
    GetAllStates(username, password, my_db, name_searched)
