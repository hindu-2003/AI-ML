#Program for Demonstrating How to Create Cursor object
#MySQLCuserEx.py
import mysql.connector
try:
    con=mysql.connector.connect(host="127.0.0.1",
                                user="root",
                                passwd="root")
    print("Type of con=",type(con))
    print("Python Program Got Connection from MySQL")
    print("-------------------------------------------")
    cur=con.cursor()
    print("type of cur=",type(cur))
    print("Python Program created Cursor Object")
except mysql.connector.DatabaseError as db:
    print("Problem with MySQL: ",db)