#Program for Demonstrating current_thread()
#CurrentThreadEx.py
import threading
t=threading.current_thread()
print("Default Thread information=",t)
print("default thread name=",t.name)
print("-------------OR----------------------")
print("Default Thread Name=",threading.current_thread().name)