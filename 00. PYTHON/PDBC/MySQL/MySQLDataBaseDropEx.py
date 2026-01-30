#Program for Creating Database in MYSQL
#MySQLDataBaseDropEx.py
import mysql.connector
def dropdatabase():
    try:
        con = mysql.connector.connect(host="127.0.0.1",
                                      user="root",
                                      passwd="root")
        cur = con.cursor()
        #Define Query and execute
        dd="drop database KVR"
        cur.execute(dd)
        print("Data Base Removed from MySQL--verify")
    except mysql.connector.DatabaseError as db:
        print("Problem with MySQL: ", db)
#Main Program
dropdatabase()