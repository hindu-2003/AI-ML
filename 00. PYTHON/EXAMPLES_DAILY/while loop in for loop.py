n = int(input("Enter the number: "))
print("=" * 50)
print("          EXECUTED NESTED LOOPS")

for i in range(1,n+1):
    print("=" * 50)
    print("\t outer loop--o/p:{}".format(i))
    print("=" * 50)
    j = 1
    while(j<=3):
        print("\t\t inner loop--executed:{}".format(j))
        k = 1
        while(k<=3):
            print("\t\t\t\tNested inner loop:{}".format(k))
            k = k+1
        else:
            j=j+1

else:
        print("=" * 50)
        print("\t\tEXECUTED NESTED LOOPS COMPLETED")
        print("=" * 50)

