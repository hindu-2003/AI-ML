#Program for Finding  Sum and Average by using Anonymous Functions
#AnonymousFunEx5.py
findsum=lambda lst: sum(lst)
findavg=lambda lst: sum(lst)/len(lst)

#Main Program
print("Enter List of Values separated by space:")
lst=[float(val) for val in input().split()]
ss=findsum(lst)
av=findavg(lst)
print("Sum({})={}".format(lst,ss))
print("Avg({})={}".format(lst,av))