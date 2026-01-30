#MatchCaseEx2.py
s="""       
            =======================================================
			Base Conversion Calculator
			=======================================================
					1. D to B
					2. D to O
					3. D to H
					------------
					4. B to D
					5. B to O
					6. B to H
					-------------
					7. O to D
					8. O to B
					9. O to H
					------------
					10. H to D
					11. H to B
					12. H to O
			===================================================="""
print(s)
ch=int(input("Enter Ur Choice:"))
match(ch):
    case 1|2|3:
        d=int(input("Enter Decimal Number:"))
        bv=bin(d) # 1
        ov=oct(d) # 2
        hv=hex(d) # 3
        print("Bin({})={}".format(d,bv))
        print("Oct({})={}".format(d,ov))
        print("Hex({})={}".format(d,hv))
    case 4|5|6:
        x=input("enter binary value preceded with 0b:")
        dv=int(x,2)
        ov=oct(int(x,2))
        hv=hex(int(x,2))
        print("Dec({})={}".format(x,dv))
        print("Oct({})={}".format(x,ov))
        print("hex({})={}".format(x, hv))
    case 7|8|9:
            x = input("enter Octal value preceded with 0o:")
            dv = int(x, 8)
            bv = bin(int(x, 8))
            hv = hex(int(x, 8))
            print("Dec({})={}".format(x, dv))
            print("Bin({})={}".format(x, bv))
            print("hex({})={}".format(x, hv))
    case 10 | 11 | 12:
        x = input("enter hex decimal value preceded with 0x:")
        dv = int(x, 16)
        bv = bin(int(x, 16))
        ov = oct(int(x, 16))
        print("Dec({})={}".format(x, dv))
        print("Bin({})={}".format(x, bv))
        print("Oct({})={}".format(x, ov))
    case _:
        print("Ur selection of Operation is Wrong-Try again")




