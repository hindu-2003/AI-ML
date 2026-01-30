#Program for Obtaining +ve Elements from list of values
#FilterFunsEx2.py
positive=lambda val: True if val>0 else False # Anonymous Function Defintion
negative=lambda val: True if val<0 else False # Anonymous Function Defintion
#Main Program
print("Enter List of Values separated by space:")
lst=[int(val) for val in input().split()]
pslist=list(filter(positive,lst))
nglist=tuple(filter(negative,lst))
print("Given Values=",lst)
print("List of +Ve Values=",pslist)
print("List of -Ve Values=",nglist)