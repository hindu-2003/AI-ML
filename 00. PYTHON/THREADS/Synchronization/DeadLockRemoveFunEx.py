#Program for Demonstrating Dead Lock Occurence
#DeadLockRemoveFunEx.py
import threading,time
def  multable(n):
	#Step-2----Get the Lock
	L.acquire()
	if(n<=0):
		print("{}--->{} is Invalid Input".format(threading.current_thread().name))
	else:
		print("------------------------------------------------")
		print("{} --->Mul table for :{}".format(threading.current_thread().name,n))
		print("------------------------------------------------")
		for i in range(1,11):
			print("{}---> {} x {}={}".format(threading.current_thread().name,n, i,n*i))
			time.sleep(0.00625)
		print("------------------------------------------------")
	#Step-3----Release the Lock	
	L.release()
	
#Main Program
#Step-1 Create an object of Lock
L=threading.Lock()
#create sub threads
t1=threading.Thread(target=multable,args=(16,))
t2=threading.Thread(target=multable,args=(19,))
t3=threading.Thread(target=multable,args=(6,))
t4=threading.Thread(target=multable,args=(9,))
#Dispatch the sub threads
t1.start()
t2.start()
t3.start()
t4.start()
