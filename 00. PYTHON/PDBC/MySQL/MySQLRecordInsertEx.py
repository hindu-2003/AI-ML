#Program for Inserting a Record
#MySQLRecordInsertEx.py
import mysql.connector
def recordinsert():
	while(True):
		try:
			con=mysql.connector.connect(host="localhost",
                                        user="root",
                                        passwd="root",
                                        database="6pmbatch")
			cur=con.cursor()
			#accept the employee values from KBD
			print("-"*50)
			empno=int(input("Enter Employee Number:"))
			empname=input("Enter Employee Name:")
			empsal=float(input("Enyer Employee Salary:"))
			cmpname=input("Enter Employee Comp Name:")
			print("-"*50)
			#design the DML Query and Insert
			iq="insert into employee values(%d,'%s',%f,'%s')"
			cur.execute(iq %(empno,empname,empsal,cmpname))
			#OR  cur.execute("insert into employee values(%d,'%s',%f,'%s')" %(empno,empname,empsal,cmpname))
			con.commit()
			print("{} Record Inserted in MySQL Sucessfully".format(cur.rowcount))
			print("-"*50)
			ch=input("Do u want to insert Another Record(yes/no):")
			if(ch.lower()=="no"):
				print("Thx for using this Program")
				break
		except mysql.connector.DatabaseError as db:
			print("Problem in MySQL DB:",db)
		except ValueError:
			print("Don't Enter Alnums,strs and symbols for empno and sal")
#Main Program
recordinsert() # Function call