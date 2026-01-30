#Program for Demonstrating Dead Lock Occurence
#DeadLockRemoveOopEx1.py
import threading,time
class MulTable:
	@classmethod
	def  getLock(cls):
		cls.K=threading.Lock() # Here K is called an object of Lock Class
	def  table(self,n):
		MulTable.K.acquire()
		if(n<=0):
			print("{}--->{} is Invalid Input".format(threading.current_thread().name,n))
		else:
			print("------------------------------------------------")
			print("{} --->Mul table for :{}".format(threading.current_thread().name,n))
			print("------------------------------------------------")
			for i in range(1,11):
				print("{}---> {} x {}={}".format(threading.current_thread().name,n, i,n*i))
				time.sleep(0.000000000000025)
			print("------------------------------------------------")
		MulTable.K.release()
	
#Main Program
MulTable.getLock()
t1=threading.Thread(target=MulTable().table,args=(16,))
t2=threading.Thread(target=MulTable().table,args=(-19,))
t3=threading.Thread(target=MulTable().table,args=(6,))
t4=threading.Thread(target=MulTable().table,args=(-9,))
t5=threading.Thread(target=MulTable().table,args=(14,))
t6=threading.Thread(target=MulTable().table,args=(17,))
t7=threading.Thread(target=MulTable().table,args=(-16,))
t8=threading.Thread(target=MulTable().table,args=(25,))
#Dispatch the sub threads
t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()
t7.start()
t8.start()