#SetComprehensionEx1.py
print("Enter List of Values separated by comma:")
st= {int(val) for val in input().split(",")} # set Comprehension
print("Set of Element=",st)
print(type(st))
