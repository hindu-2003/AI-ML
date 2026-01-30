#GlobalsFunEx1.py
a=10
b=20 # here 'a' and 'b' are called Programmer-Defined Global Variables
def operations():
    d=globals()
    print(len(d))
    print("--------------------------------------------")
    print("Invisible Global Variables")
    for gvn,gvv in d.items():
        print("\t{}---->{}".format(gvn,gvv))
    print("--------------------------------------------")
    print("Programmer-Defined Global Variables Information-Way-1")
    print("--------------------------------------------")
    print("Val of a=",d.get('a'))
    print("Val of b=", d.get('b'))
    print("--------------------------------------------")
    print("Programmer-Defined Global Variables Information-Way-2")
    print("--------------------------------------------")
    print("Val of a=",d['a'])
    print("Val of b=",d['b'])
    print("--------------------------------------------")
    print("Programmer-Defined Global Variables Information-Way-3")
    print("--------------------------------------------")
    print("Val of a=",globals().get('a'))
    print("Val of b=", globals().get('b'))
    print("--------------------------------------------")
    print("Programmer-Defined Global Variables Information-Way-4")
    print("--------------------------------------------")
    print("Val of a=", globals()['a'])
    print("Val of b=", globals()['b'])
    print("--------------------------------------------")
#Main Program
operations()