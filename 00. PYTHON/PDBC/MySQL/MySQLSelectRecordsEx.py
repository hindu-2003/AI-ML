#Program for Reading the Records from Employee Table--fetchall()
#MySQLSelectRecordEx.py
import mysql.connector
def  selectrecords():
	try:
		con=mysql.connector.connect(host="localhost",
										  user="root",
										  passwd="root",
										  database="6pmbatch")
		cur=con.cursor()
		sq="select * from employee order by sal desc"
		cur.execute(sq)
		#get the records
		print("*"*50)
		records=cur.fetchall()
		for record in records:
			for val in record:
				print(val,end="\t")
			print()
		print("*"*50)
	except mysql.connector.DatabaseError as db:
		print("Problem in MySQL Data Base:",db)

#Main Program
selectrecords()