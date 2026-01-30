#program for generating 1 to n where n is +ve
#WhileLoopEx1.py
n=int(input("Enter How Many Numbers u want to Generate:"))
if(n<=0):
    print("{} is Invalid input".format(n))
else:
    print("-"*50)
    print("Numbers within:{}".format(n))
    print("-" * 50)
    i=1 # Initlization Part
    while(i<=n): # Cond Part
        print(i)
        i+=1 # Updation Part
    else:
        print("*"*50)


