#Program for finding Factroial of a Number
#WhileLoopEx8.py
n=int(input("a Number for Cal Factorial of Number:"))
if(n<0):
    print("{} is Invalid Input--no Factrial for -ve Nums".format(n))
else:
    fact=1
    i=1
    while(i<=n):
        fact=fact*i
        i=i+1
    else:
        print("Factorial({})={}".format(n,fact))

