#Program for Finding Sum of Digits of Given Number--Logic-2
#DigitsSumEx2.py
num=input("Enter a Number for Finding Digits Sum:") # num='4578'
s=0
for ch in num:
    s=s+int(ch)
else:
    print("Digits sum=",s)
