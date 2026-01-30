#Program for Creating Database in MYSQL
#MySQLDataBaseCreateEx.py
import mysql.connector
def createdatabase():
    try:
        con = mysql.connector.connect(host="127.0.0.1",
                                      user="root",
                                      passwd="root")
        cur = con.cursor()
        #Define Query and execute
        dc="create database KVR"
        cur.execute(dc)
        print("Data Base Created in MySQL--verify")
    except mysql.connector.DatabaseError as db:
        print("Problem with MySQL: ", db)
#Main Program
createdatabase()