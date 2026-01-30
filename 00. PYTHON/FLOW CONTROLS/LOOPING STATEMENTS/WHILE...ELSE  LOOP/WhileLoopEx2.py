#program for generating n to 1 where n is +ve
#WhileLoopEx2.py
n=int(input("Enter How Many Numbers u want to Enter:"))
if(n<=0):
    print("{} is Invalid".format(n))
else:
    print("="*50)
    print("Numbers within :{}".format(n))
    print("="*50)
    i=n # Initlization
    while(i>=1): # Cond Part
        print("\t\t{}".format(i))
        i=i-1 # Updation Part
    else:
        print("=" * 50)


