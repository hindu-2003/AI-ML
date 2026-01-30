#Program for Demonstrating Dead Lock Occurence
#DeadLockRemoveOopEx.py
import threading,time
class MulTable:
	def  table(self,n):
		L.acquire()
		if(n<=0):
			print("{}--->{} is Invalid Input".format(threading.current_thread().name,n))
		else:
			print("------------------------------------------------")
			print("{} --->Mul table for :{}".format(threading.current_thread().name,n))
			print("------------------------------------------------")
			for i in range(1,11):
				print("{}---> {} x {}={}".format(threading.current_thread().name,n, i,n*i))
				time.sleep(0.25)
			print("------------------------------------------------")
		L.release()
	
#Main Program
L=threading.Lock()
t1=threading.Thread(target=MulTable().table,args=(16,))
t2=threading.Thread(target=MulTable().table,args=(-19,))
t3=threading.Thread(target=MulTable().table,args=(6,))
t4=threading.Thread(target=MulTable().table,args=(-9,))
#Dispatch the sub threads
t1.start()
t2.start()
t3.start()
t4.start()
