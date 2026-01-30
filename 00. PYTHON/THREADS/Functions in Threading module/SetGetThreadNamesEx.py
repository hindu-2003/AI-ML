#Program for demonstrating set and get the thread names
#SetGetThreadNamesEx.py
import threading
def welcome():
	print("\tLine-5-->welcome() executed by:",threading.current_thread().name)

#main program
print("------------------------------------------------------------------")
print("Line-9: Program Execution Started by :",threading.current_thread().name)
print("------------------------------------------------------------------")
t1=threading.Thread(target=welcome)# here t1 is object name and called Sub Thread
#Here the Default name to the sub thread is Thread-1
#print("In Main Program Sub Thread name=", t1.getName()) # Thread-1---Not recommended to use
print("In Main Program Sub Thread name=", t1.name)
#t1.setName("RS") ----  Not recommended to use
t1.name="RS" #Setting the Name to sub thread
print("In Main Program Sub Thread name=", t1.name)
t1.start()
print("------------------------------------------------------------------")
