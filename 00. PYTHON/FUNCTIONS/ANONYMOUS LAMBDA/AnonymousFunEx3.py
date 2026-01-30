#Program for Finding  max and minfrom List of  Numbers by using Anonymous Functions
#AnonymousFunEx3.py
findmax=lambda lst:"All Are equal" if len(set(lst))==1 else max(lst)
findmin=lambda lst:"All Are equal" if len(set(lst))==1 else min(lst)

#Main Program
print("Enter List of Values separated by space:")
lst=[int(val) for val in input().split()]
print("Max({})={}".format(lst,findmax(lst)))
print("Min({})={}".format(lst,findmin(lst)))
