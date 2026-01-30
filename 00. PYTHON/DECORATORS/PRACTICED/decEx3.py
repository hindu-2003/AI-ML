def square(v):
    print(v,type(v))

@square
def getval():
    return float(input("Enter any numerical value :"))

k = getval()
print(k)
