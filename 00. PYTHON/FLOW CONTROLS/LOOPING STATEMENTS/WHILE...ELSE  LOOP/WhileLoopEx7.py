#Program for finding product of n natural Numbers
#WhileLoopEx7.py
n=int(input("Enter How Many natural nums Product u want:"))
if(n<=0):
    print("{} is Invalid Input".format(n))
else:
    print("=" * 50)
    print("Natural Numbers within:{}".format(n))
    print("-"*50)
    s=1 # For Accumulating the product the Individual generated nums
    i=1 # Initlization part
    while(i<=n):
        print('\t{}'.format(i))
        s = s * i
        i=i+1
    else:
        print("-" * 50)
        print("Product={}".format(s))
        print("-" * 50)

