#Program for Demonstrating the Need pf Variable length arguments
#This Program will not execute as it is bcoz PVM is performing Interpretation Process and It remembers latest function definittion (bcoz we have familiy of similar function names with Variable Positional Args / params)
#VarArgsEx1.py
def  disp(a,b,c,d,e): # Function Def-1 with 5 Formal Pos Parms
	print(a,b,c,d,e)
def disp(a,b,c,d): # Function Def-2 with 4 Formal Pos Parms
	print(a,b,c,d)
def disp(a,b,c): # Function Def-3 with 3 Formal Pos Parms
	print(a,b,c)
def disp(a,b): # Function Def-4 with 2 Formal Pos Parms
	print(a,b)
def disp(a): # Function Def-5with 1 Formal Pos Parms
	print(a)
def disp(): # Function Def-6 with ZERO Formal Pos Parms
	print("empty")
def  disp(a,b,c,d,e,f): # Function Def-7 with 6 Formal Pos Parms
	print(a,b,c,d,e,f)


#Main Program
disp(10,20,30,40,50) # Function Call-1 with 5 Args
disp(10,20,30,40) # Function Call-2 with 4 Args
disp(10,20,30) # Function Call-3 with 3 Args
disp(10,20) # Function Call-4 with 2 Args
disp(10) # Function Call-5 with 1 Args'
disp() # Function Call-6 with 0 Args
disp("TR","RS","DR",12.34,True,2+3j) # Function Call-7 with 6 Args
