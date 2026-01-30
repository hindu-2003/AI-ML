#program for Generating Mul table for a Given + Ve Number
n=int(input("Enter a Number for Generating Mul table:"))
if(n<=0):
    print("{} is Invalid Input".format(n))
else:
    print("="*50)
    print("Mul Table for :{}".format(n))
    print("=" * 50)
    i=1
    while(i<=10):
        print("\t\t{} x {} = {}".format(n,i,n*i))
        i+=1
    else:
        print("=" * 50)

