def findtotalmarks(sno,sanme,sclass,*val,**vals):
    print("="*50)
    print("Student number :{}".format(sno))
    print("Student Name :{}".format(sanme))
    print("Student class :{}".format(sclass))
    print("Student practical :{}".format(val))
    print("Student subject :{}".format(vals))
    p = 0
    for i in val:
        p =p+i
    print("Student total pr :{}".format(p))
    s = 0
    for k,v in vals.items():
        s =s +v
    print("Student total marks :{}".format(s))


# main program
findtotalmarks(10,"RAJESH","X",10,20,30,40,Tel=50,Hin=85,Eng=95,Maths=87,Sci=69,Soc=98)
findtotalmarks(20,"MAHESH","XII",10.,3.,5.2,6,Sanskri=56,English=89,Mathes=85,Physics = 78,Chemistry=58)
findtotalmarks(30,"RAJU","UG",11,22,33,44,55,Telugu = 56,English=56,Mathes=98,Chemistry=58,Computer_sci=52)
findtotalmarks(40,"SWAMY","Tuter")
findtotalmarks(50,"KVR","TRINER")


