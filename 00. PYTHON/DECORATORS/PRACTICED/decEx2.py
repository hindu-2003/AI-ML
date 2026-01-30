def getval():
    return float(input("Enter any numerical value :"))
def cube(mb):
    def calc():
        n = mb
        res = n**3
        return res
    return calc
# Main program
k= cube(getval())
print(k(),type(k))