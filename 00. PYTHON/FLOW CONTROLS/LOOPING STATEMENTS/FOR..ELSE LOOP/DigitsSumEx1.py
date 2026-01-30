#Program for Finding Sum of Digits of Given Number--Logic-1
#DigitsSumEx1.py
num=int(input("Enter a Number for Finding Digits Sum:"))
if(num<=0):
    print("{} is Invalid input".format(num))
else:
    s=0
    while(num>0):
        digit=num%10
        s=s+digit
        num=num//10
    else:
        print("Sum of Digits=",s)
