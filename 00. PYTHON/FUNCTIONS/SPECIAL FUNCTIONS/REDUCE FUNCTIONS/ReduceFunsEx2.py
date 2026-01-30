#Program for Finding Sum of List of Values by using reduce()
#ReduceFunsEx2.py
import functools as fc
def operation(k,v):
	return k+v

print("Enter List of Values Separated by Space:")
lst=[float(val) for val in input().split()]
res=fc.reduce(operation,lst)
print("Sum({})={}".format(lst,res))