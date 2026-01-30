#Program for Inserting a Record
#OracleRecordInsertEx3.py
import oracledb as orc
def recordinsert():
	while(True):
		try:
			con=orc.connect("system/tiger@127.0.0.1/orcl")
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
			print("{} Record Inserted in Oracle Sucessfully".format(cur.rowcount))
			print("-"*50)
			ch=input("Do u want to insert Another Record(yes/no):")
			if(ch.lower()=="no"):
				print("Thx for using this Program")
				break
		except orc.DatabaseError as db:
			print("Problem in Oracle DB:",db)
		except ValueError:
			print("Don't Enter Alnums,strs and symbols for empno and sal")
#Main Program
recordinsert() # Function call