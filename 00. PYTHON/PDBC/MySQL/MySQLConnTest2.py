#This Program Demonstrates How to get connection from MySQL
#MySQLConnTest2.py
import mysql.connector
try:
    con=mysql.connector.connect(host="127.0.0.1",
                                user="root",
                                passwd="root")
    print("Type of con=",type(con))
    print("Python Program Got Connection from MySQL")
except mysql.connector.DatabaseError as db:
    print("Problem with MySQL: ",db)