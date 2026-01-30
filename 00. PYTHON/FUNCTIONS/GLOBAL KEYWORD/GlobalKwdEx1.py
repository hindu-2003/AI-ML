#Program for Demonstrating global keyword
#GlobalKwdEx1.py
def incr():
    global a
    a=a+1
def modify():
    global a
    a=a*2
#Main Program
a=10 # here a is called Global variable
print("In Main Program--Value of a before incr()={}".format(a))
incr() # function call
print("In Main Program--Value of a after incr()={}".format(a))
modify() # function call
print("In Main Program--Value of a after moidfy()={}".format(a))