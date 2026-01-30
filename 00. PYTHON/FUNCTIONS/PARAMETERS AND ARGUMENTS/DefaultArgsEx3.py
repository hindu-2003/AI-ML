#Program for Demonstrating Default Arguments technique
#DefaultArgsEx3.py
def insertstuddetails(sno,sname,marks,crs="PYTHON",cnt="INDIA"):
	print("\t{}\t{}\t{}\t{}\t{}".format(sno,sname,marks,crs,cnt))


#Main Program
print("-"*50)
print("\tSNO\tNAME\tMARKS\tCOURSE\tCountry")
print("-"*50)
insertstuddetails(100,"RS",3.5) # Function Call with Possitional args
insertstuddetails(200,"TR",4.5) # Function Call with Possitional args
insertstuddetails(300,"MC",2.5) # Function Call with Possitional args
insertstuddetails(400,"DR",1.5) # Function Call with Possitional args
insertstuddetails(cnt="USA",crs="HTML",sname="DR",marks=1.5,sno=500)  # Function Call with Keyword args
insertstuddetails(sname="KV",crs="Java",marks=3.4,sno=600) # Function Call with Keyword args
print("-"*50)
