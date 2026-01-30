#Program for Inserting a Record
#OracleRecordInsertEx1.py
import oracledb as orc
def recordinsert():
	try:
		con=orc.connect("system/tiger@127.0.0.1/orcl")
		cur=con.cursor()
		#design the DML Query and Insert
		iq="insert into employee values(125,'Uday',1.6,'TCS')"
		cur.execute(iq)
		con.commit()
		print("Record Inserted in Oracle Sucessfully")
	except orc.DatabaseError as db:
		print("Problem in Oracle DB:",db)
#Main Program
recordinsert() # Function call