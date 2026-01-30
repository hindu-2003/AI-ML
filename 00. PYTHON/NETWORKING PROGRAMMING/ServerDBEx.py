#ServerDBEx.py
import socket
import oracledb as orc
s=socket.socket()
s.bind(("127.0.0.1",3600))
s.listen(20)
while(True):
	try:
		cs,ca=s.accept()
		#get employee Number from client
		eno=int(cs.recv(1024).decode())
		#PDBC Code
		con=orc.connect("system/tiger@localhost/orcl")
		cur=con.cursor()
		cur.execute("select * from employee where eno=%d" %eno)
		#get the records
		record=cur.fetchone()
		if(record!=None):
			s1="Employee Number:"+str(record[0])
			s2="Employee Name:"+str(record[1])
			s3="Employee Salary:"+str(record[2])
			s4="Employee Comp Name:"+str(record[3])
			res=s1+"\n"+s2+"\n"+s3+"\n"+s4
			cs.send(res.encode())
		else:
			cs.send("Employee Record does not Exist".encode())
	except orc.DatabaseError as db:
		cs.send(("Problem with Oracle db"+str(db)).encode())
	except ValueError:
		cs.send("Don't enter alnums,strs and symbols for eno".encode())