# for loop in while loop
#InnerLoopEx3.py
i=1
while(i<=5): # outer loop
    print("-"*50)
    print("Val of i-outer loop=",i)
    print("-" * 50)
    for j in range(3,0,-1): # inner loop
        print("\tVal of j-inner loop=", j)
    else:
        i=i+1
        print("i am out-off inner loop")
else:
    print("i am out-off outer loop")

