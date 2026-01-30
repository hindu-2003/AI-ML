#Program for altering employee table by adding new Col Name
#OracleAlterwithAdd.py
import oracledb as orc
def alterwithAdd():
    try:
        con=orc.connect("system/tiger@localhost/orcl") # Step-2
        cur=con.cursor() # Step-3
        #Step-4
        aq="alter table employee add(compname varchar2(10) not null)"
        cur.execute(aq)
        #step-5
        print("Table altered Sucessfully in Oracle")
    except orc.DatabaseError as db:
        print("Problem in Oracle in DB:",db)

#Main program
alterwithAdd()