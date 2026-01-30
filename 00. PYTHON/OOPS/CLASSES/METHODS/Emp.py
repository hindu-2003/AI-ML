#Emp.py<---File Name and Module Name
class Employee:
    def readempdata(self):
        print('-'*50)
        self.eno=int(input("\tEnter Employee Number:"))
        self.ename=input("\tEnter Employee Name:")
        self.sal=float(input("\tEnter Employee Salary:"))