#Program for deciding whether the given number is even or odd with +ve number
#if user enters -ve Numbers then display Invalid Input
#EvenOddPos.py
n=float(input("Enter a Number:"))
res="Invalid Input" if (n<0) else "Even" if n%2==0 else "Odd"
print("{} is {}".format(n,res))