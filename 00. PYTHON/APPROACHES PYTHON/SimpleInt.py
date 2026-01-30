#program for cal simpleint and total amount to pay
#SimpleInt.py
p=float(input("Enter principle Amount:"))
t=float(input("Enter Time:"))
r=float(input("Enter Rate of Interest:"))
#cal si and totamt
si=(p*t*r)/100
totamt=p+si
#display the Result
print("*"*50)
print("\t\tResults of Simple Interest")
print("*"*50)
print("\t\tPrinciple Amount:{}".format(p))
print("\t\tTime:{}".format(t))
print("\t\tRate of Interest:{}".format(r))
print("\t\tSimple Interest:{}".format(si))
print("\t\tTOTAL AMOUNT TO PAY:{}".format(totamt))
print("*"*50)
