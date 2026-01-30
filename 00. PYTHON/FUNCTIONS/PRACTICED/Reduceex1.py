import functools
print("Enter List of Values Separated by Space:")
lst=[float(val) for val in input().split()]
res=functools.reduce(lambda k,v:k+v,lst)
print("Sum({})={}".format(lst,res))