line = "PyT5ho$n l2s aN 0o3p L@a9n1G"
lin=line.replace(" ","")
# upper case concatenate
# lower case concatenate
# Special symbol concatenate
# Numeric values concatenate
import functools
def fmp():
    digs = []
    upper = []
    lower = []
    ss = []
    for x in lin:
        if x.isdigit():
            digs.append(x)
        elif x.isupper():
            upper.append(x)
        elif x.islower():
            lower.append(x)
        else:
            ss.append(x)
    dc = functools.reduce(lambda m,b:m+b,digs)
    print(dc)
    uc = functools.reduce(lambda m, b: m + b, upper)
    print(uc)
    lc = functools.reduce(lambda m, b: m + b, lower)
    print(lc)
    sc = functools.reduce(lambda m, b: m + b, ss)
    print(sc)
    print("-"*50)
    print("Given Line:",line)
    print("-" * 50)
    print("Concatenate of digits:",dc)
    print("_" * 50)
    print("Concatenate of digits:", uc)
    print("_" * 50)
    print("Concatenate of digits:", lc)
    print("_" * 50)
    print("Concatenate of digits:", sc)
    print("*" * 50)


fmp()