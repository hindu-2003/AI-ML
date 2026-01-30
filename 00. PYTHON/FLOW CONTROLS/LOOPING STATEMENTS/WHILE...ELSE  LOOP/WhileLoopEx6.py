#Program for finding Sum of n natural Numbers,squares and Cubes
#WhileLoopExb.py
n=int(input("Enter How Many natural nums u want:"))
if(n<=0):
    print("{} is Invalid Input".format(n))
else:
    print("=" * 50)
    print("NatNums\t\tSquares\t\tCubes")
    print("-"*50)
    s=0 # For Accumulating the Individual generated nums
    ss=0 # For Accumulating the Individual generated nums squares
    cs=0 # # For Accumulating the Individual generated nums cubes
    i=1 # Initlization part
    while(i<=n):
        print('\t{}\t\t{}\t\t\t\t{}'.format(i,i**2,i**3))
        s = s + i
        ss= ss+i**2
        cs=cs+i**3
        i=i+1
    else:
        print("-" * 50)
        print("\t{}\t\t{}\t\t\t\t{}".format(s,ss,cs))
        print("-" * 50)
