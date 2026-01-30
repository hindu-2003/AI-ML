#Program for Showing Default Thread Present in Python Program
#DefaultThreadEx.py
import threading
tname=threading.current_thread().name
print("Default Thread Name=",tname)
noth=threading.active_count()
print("Default Number of threads in Python Program=",noth)