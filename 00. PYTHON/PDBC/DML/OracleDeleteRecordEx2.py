#Program for Deleting a Record
#OracleDeleteRecordEx2.py
import oracledb as orc
def deleterecord():
	while(True):
		try:
			con=orc.connect("system/tiger@127.0.0.1/orcl")
			cur=con.cursor()
			#accept employee Number from Key board
			empno=int(input("Enter Employee Number:"))
			dq="delete from employee where eno=%d"
			cur.execute(dq %empno)
			con.commit()
			if(cur.rowcount>0):
				print("{} Record Deleted From Oracle DB".format(cur.rowcount))
			else:
				print("Emp Number does not Exist")
			print("-"*50)
			ch=input("Do u want to Delete Another Record(yes/no):")
			if(ch.lower()=="no"):
				print("Thx for using this Program")
				break
		except orc.DatabaseError as db:
				print("Problem in Oracle DB:",db)
		except ValueError:
			print("Don't Enter Alnums,strs and symbols for empno")

#Main Program
deleterecord() # Function Call