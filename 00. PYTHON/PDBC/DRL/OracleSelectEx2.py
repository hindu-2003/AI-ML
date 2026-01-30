#Program for Reading the Records from Employee Table--fetchmany()
#OracleSelectEx2.py
import oracledb as orc
def  selectrecords():
	try:
		con=orc.connect("system/tiger@localhost/orcl")
		cur=con.cursor()
		sq="select * from employee"
		cur.execute(sq)
		#get the records
		print("*"*50)
		records=cur.fetchmany(6)
		for record in records:
			for val in record:
				print(val,end="\t")
			print()
		print("*"*50)
	except orc.DatabaseError as db:
		print("Problem in Oracle Data Base:",db)

#Main Program
selectrecords()