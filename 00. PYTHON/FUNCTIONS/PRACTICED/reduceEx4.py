import functools
print("Enter the values for list with separated by space :")
lst = [val for val in input().split()]
op = functools.reduce(lambda k,v: k if k>v else v ,lst)
print(op)

