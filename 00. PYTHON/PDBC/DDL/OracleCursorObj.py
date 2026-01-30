#Program for Demonstrating How create cursor object
#OracleCursorObj.py
import oracledb as orc
def getcursor():
    try:
        con=orc.connect("system/tiger@localhost/orcl") # Step-2
        print("type of con=",type(con))
        print('Python Prog Got Connection from Oracle DB')
        print("---------------------------------------")
        cur=con.cursor() # Step-3
        print("type of cur=",type(cur))
        print("Python Prog Created Cursor Object")
        print("---------------------------------------")
    except orc.DatabaseError as db:
        print("Problem in Oracle:",db)
#Main Program
getcursor()