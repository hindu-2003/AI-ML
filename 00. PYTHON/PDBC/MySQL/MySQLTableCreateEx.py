#Program for Creating Table in MySQL
#MySQLTableCreateEx.py
import mysql.connector
def createtable():
    try:
        con = mysql.connector.connect(host="127.0.0.1",
                                      user="root",
                                      passwd="root",
                                      database="6pmbatch")
        cur = con.cursor()
        #Define Query and execute
        tq="create table employee(eno int primary key, name varchar(10) not null, sal real not null,compname varchar(10) not null)"
        cur.execute(tq)
        print("Table Created in MYSQL-----verify")
    except mysql.connector.DatabaseError as db:
        print("Problem with MySQL: ", db)
#Main Program
createtable()