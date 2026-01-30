#WhileLoopEx2.py
n=int(input("Enter How Many Odd Numbers u want to Generate:"))
if(n<=0):
    print("{} is Invalid Input".format(n))
else:
    if(n%2==0):
        n=n-1
    while(n>=1):
        print("\t{}".format(n))
        n=n-2

