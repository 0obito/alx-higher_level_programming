#!/usr/bin/python3
"""
takes in the name of a state as an argument
and lists all cities of that state, using the
database hbtn_0e_4_usa
"""
import MySQLdb
import sys

if __name__ == "__main__":
    connection = MySQLdb.connect(host="localhost",
                                 port=3306, user=sys.argv[1],
                                 passwd=sys.argv[2],
                                 db=sys.argv[3])
    cursor = connection.cursor()
    sql_query = """
                SELECT cities.name
                FROM states
                INNER JOIN cities ON states.id = cities.state_id
                WHERE states.name = %s
                ORDER BY cities.id ASC
                """
    cursor.execute(sql_query, (sys.argv[4],))
    rows = cursor.fetchall()
    print(", ".join([city[0] for city in rows]))
    cursor.close()
    connection.close()
