#Program for Removing the Table from Oracle Database
#OracleDynamicDropTable.py
import oracledb as orc
def droptablename():
    try:
        con=orc.connect("system/tiger@localhost/orcl") # Step-2
        cur=con.cursor() # Step-3
        #Step-4
        cur.execute("drop table %s" %input("Enter the Table Name to drop:"))
        #step-5
        print("Table Droped Sucessfully in Oracle")
    except orc.DatabaseError as db:
        print("Problem in Oracle in DB:",db)

#Main Program
droptablename()