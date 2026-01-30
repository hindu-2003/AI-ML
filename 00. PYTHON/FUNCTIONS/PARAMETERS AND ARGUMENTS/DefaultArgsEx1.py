#Program for Demonstrating Default Arguments technique
#DefaultArgsEx1.py
def insertstuddetails(sno,sname,marks,crs="PYTHON"):
	print("\t{}\t{}\t{}\t{}".format(sno,sname,marks,crs))


#Main Program
print("-"*50)
print("\tSNO\tNAME\tMARKS\tCOURSE")
print("-"*50)
insertstuddetails(100,"RS",3.5) # Function Call with Possitional args
insertstuddetails(200,"TR",4.5) # Function Call with Possitional args
insertstuddetails(300,"MC",2.5) # Function Call with Possitional args
insertstuddetails(400,"DR",1.5) # Function Call with Possitional args
print("-"*50)
