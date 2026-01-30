a =float(input("Enter first value:"))
b =float(input("Enter second value:"))
c =float(input("Enter third value:"))
if b<=a>c: #a is bigger
    print("{},{},{} in bigger value is: {}".format(a,b,c,a))
if a<b>=c:
    print("{},{},{} in bigger value is: {}".format(a, b, c, b))
if a<=c>b:
    print("{},{},{} in bigger value is: {}".format(a, b, c, c))
if (a==b==c):
    print("all values are eaqual")