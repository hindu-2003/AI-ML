#Program for Obtaining Reverse of a Given Value--without using extended Slicing
#ValueReverseEx2.py--Logic-2 (Int data and str data)
value=input("Enter Any Value:") # PYTHON
s=""
for i in range(-1,-len(value)-1,-1):
    s=s+value[i]
else:
    print("Given Value:",value)
    print("Reversed Value:",s)
