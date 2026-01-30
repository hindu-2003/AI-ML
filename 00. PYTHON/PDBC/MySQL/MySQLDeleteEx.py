#Program for Deleting a Record
#MySQLDeleteRecordEx.py
import mysql.connector
def deleterecord():
	while(True):
		try:
			con = mysql.connector.connect(host="localhost",
										  user="root",
										  passwd="root",
										  database="6pmbatch")
			cur=con.cursor()
			#accept employee Number from Key board
			empno=int(input("Enter Employee Number:"))
			dq="delete from employee where eno=%d"
			cur.execute(dq %empno)
			con.commit()
			if(cur.rowcount>0):
				print("{} Record Deleted From MySQL DB".format(cur.rowcount))
			else:
				print("Emp Number does not Exist")
			print("-"*50)
			ch=input("Do u want to Delete Another Record(yes/no):")
			if(ch.lower()=="no"):
				print("Thx for using this Program")
				break
		except mysql.connector.DatabaseError as db:
				print("Problem in MySQL DB:",db)
		except ValueError:
			print("Don't Enter Alnums,strs and symbols for empno")

#Main Program
deleterecord() # Function Call