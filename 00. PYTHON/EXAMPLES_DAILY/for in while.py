n = int(input("Enter the number:(outer) "))
a = int(input("Enter the number:(inner) "))
if n<=0:
    print("{} is invalid".format(n))
i = 1
while(i<=n):
    print("=" * 50)
    print("outer loop-output: {}".format(i))
    print("=" * 50)
    for j in range(1,a+1):
        print("\t\tinner loop-executed:{}".format(j))

    i+=1
else:
    print("="*50)
    print("output is cleared")
