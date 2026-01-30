#Program for generating  Mul tables  for list of Random Numbers
#InnerloopEx7.py
lst=[17,19,-7,8,25,0,33]
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


