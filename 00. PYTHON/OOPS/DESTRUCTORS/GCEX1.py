#GCEX1.py
import gc
print("Is GC Running=",gc.isenabled())
print("Program Execution Started")
a=10
b=20
v=a+b
print("Val of a=",a)
gc.disable()
print("Val of b=",b)
print("\tIs GC Running after disbale()=",gc.isenabled())
print("sum=",v)
gc.enable()
print("\tIs GC Running after enable()=",gc.isenabled())
print("Program Execution Ended")
