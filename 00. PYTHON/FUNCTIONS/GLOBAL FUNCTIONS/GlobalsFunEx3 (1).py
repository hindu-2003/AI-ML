#Program for Demonstrating globals()
#GlobalsFunEx2.py
a=10
b=20
c=30
d=40 # # Here a,b,c,d are called global Variables
def operations():
    a=100
    b=200
    c=300
    d=400 # Here a,b,c,d are called local Var
    res=a+b+c+d+globals()['a']+globals()['b']+globals()['c']+globals()['d']
    print("Sum=",res)
#Main Program
operations() # function call