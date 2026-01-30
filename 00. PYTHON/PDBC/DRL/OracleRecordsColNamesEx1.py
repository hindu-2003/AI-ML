#Probgram for Demonstrating Meta-data
#Here Mata-Data= Data About Data, here Data Represents Records and "about Data" represents Col Names, Col Names DB Data type...etc
#OracleRecordsColNamesEx1.py
import oracledb as orc
def  selectmetadata():
	try:
		con=orc.connect("system/tiger@localhost/orcl")
		cur=con.cursor()
		sq="select * from employee order by sal desc"
		cur.execute(sq)
		#get metedata
		metadata=cur.description  # Here description is pre-defined attribute present in cur object and it gives meta data
		print('-'*50)
		for colinfo in metadata:
			print(colinfo[0],end="\t")
		print()
		print('-'*50)
		records=cur.fetchall()
		for record in records:
			for val in record:
				print(val,end="\t")
			print()
		print('-'*50)
	except orc.DatabaseError as db:
		print("Problem in Oracle Data Base:",db)

#Main Program
selectmetadata()