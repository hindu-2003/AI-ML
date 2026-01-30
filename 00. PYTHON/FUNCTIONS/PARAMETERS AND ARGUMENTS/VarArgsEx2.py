#Program for Demonstrating the Need of Variable length arguments
#This Program will  execute as it is 
#VarArgsEx2.py
def  disp(a,b,c,d,e): # Function Def-1 with 5 Formal Pos Parms
	print(a,b,c,d,e)
disp(10,20,30,40,50) # Function Call-1 with 5 Args
disp("RS","TR","ST","DR","KV") # Function Call-1 with 5 Args
#-------------------------------------------------------------------------------------------------------
def disp(a,b,c,d): # Function Def-2 with 4 Formal Pos Parms
	print(a,b,c,d)
disp(10,20,30,40) # Function Call-2 with 4 Args
#-------------------------------------------------------------------------------------------------------
def disp(a,b,c): # Function Def-3 with 3 Formal Pos Parms
	print(a,b,c)
disp(10,20,30) # Function Call-3 with 3 Args
#-------------------------------------------------------------------------------------------------------
def disp(a,b): # Function Def-4 with 2 Formal Pos Parms
	print(a,b)
disp(10,20) # Function Call-4 with 2 Args
#-------------------------------------------------------------------------------------------------------
def disp(a): # Function Def-5with 1 Formal Pos Parms
	print(a)
disp(10) # Function Call-5 with 1 Args
#-------------------------------------------------------------------------------------------------------
def disp(): # Function Def-6 with ZERO Formal Pos Parms
	print("empty")
disp() # Function Call-6 with 0 Args

#-------------------------------------------------------------------------------------------------------
def  disp(a,b,c,d,e,f): # Function Def-7 with 6 Formal Pos Parms
	print(a,b,c,d,e,f)

disp("TR","RS","DR",12.34,True,2+3j) # Function Call-7 with 6 Args
#-------------------------------------------------------------------------------------------------------
#Limitation: 
# In This Program -- we have 7 function calls---7 function defs
#In general ------------we have n-function calls---we need n-Function defs----waste of time takes more development time
# We need  n-function calls we have----we need 1 FUNCTION DEFINITION