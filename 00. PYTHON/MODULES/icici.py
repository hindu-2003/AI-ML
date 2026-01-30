#icici.py<--File Name and Module Name
bname="BOI"
addr="HYD"  # Here bname and addr are called global Variables
def simpleint():  # Function Definition
    p=float(input("Enter principle Amount:"))
    t=float(input("Enter Time:"))
    r=float(input("Enter Rate of Interest:"))
    #cal si and tot amt to pay
    si=(p*t*r)/100
    totamt=p+si
    print("-----------------------------------")
    print("\tPrinciple Amount:{}".format(p))
    print("\tTime:{}".format(t))
    print("\tRate of Interest:{}".format(r))
    print("\tSimple Interest:{}".format(si))
    print("\tTOTAL AMOUNT TO PAY:{}".format(totamt))
    print("-----------------------------------")

