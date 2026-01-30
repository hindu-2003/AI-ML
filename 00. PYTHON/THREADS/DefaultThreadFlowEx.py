#Program for Showing Internal Flow of Main Thread
#DefaultThreadFlowEx.py
import threading
def welcome():
	print("Line-4-->welcome() executed by:",threading.current_thread().name)

def hello():
	print("Line-7-->hello() executed by:",threading.current_thread().name)

def hi():
	print("Line-4-->hi() executed by:",threading.current_thread().name)

#main program
print("Line-13: Program Execution Started by :",threading.current_thread().name)
welcome()
print("Line-15")
hello()
print("Line-17")
hi()
print("Line-20: Program Execution Ended by :",threading.current_thread().name)