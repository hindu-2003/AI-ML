#Program for Creating a Table
#OracleCreateTableEx2.py
import oracledb as tcs # Step-1
def createtable():
    try:
        con=tcs.connect("system/tiger@localhost/orcl") # Step-2
        cur=con.cursor() # Step-3
        #Step-4
        tc=input("Enter Query for Creating a Table in Oracle-SQL:")
        cur.execute(tc)
        #step-5
        print("Table created Sucessfully in Oracle")
    except tcs.DatabaseError as db:
        print("Problem in Oracle in DB:",db)
#Main Program
createtable() # function Call