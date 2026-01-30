#Program for altering employee table column sizes
#OracleAlterwithModify.py
import oracledb as orc
def alterwithmodify():
    try:
        con=orc.connect("system/tiger@localhost/orcl") # Step-2
        cur=con.cursor() # Step-3
        #Step-4
        aq="alter table employee modify(eno number(3),name varchar2(15))"
        cur.execute(aq)
        #step-5
        print("Table altered Sucessfully in Oracle")
    except orc.DatabaseError as db:
        print("Problem in Oracle in DB:",db)

#Main program
alterwithmodify()