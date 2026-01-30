#Program for Deciding Weather Given Number is Prime or Not
#BreakEx5.py
n=int(input("Enter a Number to decide prime or not:"))
if(n<=1):
    print("{} is Invalid Input".format(n))
else:
    res="Prime"
    for i in range(2,n):
        if(n%i==0):
            res="Not Prime"
            break
    if(res=="Prime"):
        print("{} is {}".format(n,res))
    else:
        print("{} is {}".format(n,res))

