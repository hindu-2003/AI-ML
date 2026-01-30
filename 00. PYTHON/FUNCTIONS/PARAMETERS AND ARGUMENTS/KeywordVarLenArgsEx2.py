#Program for Demonstrating the Need of  Keyword Variable Length Arguments
#This Program will  execute as it is 
#KeywordVarLenArgsEx2.py
def  dispvalues(sno,sname,marks,cname): # Function Def-1
	print(sno,sname,marks,cname)

dispvalues(sno=100,sname="RS",marks=45.67,cname="OUCET") # Function call-1 with 4-Keyword args
#----------------------------------------------------------------------------------------------------------------------------------------------
def dispvalues(eno,ename,sal,compname,dsg): # Function Def-2
	print(eno,ename,sal,compname,dsg)
dispvalues(eno=1000,ename="TR",sal=5.6,compname="TCS",dsg="SE") # Function call-2 with 5-Keyword args
#----------------------------------------------------------------------------------------------------------------------------------------------
def dispvalues(sid,stname,hb1,hb2,hb3,hb4): # Function Def-3
	print(sid,stname,hb1,hb2,hb3,hb4)
dispvalues(sid=200,stname="abc",hb1="Sleeping",hb2="Eating",hb3="Chatting",hb4="Roaming") # Function call-3 with 6-Keyword args
#----------------------------------------------------------------------------------------------------------------------------------------------
def dispvalues(tno,tname,sub1):
	print(tno,tname,sub1)
dispvalues(tno=300,tname="Rossum",sub1="PYTHON-JAVA")# Function call-4 with 3-Keyword args
#----------------------------------------------------------------------------------------------------------------------------------------------
def dispvalues(cid) :
	print(cid)
dispvalues(cid=500) # Function call-5 with 1-Keyword arg
#----------------------------------------------------------------------------------------------------------------------------------------------


#Limitation: 
# In This Program -- we have 5 function calls---5 function defs
#In general ------------we have n-function calls---we need n-Function defs----waste of time takes more development time
# We need  n-function calls we have----we need 1 FUNCTION DEFINITION



