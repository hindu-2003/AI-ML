#unpickling the data
import pickle
def readrecord():
	with open("Emp.txt","rb") as fp:
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

readrecord()