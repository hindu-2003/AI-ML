#Probgram for Demonstrating Meta-data
#Here Mata-Data= Data About Data, here Data Represents Records and "about Data" represents Col Names, Col Names DB Data type...etc
#MySQLSelectRecordColNamesEx.py
import mysql.connector
def  selectmetadata():
	try:
		con=mysql.connector.connect(host="localhost",
										  user="root",
										  passwd="root",
										  database="6pmbatch")
		cur=con.cursor()
		sq="select * from {}".format(input('Enter Table Name:'))
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
	except mysql.connector.DatabaseError as db:
		print("Table Does not Exist")

#Main Program
selectmetadata()