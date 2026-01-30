#Program for Demonstrating global keyword
#GlobalKwdEx2.py
def update1():
    global a,b
    a=a+1
    b=b+1

def update2():
    global a,b
    a=a*2
    b=b*2

def update3():
    #No Need to write write global kwd bcoz here we are just accessing global var vals a,b
    c=a+10
    d=b+10
    print("Local c={} and Local d={}".format(c,d))
def update4():
    global a
    a=a+b

#Main Program
a,b=10,20
print("Main Program, before update1() a={}  b={}".format(a,b))
update1()
print("Main Program, after update1() a={}  b={}".format(a,b))
update2()
print("Main Program, after update2() a={}  b={}".format(a,b))
update3()
print("Main Program, after update3() a={}  b={}".format(a,b))
update4()
print("Main Program, after update4() a={}  b={}".format(a,b))