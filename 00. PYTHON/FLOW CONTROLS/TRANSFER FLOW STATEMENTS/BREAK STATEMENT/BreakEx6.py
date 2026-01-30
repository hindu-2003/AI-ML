#Program for Deciding Weather Given Number is Prime or Not
#BreakEx6.py
n=int(input("Enter a Number to decide prime or not:"))
if(n<=1):
    print("{} is Invalid Input".format(n))
else:
    res="Prime"
    for i in range(2,n):
        if(n%i==0):
            res="Not Prime"
            break
    print("{} is {}".format(n,res))

