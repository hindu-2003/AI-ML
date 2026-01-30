#Program for generating values from 1 to N-1 Values by using threads
#NumberGenOOPsEx2.py
import threading,time
class Numbers:
	def __init__(self,n):
		self.n=n
	def generate(self):
		if(self.n<=0):
			print("{}-->{} is Invalid Input".format(threading.current_thread().name,self.n))
		else:
			print("="*50)
			print("Numbers within:{}".format(self.n))
			print("="*50)
			for val in range(1,self.n+1):
				print("{}-->Value :{}".format(threading.current_thread().name,val))
				time.sleep(0.25)
			print("="*50)

#main Program
n=int(input("Enter How many Numbers u want to generate:"))
no=Numbers(n) # Obejct Creation--Calls parametrized Constructor
t1=threading.Thread(target=no.generate)
t1.start()
