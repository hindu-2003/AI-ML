#Program for Accepting List of Numerical value and get Max Value by using Reduce Function
#ReduceFunEx3.py
import functools
print("Enter List of Values Separated by Space:")
values=[float(val) for val in input().split() ]
print("Given Values:")
print(values) # [10.0, 2.0, 12.0, 3.0, 45.0, 4.0, 56.0, 13.0, -3.0, 6.0]
#Find Max by using reduce()
val=functools.reduce(lambda k,v: k if k>v else v, values)
print("max=",val)
#Find Min by using reduce()
val=functools.reduce(lambda k,v: k if k<v else v, values)
print("min=",val)
