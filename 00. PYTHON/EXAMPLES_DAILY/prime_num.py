n = int(input("Enter a number:"))
if n<=1:
    print("{} is invalid".format(n))
else:
    nop = 0
    for num in range(2,n):
        res = True
        for i in range(2,num):
            if (num%i==0):
                res = False
                break
            if(res):
                print(num)
                nop+=1


