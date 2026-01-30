#Program for Showing Internal Flow of Main Thread with Sub Threads
#SubThreadFlowEx.py
import threading
def welcome():
	print("\tLine-4-->welcome() executed by:",threading.current_thread().name)

def hello():
	print("\tLine-7-->hello() executed by:",threading.current_thread().name)

def hi(val):
	print("\tLine-10-->hi() ,{} executed by:{}".format(val,threading.current_thread().name))

#main program
print("------------------------------------------------------------------")
print("Line-13: Program Execution Started by :",threading.current_thread().name)
print("------------------------------------------------------------------")
t1=threading.Thread(target=welcome)# here t1 is sub thread object whose name is Thread-0
t1.name="RS"
t2=threading.Thread(target=hello) # here t2 is sub thread object whose name is Thread-1
t2.name="TR"
t3=threading.Thread(target=hi,args=("Rossum",) )# here t3 is sub thread object whose name is Thread-2
t3.name="DR"
#dispatch the sub threads to the target functions
t1.start()
t2.start()
t3.start()
t1.join()
t2.join()
t3.join()
print("------------------------------------------------------------------")
print("Line-20: Program Execution Ended by :",threading.current_thread().name)
print("------------------------------------------------------------------")