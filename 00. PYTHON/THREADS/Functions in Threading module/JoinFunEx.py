#Program for Showing Importance of join()
#JoinFunEx.py
import threading,time
def  squares(lst):
	for val in lst:
		print("{}---square({})={}".format(threading.current_thread().name,val,val**2))
		time.sleep(1)
	
#Main Program
print("------------------------------------------------------------------")
print("Program Execution Started by :",threading.current_thread().name)
print("------------------------------------------------------------------")
lst=[12,4,5,16,-6,17,19,4,13,45]
t1=threading.Thread(target=squares, args=(lst,))
print('Execution Status of t1 before start()=',t1.is_alive())
print("Number of Active Threads before start=",threading.active_count()) # 1
t1.start()
print('Execution Status of t1 after start()=',t1.is_alive())
print("Number of Active Threads after start=",threading.active_count()) # 2
#make the sub threads to join with main Thread after completetion of execution
t1.join()
print("Number of Active Threads after join=",threading.active_count()) # 1
print("Program execution completed:",threading.current_thread().name)
