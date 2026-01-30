#program for accepting List of Numerical Values and find +ve Values sum and -ve vals sum
#FilterReduceEx1.py
import functools
print("Enter List of Numerical Values separated by space:")
vals=[float(val) for val in input().split()]
print("Given List of Values=",vals)
print("--------------------------------")
#Filter +Ve Values
posvalues=list(filter(lambda k: k>0,vals))
print("Possitive Values")
print(posvalues)
#Find Pos Values Sum
psum=functools.reduce(lambda k,v:k+v,posvalues)
print("Sum({})={}".format(posvalues,psum))
print("--------------------------------")
#Filter -Ve Values
negvalues=list(filter(lambda k: k<0,vals))
print("Negative Value:")
print(negvalues)
#Find Neg Values Sum
nsum=functools.reduce(lambda k,v:k+v,negvalues)
print("sum({})={}".format(negvalues,nsum))
print("--------------------------------")