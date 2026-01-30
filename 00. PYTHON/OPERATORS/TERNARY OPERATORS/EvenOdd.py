#Program for deciding whether the given number is even or odd
#EvenOdd.py
n=float(input("Enter a Number:"))
res="Even" if n%2==0  else "Odd"
print("{} is {}".format(n,res))