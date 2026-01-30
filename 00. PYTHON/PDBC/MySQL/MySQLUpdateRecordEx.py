#Program for Updating a Record
#MySQLUpdateRecordEx.py
import mysql.connector
def updaterecord():
	while(True):
		try:
			con=mysql.connector.connect(host="localhost",
										  user="root",
										  passwd="root",
										  database="6pmbatch")
			cur=con.cursor()
			#accept empno,emp new sal and emp new comp name
			empno=int(input("Enter Employee Number for Updating emp sal and comp name:"))
			empsal=float(input("Enter Employee New Salary:"))
			cmpname=input("Enter Employee New Comp Name:")
			uq="update employee set sal=%f,compname='%s' where eno=%d"
			cur.execute(uq %(empsal,cmpname,empno))
			con.commit()
			if(cur.rowcount>0):
				print("{} Record Updated in MySQL DB".format(cur.rowcount))
			else:
				print("Emp Number does not Exist")
			print("-"*50)
			ch=input("Do u want to Update Another Record(yes/no):")
			if(ch.lower()=="no"):
				print("Thx for using this Program")
				break
		except mysql.connector.DatabaseError as db:
					print("Problem in MySQL DB:",db)
		except ValueError:
					print("Don't Enter Alnums,strs and symbols for empno and Sal")

#Main Program
updaterecord() # Function Call