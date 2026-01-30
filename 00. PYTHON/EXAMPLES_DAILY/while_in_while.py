n = int(input("Enter the number:"))
i = 1
while(i<=n):
    print("outer loop-output:{}".format(i))
    j = 1
    while(j<=3):
        print("\t\tinner loop-output:{}".format(j))
        j = j+1
    else:
        i=i+1

