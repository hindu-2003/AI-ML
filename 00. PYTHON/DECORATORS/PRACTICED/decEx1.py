def getval():
    return float(input("Enter any numerical value :"))

def square(mb):
    print(" I am from outer")
    def calculate():
        n = mb
        res = n**2
        r = n**3
        print(" i am from inner ")
        return n,res
    return calculate
rv = (square(getval()))()
print("square={}".format(rv))


















