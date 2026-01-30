#PrimeNumbersWithinRange.py
n=int(input("Enter the Range,In which Prime Numbers to display:"))
if(n<=1):
    print("{} invalid input".format(n))
else:
    print("--------------------------------")
    print("List of Prime Numbers:")
    print("--------------------------------")
    nop=0
    nopsum=0
    for num in range(2,n+1): # Outer loop--Supply Numbers
        res=True
        for i in range(2,num):
            if(num%i==0):
                res=False
                break
        if(res):
            print(num)
            nop=nop+1
            nopsum=nopsum+num
    else:
        print("Number of Primes within {} Range={}".format(n,nop))
        print("Sum of all Primes={}".format(nopsum))