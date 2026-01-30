#ListComprehensionEx1.py
print("Enter List of Values separated by space:")
lst=[ str(val) for val in input().split()] # List Comprehension
print("List of Element=",lst)
print(type(lst))
