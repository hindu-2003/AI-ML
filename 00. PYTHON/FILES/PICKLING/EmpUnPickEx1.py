#Program for Reading the Records from the File (emp.data) where It contains Employee Records
#EmpUnPickEx1.py
import pickle
with open("emp.data","rb") as fp:
		print("*************************************************")
		while(True):
			try:
				record=pickle.load(fp)
				for val in record:
					print("{}".format(val),end="\t")
				print()
			except EOFError:
				print("*************************************************")
				break
	