#Program for Obtaning The Factors of a Given Number
#FactorsEx1.py
num=int(input("Enter a Number for Finding Its Factors:"))
if(num<=0):
    print("{} is Invalid Input".format(num))
else:
    for i in range(1,(num//2)+1):
        if(num%i==0):
            print(i)
    print(num)
