#!/usr/bin/python3
"""
this module lists all states with a name
starting with N from the given database
"""
import MySQLdb
import sys
if __name__ == "__main__":
    connection = MySQLdb.connect(host="localhost",
                                 port=3306, user=sys.argv[1],
                                 passwd=sys.argv[2],
                                 db=sys.argv[3])
    cursor = connection.cursor()
    sql_query = "SELECT * FROM states \
                WHERE name LIKE BINARY 'N%' ORDER BY id ASC"
    cursor.execute(sql_query)
    many = cursor.fetchall()
    for one in many:
        print(one)
    cursor.close()
    connection.close()
