#Program for Removing the Table from Oracle Database
#OracleDropTable.py
import oracledb as orc
def droptablename():
    try:
        con=orc.connect("system/tiger@localhost/orcl") # Step-2
        cur=con.cursor() # Step-3
        #Step-4
        dt="drop table student"
        cur.execute(dt)
        #step-5
        print("Table Droped Sucessfully in Oracle")
    except orc.DatabaseError as db:
        print("Problem in Oracle in DB:",db)

#Main Program'
droptablename()