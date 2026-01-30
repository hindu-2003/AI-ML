#Program for Demonstrating the Need pf Variable length arguments
#This Program will  execute as it is 
#PureVarArgsEx2.py

def  disp( *a):  # here *a is called Variable length Parameter whose type is <class,tuple>
	print("--------------------------------------------")
	print("Number of Values=",len(a))
	for val in a:
		print(val,end="  ")
	print()
	print("---------------------------------------------")

#Main Program
disp(10,20,30,40,50) # Function Call-1 with 5 Args
disp(10,20,30,40) # Function Call-2 with 4 Args
disp(10,20,30) # Function Call-3 with 3 Args
disp(10,20) # Function Call-4 with 2 Args
disp(10) # Function Call-5 with 1 Args'
disp() # Function Call-6 with 0 Args
disp("TR","RS","DR",12.34,True,2+3j) # Function Call-7 with 6 Args
