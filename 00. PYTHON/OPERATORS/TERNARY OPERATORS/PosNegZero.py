#Program for accepting a Number and decide wheteher it is +Ve or -Ve or Zero
#PosNegZero.py
n=float(input("Enter a Number:")) # -6
res="Zero" if(n==0) else "Possitive" if n>0 else "Negative"
print("{} is {}".format(n,res))
