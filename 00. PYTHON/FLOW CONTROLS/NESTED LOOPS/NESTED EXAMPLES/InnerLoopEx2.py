# while loop in while loop
#InnerLoopEx2.py
i=1
while(i<=5): # outer loop
    print("-"*50)
    print("Val of i-outer loop=",i)
    print("-" * 50)
    j=1
    while(j<=3): # inner loop
        print("\tVal of j-inner loop=", j)
        j=j+1
    else:
        i=i+1
        print("i am out-off inner loop")
else:
    print("i am out-off outer loop")

