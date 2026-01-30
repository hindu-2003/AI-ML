a = float(input("Enter first number:"))
b = float(input("Enter second number:"))
if a>b:
    print("{},{} in bigger value is:{} ".format(a,b,a))
else:
    if b>a:
        print("{},{} in bigger value is:{} ".format(a, b, b))
    else:
        print("Both are equal")