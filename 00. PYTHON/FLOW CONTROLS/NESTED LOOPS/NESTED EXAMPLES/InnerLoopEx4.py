# while loop in for loop
#InnerLoopEx4.py
for i in range(1,6)[::-1]: # outer loop
    print("-"*50)
    print("Val of i-outer loop=",i)
    print("-" * 50)
    j=3
    while(j>=1): # inner loop
        print("\tVal of j-inner loop=", j)
        j=j-1
    else:
        print("i am out-off inner loop")
else:
    print("i am out-off outer loop")

