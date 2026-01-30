#Program for Cal totmarks of Different Students who are studying Different Classes with Different Subject with Different Secured Marks.
#PureKeywordVarLenArgsEx4.py
def  findtotalmarks(sno,sname,cls,city="HYD",**submarks):
	print("-"*50)
	print("\tStudent Number:{}".format(sno))
	print("\tStudent Name:{}".format(sname))
	print("\tStudent Class:{}".format(cls))
	print("\tStudent City={}".format(city))
	print("\tSubjects\tMarks")
	print("*"*50)
	totmarks=0
	for subject,marks in submarks.items():
		print("\t{}\t\t{}".format(subject,marks))
		totmarks+=marks
	print("\tTOTAL MARKS={}".format(totmarks))
	print("="*50)

#Main Program
findtotalmarks(10,"Rajesh","X",Tel=60,Eng=70,Hindi=50,Maths=89,Sci=88,Soc=99) # Function Call-1
findtotalmarks(20,"Rakesh","XII",Sanskrit=99,English=98,Maths=75,Physics=60,Chemistry=60)# Function Call-2
findtotalmarks(30,"Ram","B.Tech",OS=50,DBMS=45,NW=48) # Function Call-3
findtotalmarks(40,"RS","Research") # Function Call-4
findtotalmarks(40,"Raj","4th",dw=40) # Function Call-5
findtotalmarks(50,"Raj","5th",rd=40,an=89,city="AP") # Function Call-6
findtotalmarks(50,"Raj","5th",city="AP",rd=40,an=89) # Function Call-6