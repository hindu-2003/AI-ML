#LIST_Q60.py
#60. Write a Python program to find a tuple, the smallest second index value from a list of tuples.
import functools as fc
lt = [(1,2,1),(60,20,20),(9,6,3)]
lst = []
for val in lt:
    lst.append(list(val))
for val in lst:
    val.sort()
    print(tuple(val),"This tuple 2nd smallest number is: ",val[1],end=" \n")
