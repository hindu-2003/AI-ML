#Program for Demonstrating finding number of active threads by using active_count()
#ActiveCountThreadEx.py
import threading
print("Name of Active Thread=",threading.current_thread().name)
print("Number of Threads in Python=",threading.active_count())