#Program for Showing Internal Flow of Main Thread only  with Execution Time
#MainThreadExecutionTime.py
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
squares(lst)
print("------------------------------------------------------------------")
cubes(lst)
print("------------------------------------------------------------------")
print("Program Execution Ended by :",threading.current_thread().name)
print("------------------------------------------------------------------")
et=time.time()
print("Execution of the Program with Only MainThread without Sub threads:",(et-bt))
