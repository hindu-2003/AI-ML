#Program for displaying +Ve Values from List of Values
#ContinueStmtEx4.py
lst=[10,-20,30,40,0,-50,-60,-12,45,67,90,-45]
print("List of +ve Values")
nop=0
for val in lst:
    if(val<=0):
        continue
    print(val)
    nop=nop+1
print("Number of +Ve Values=",nop)
print("-------------------------------")
print("List of -VE Values")
non=0
for val in lst:
    if(val>=0):
        continue
    print(val)
    non=non+1
print("Number of -Ve Values=",non)