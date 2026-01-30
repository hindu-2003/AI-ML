#Program for generating values from 1 to N-1 Values by using threads
#NumberGenOOPsEx1.py
import threading,time
class Numbers:
	def generate(self,n):
		if(n<=0):
			print("{}-->{} is Invalid Input".format(threading.current_thread().name,n))
		else:
			print("="*50)
			print("Numbers within:{}".format(n))
			print("="*50)
			for val in range(1,n+1):
				print("{}-->Value :{}".format(threading.current_thread().name,val))
				time.sleep(0.25)
			print("="*50)

#main Program
n=int(input("Enter How many Numbers u want to generate:"))
no=Numbers()
t1=threading.Thread(target=no.generate,args=(n,))
t1.start()
