#Program for finding Factroial of a Number
# 4! = 4 x 3 x 2 x 1
#WhileLoopEx9.py
n=int(input("a Number for Cal Factorial of Number:"))
if(n<0):
    print("{} is Invalid Input--no Factrial for -ve Nums".format(n))
else:
    fact=1
    i=n # preserving Original Value in temp var i
    while(n>=1):
        fact=fact*n
        n=n-1
    else:
        print("{}!={}".format(i,fact))


