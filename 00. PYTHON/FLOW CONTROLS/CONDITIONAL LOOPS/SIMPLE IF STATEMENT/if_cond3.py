a =float(input("Enter first value:"))
b =float(input("Enter second value:"))
c =float(input("Enter third value:"))
if a>b and a>c: #a is bigger
    print("{},{},{} in bigger value is: {}".format(a,b,c,a))
if b>a and b>c:
    print("{},{},{} in bigger value is: {}".format(a, b, c, b))
if c>a and c>b:
    print("{},{},{} in bigger value is: {}".format(a, b, c, c))
if (a==b) and (b==c) and a==c:
    print("all values are eaqual")