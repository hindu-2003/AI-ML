#Program for Obtaining Squares and Square Roots for List of Values
#MapEx3.py
print("Enter List of Numerical Values:")
lst=[float(val) for val in input().split()]
print("Given List of Elements=",lst)  # [25.0, 3.0, 4.0, 15.0, 226.0]
sqrlist=list(map(lambda x: x**2, lst))
sqroots=list(map(lambda x: round(x**0.5,2),lst))
print("-"*60)
print("\tGiven Number\tSquares\t\tSquare Roots")
print("-"*60)
for no,sqno,sqrtno in zip(lst,sqrlist,sqroots):
	print("\t{}\t\t{}\t\t{}".format(no,sqno,sqrtno))
print("-"*60)

