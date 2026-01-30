#Program for Demonstrating the Need of  Keyword Variable Length Arguments
#This Program will not execute as it is bcoz PVM is performing Interpretation Process and It remembers latest function definittion (bcoz we have familiy of similar function names with Keyword Variable Length Positional Args / params)
#KeywordVarLenArgsEx1.py
def  dispvalues(sno,sname,marks,cname): # Function Def-1
	print(sno,sname,marks,cname)
def dispvalues(eno,ename,sal,compname,dsg): # Function Def-2
	print(eno,ename,sal,compname,dsg)
def dispvalues(sid,stname,hb1,hb2,hb3,hb4): # Function Def-3
	print(sid,stname,hb1,hb2,hb3,hb4)
def dispvalues(tno,tname,sub1):
	print(tno,tname,sub1)
def dispvalues(cid) :
	print(cid)

#Main Program
dispvalues(sno=100,sname="RS",marks=45.67,cname="OUCET") # Function call-1 with 4-Keyword args
dispvalues(eno=1000,ename="TR",sal=5.6,compname="TCS",dsg="SE") # Function call-2 with 5-Keyword args
dispvalues(sid=200,stname="abc",hb1="Sleeping",hb2="Eating",hb3="Chatting",hb4="Roaming") # Function call-3 with 6-Keyword args
dispvalues(tno=300,tname="Rossum",sub1="PYTHON-JAVA")# Function call-4 with 3-Keyword args
dispvalues(cid=500) # Function call-5 with 1-Keyword arg
