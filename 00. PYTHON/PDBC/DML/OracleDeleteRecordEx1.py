#Program for Deleting a Record
#OracleDeleteRecordEx1.py
import oracledb as orc
def deleterecord():
	try:
		con=orc.connect("system/tiger@127.0.0.1/orcl")
		cur=con.cursor()
		dq="delete from employee where eno=100"
		cur.execute(dq)
		con.commit()
		if(cur.rowcount>0):
			print("{} Record Deleted From Oracle DB".format(cur.rowcount))
		else:
			print("Emp Number does not Exist")
	except orc.DatabaseError as db:
			print("Problem in Oracle DB:",db)

#Main Program
deleterecord() # Function Call