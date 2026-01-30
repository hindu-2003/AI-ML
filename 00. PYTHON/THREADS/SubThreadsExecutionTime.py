#Program for Showing Internal Flow of Main Thread only  with Execution Time
#SubThreadsExecutionTime.py
import threading,time
def  squares(lst):
	for val in lst:
		print("{}---square({})={}".format(threading.current_thread().name,val,val**2))
		time.sleep(1)
	
def cubes(lst):
	for val in lst:
		print("{}---cube({})={}".format(threading.current_thread().name,val,val**3))
		time.sleep(1)

#Main Program
bt=time.time()
print("------------------------------------------------------------------")
print("Program Execution Started by :",threading.current_thread().name)
print("------------------------------------------------------------------")
lst=[12,4,5,16,-6,17,19,4,13,45]
t1=threading.Thread(target=squares, args=(lst,))
t1.name="Hemnath"
print("------------------------------------------------------------------")
t2=threading.Thread(target=cubes,args=(lst,))
t2.name="Rajneeth"
#dispatch the Sub Threads
t1.start()
t2.start()
t1.join()
t2.join()
et=time.time()
print("Execution of the Program with  with Sub threads:",(et-bt))
