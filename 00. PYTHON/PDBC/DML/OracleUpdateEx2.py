#Program for Updating a Record
#OracleUpdateEx2.py
import oracledb as orc
def updaterecord():
	while(True):
		try:
			con=orc.connect("system/tiger@127.0.0.1/orcl")
			cur=con.cursor()
			#accept empno,emp new sal and emp new comp name
			empno=int(input("Enter Employee Number for Updating emp sal and comp name:"))
			empsal=float(input("Enter Employee New Salary:"))
			cmpname=input("Enter Employee New Comp Name:")
			uq="update employee set sal=%f,compname='%s' where eno=%d"
			cur.execute(uq %(empsal,cmpname,empno))
			con.commit()
			if(cur.rowcount>0):
				print("{} Record Updated in Oracle DB".format(cur.rowcount))
			else:
				print("Emp Number does not Exist")
			print("-"*50)
			ch=input("Do u want to Update Another Record(yes/no):")
			if(ch.lower()=="no"):
				print("Thx for using this Program")
				break
		except orc.DatabaseError as db:
					print("Problem in Oracle DB:",db)
		except ValueError:
					print("Don't Enter Alnums,strs and symbols for empno and Sal")

#Main Program
updaterecord() # Function Call