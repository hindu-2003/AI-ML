#Program for generating  Mul tables  for list of Random Numbers
#InnerloopEx7.py
lst=list()
while(True):
    value=input("Enter a Number(Pree ! to stop):")
    if(value=="!"):
        break
    else:
        lst.append(int(value))
print("----------------------------------")
print("List of Elements=",lst)
print("----------------------------------")
#Code for Generating Mul Table for List of Random Values
for num in lst: # Supply the Num from list--outer loop
    if(num<=0):
        print("{} is invalid Input".format(num))
        continue
    print("---------------------")
    print("Mul Table for :{}".format(num))
    print("---------------------")
    for i in range(1,11): # inner loop
        print("\t{} x {} = {}".format(num,i,num*i))
    else:
        print("---------------------")


