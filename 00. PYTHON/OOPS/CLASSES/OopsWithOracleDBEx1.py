#Program for Reading Student Data from KBD and save them as Record in Student table 
#OopsWithOracleDBEx1.py
import oracledb as orc
class StudentWithOracleDB:
	def  getstudvals(self):
		print('----------------------------------------------------------')
		self.sno=int(input("Enter Student Number:"))
		self.name=input("Enter Student Name:")
		self.marks=float(input("Enter Student Marks:"))
		print('----------------------------------------------------------')
	def savestuddata(self):
		while(True):
			self.getstudvals()
			#Write the Python Code for Communicating with Oracle Database
			try:
				con=orc.connect("system/tiger@localhost/orcl")
				cur=con.cursor()
				cur.execute("insert into student values(%d,'%s',%f)" %(self.sno,self.name,self.marks ) )
				con.commit()
				print("{} Record Inserted".format(cur.rowcount))
				ch=input("Do u want to Insert Another Record(yes/no):")
				if(ch.lower()=="no"):
					print("Thx for using program")
					break
			except orc.DatabaseError as db:
				print("Problem on Oracle DB:",db)

#main Program
so=StudentWithOracleDB()
so.savestuddata()
