#EmpPickUnPickDemo.py<---Main Program
from EmpPickUnPickMenu import menu
from EmpPickEx2 import saverecord
from EmpUnPickEx2 import readrecord
while(True):
	try:
		menu()
		ch=int(input("Enter Ur Choice:"))
		match(ch):
			case 1:
				saverecord()
			case 2:
				readrecord()
			case 3:
				print("Thx for Using Program")
				break
			case _:
				print("Ur Selection of Operation is wrong--try again")
	except ValueError:
		print("Don't Enter alnums,str,symbols and floats for Choice of Operation--enter int values")