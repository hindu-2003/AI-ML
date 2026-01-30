#Program for Obtaining Reverse of a Given Value--without using extended Slicing
#ValueReverseEx3.py--Logic-2 (Int data only
value=int(input("Enter Any Value:")) # 4578
if(value<=0):
    print("{} is Invalid Input".format(value))
else:
    rvn=0
    on=value
    while(value>0):
        dig=value%10
        rvn=rvn*10+dig
        value=value//10
    else:
        print("Reversed Number=",rvn)
        if(rvn==on):
            print("{} is palindrome".format(on))
        else:
            print("{} is not palindrome".format(on))

