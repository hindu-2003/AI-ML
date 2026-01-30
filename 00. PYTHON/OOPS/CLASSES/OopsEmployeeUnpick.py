#OopsEmployeeUnpick.py
import pickle
class EmployeeUnpick:
	def getemprecords(self):
		try:
			with open("emp.pick","rb") as fp:
				print("-----------------------------------------")
				while(True):
					try:
						record=pickle.load(fp)
						record.dispempvals()
					except EOFError:
						print("-----------------------------------------")
						break
		except FileNotFoundError:
			print("File Does not Exist")


#Main Program
eo=EmployeeUnpick()
eo.getemprecords()
