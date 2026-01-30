#Program for Creating Two Sub Threads for generating Odd and Even Numbers within the range
#OddEvenThreadsFunEx1.py
import threading,time
def  odd(n):
	if(n<=0):
		print("{}-->{} is Invalid Input".format(threading.current_thread().name,n))
	else:
		for val in range(1,n+1,2):
			print("{}--->Odd Number:{}".format(threading.current_thread().name,val))
			time.sleep(1)
def  even(n):
	if(n<=0):
		print("{}-->{} is Invalid Input".format(threading.current_thread().name,n))
	else:
		for val in range(2,n+1,2):
			print("{}--->Even Number:{}".format(threading.current_thread().name,val))
			time.sleep(1)
#main program
t1=threading.Thread(target=odd,args=(10,))
t2=threading.Thread(target=even,args=(10,))
t1.start()
t2.start()
