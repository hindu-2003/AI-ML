n = int(input("Enter a number for input:"))
for i in range(1,n+1):
    print("outer loop-output:{}".format(i))
    for j in range(1,4):
        print("\t\tinner loop-output:{}".format(i))
else:
    print("out put is arrived wise loop in loop")