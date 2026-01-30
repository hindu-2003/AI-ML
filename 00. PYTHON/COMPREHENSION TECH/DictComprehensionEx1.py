#DictComprehensionEx1.py
print("Enter List of Values separated comma:")
d= {int(val):int(val)**2  for val in input().split(",")} # dict Comprehension
print("Dict of Element=",d)
for k,v in d.items():
    print("\t{}--->{}".format(k,v))
