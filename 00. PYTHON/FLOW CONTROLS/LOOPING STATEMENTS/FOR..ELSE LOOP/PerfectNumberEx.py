#Program for Deciding Whether the given number is Perfect or not
#Perfect Number:   Sum of the Factors of a Given Number is equal to Original Number
#PerfectNumberEx.py
num=int(input("Enter a Number for Finding Its Factors:"))
if(num<=0):
    print("{} is Invalid Input".format(num))
else:
    s=0
    for i in range(1,(num//2)+1):
        if(num%i==0):
            s=s+i
            print(i)
    else:
        if(s==num):
            print("{} is Perfect Number".format(num))
        else:
            print("{} is Not Perfect Number".format(num))
