#Program for generating 1 to n Mul tables where n is +ve
#InnerloopEx6.py
n=int(input("Enter How Many Mul tables u want:"))
if(n<=0):
    print("{} is invalid Input".format(n))
else:
    for num in range(1,n+1): # outer loop--Supply the Number
        print("Mul table for :{}".format(num))
        print("------------------------------")
        for i in range(1,11): # inner loop--generates mul table
            print("\t{} x {} = {}".format(num,i,num*i))
        else:
            print("------------------------------")