#program for Performing Division of Two Numbers
#Div1.py
print("Program Execution Started")
s1=input("Enter First Value:")
s2=input("Enter Second Value:")
#Convert str type value into int type
a=int(s1) #------------------------------- exception generated stmt--ValueError
b=int(s2)#------------------------------- exception generated stmt--ValueError
print("First Value:",a)
print("Second Value:",b)
c=a/b  #------------------------------- exception generated stmt--ZeroDivisionError
print("Div=",c)
print("Program Execution Ended")