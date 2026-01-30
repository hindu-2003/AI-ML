#Program for Finding Biggest of Two Numbers and Check for Equality
# by using Anonymous Functions
##AnonymousFunEx2.py
findmaxtwo=lambda k,v: k if k>v else v if v>k else "Both Values are equal"

#Main Program
a=int(input("Enter First Value:"))
b=int(input("Enter Second Value:"))
res=findmaxtwo(a,b)
print("Max({},{})={}".format(a,b,res))

