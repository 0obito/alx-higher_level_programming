#!/usr/bin/python3
"""
this module takes in an argument and displays all values
in the states table of hbtn_0e_0_usa where name matches
the argument, and it's safe from SQL injections.
"""
import MySQLdb
import sys
if __name__ == "__main__":
    connection = MySQLdb.connect(host="localhost",
                                 port=3306, user=sys.argv[1],
                                 passwd=sys.argv[2],
                                 db=sys.argv[3])
    cursor = connection.cursor()
    sql_query = """SELECT * FROM states
                WHERE name = %s ORDER BY id ASC
                """
    cursor.execute(sql_query, (sys.argv[4],))
    many = cursor.fetchall()
    for one in many:
        print(one)
    cursor.close()
    connection.close()
