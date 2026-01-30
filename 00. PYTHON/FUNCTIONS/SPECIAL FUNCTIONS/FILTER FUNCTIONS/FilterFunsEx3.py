#Program for Obtaining +ve Elements from list of values
#FilterFunsEx3.py
print("Enter List of Values separated by space:")
lst=[int(val) for val in input().split()]
pslist=list(filter(lambda val: True if val>0 else False, lst))
nglist=tuple(filter(lambda val: True if val<0 else False, lst))
print("Given Values=",lst)
print("List of +Ve Values=",pslist)
print("List of -Ve Values=",nglist)