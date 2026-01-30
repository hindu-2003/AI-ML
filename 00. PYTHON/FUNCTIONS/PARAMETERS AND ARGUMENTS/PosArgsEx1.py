#Program for Demonstrating Possitional Arguments
#PosArgsEx1.py
def insertstuddetails(eno,ename,sal):
	print("\t{}\t{}\t{}".format(eno,ename,sal))


#Main Program
print("-"*50)
print("\tENO\tNAME\tSAL")
print("-"*50)
insertstuddetails(100,"RS",3.5) # Function Call with Possitional args
insertstuddetails(200,"TR",4.5) # Function Call with Possitional args
insertstuddetails(300,"MC",2.5) # Function Call with Possitional args
insertstuddetails(400,"DR",1.5) # Function Call with Possitional args
print("-"*50)
