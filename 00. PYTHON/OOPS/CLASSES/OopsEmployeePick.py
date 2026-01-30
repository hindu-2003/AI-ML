#OopsEmployeePick.py
from OopsEmp import Employee
import pickle
class EmployeePick:
	def  saveempdata(self):
		while(True):
			print("--------------------------------------------------")
			eno=int(input("Enter Employee Number:"))
			ename=input("Enter Employee Name:")
			sal=float(input("Enter Employee Salary:"))
			print("--------------------------------------------------")
			with open("emp.pick","ab") as fp:
				eo=Employee()
				eo.getempvals(eno,ename,sal)
				#save eo object data into file
				pickle.dump(eo,fp)
				print("Employee Record saved in File sucessfully:")
				print("--------------------------------------------------")
				ch=input("Do u want to Insert Another Record(yes/no):")
				if(ch.lower()=="no"):
						print("Thx for using program")
						break



#Main Program
eo=EmployeePick()
eo.saveempdata()
