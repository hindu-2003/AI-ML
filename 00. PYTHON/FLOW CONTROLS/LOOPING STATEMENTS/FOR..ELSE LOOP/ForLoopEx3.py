#prohgram for Generating mul Table for a Guven +ve Number
#ForLoopEx3.py
n=int(input("Enter a Number for Generating Mul Table:"))
if(n<=0):
    print("{} is Invalid Input".format(n))
else:
    print("-"*50)
    print("Mul Table for {}".format(n))
    print("-" * 50)
    for i in range(1,11):
        print("{} x {} = {}".format(n,i,n*i))
    else:
        print("-" * 50)


