# for loop in for loop
#InnerLoopEx1.py
for i in range(1,6): # outer loop
    print("-"*50)
    print("Val of i-outer loop=",i)
    print("-" * 50)
    for j in range(1,4): # inner loop
        print("\tVal of j-inner loop=", j)
    else:
        print("i am out-off inner loop")
else:
    print("i am out-off outer loop")

