#Program for Demonstrating the Need of  Keyword Variable Length Arguments
#This Program will not execute as it is 
#PureKeywordVarLenArgsEx2.py

def   dispvalues( **hyd): # Here **hyd is called Keyword Variable length Argument and whose type dict
	print("----------------------------------------------------")
	print("Number of Values in Key-word Var length Param=",len(hyd))
	for k,v in hyd.items():
		print("\t{}-->{}".format(k,v))
	print()
	print("----------------------------------------------------")

#Main Program
dispvalues(sno=100,sname="RS",marks=45.67,cname="OUCET") # Function call-1 with 4-Keyword var length args
dispvalues(eno=1000,ename="TR",sal=5.6,compname="TCS",dsg="SE") # Function call-2 with 5-Keyword var lengthargs
dispvalues(sid=200,stname="abc",hb1="Sleeping",hb2="Eating",hb3="Chatting",hb4="Roaming") # Function call-3 with 6-Keyword  var length args
dispvalues(tno=300,tname="Rossum",sub1="PYTHON-JAVA")# Function call-4 with 3-Keyword var length args
dispvalues(cid=500) # Function call-5 with 1-Keyword var length arg
dispvalues()# Function call-6 with 0-Keyword var length arg