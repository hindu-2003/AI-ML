#Program for Reading Employee Values and Save them as Record in a file.
#EmpPickEx2.py<--File Name and Module Name
import pickle
def saverecord():
	with open("emp.data","ab") as fp:
		while(True):
			try:
				#accept the employee values from KBD
				print("-------------------------------------------------------")
				empno=int(input("Enter Employee Number:"))
				ename=input("Enter Employee Name:")
				sal=float(input("Enter Employee Salary:"))
				dsg=input("Enter Employee Designation:")
				print("-------------------------------------------------------")
				#create an empty list and place emp values 
				lst=list()
				lst.append(empno)
				lst.append(ename)
				lst.append(sal)
				lst.append(dsg)
				#Save OR Transfer lst data into the file
				pickle.dump(lst,fp)
				print("Employee Record Saved in File sucessfully:")
				print("-------------------------------------------------------")
				ch=input("Do u want to Insert Another Record(yes/no):")
				if(ch.lower()=="no"):
					print("Thx for using this program")
					break
			except ValueError:
				print("Don't enter alnums,strs and symbols for empno,sal")
