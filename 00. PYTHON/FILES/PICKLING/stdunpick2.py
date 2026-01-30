#stdunpick2.py
#Student data writing to file

import pickle
def reads():
	with open("stud.data","rb")as fp:
		while(21):
			try:
				record = pickle.load(fp)
				print(record)
			except EOFError:
				print("*"*50)
				break
			
	
	
		