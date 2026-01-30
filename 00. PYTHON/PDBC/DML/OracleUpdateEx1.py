#Program for Updating a Record
#OracleUpdateEx1.py
import oracledb as orc
def updaterecord():
	try:
		con=orc.connect("system/tiger@127.0.0.1/orcl")
		cur=con.cursor()
		uq="update employee set sal=6.7,compname='HCL' where eno=300"
		cur.execute(uq)
		con.commit()
		if(cur.rowcount>0):
			print("{} Record Updated in Oracle DB".format(cur.rowcount))
		else:
			print("Emp Number does not Exist")
	except orc.DatabaseError as db:
			print("Problem in Oracle DB:",db)

#Main Program
updaterecord() # Function Call