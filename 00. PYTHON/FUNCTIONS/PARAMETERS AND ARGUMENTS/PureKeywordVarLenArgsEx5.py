#Program for Cal totmarks of Different Students who are studying Different Classes with Different Subject with Different Secured Marks.
#PureKeywordVarLenArgsEx5.py
def  findtotalmarks(sno,sname,cls,*vals,city="HYD",**submarks):
	print("="*50)
	print("Variables Length Values={}".format(vals))
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
findtotalmarks(10,"Rajesh","X",10,20,30,40,50,Tel=60,Eng=70,Hindi=50,Maths=89,Sci=88,Soc=99) # Function Call-1
findtotalmarks(20,"Rakesh","XII",100,200,300,400,Sanskrit=99,English=98,Maths=75,Physics=60,Chemistry=60)# Function Call-2
findtotalmarks(30,"Ram","B.Tech",1.2,2.3,3.4,OS=50,DBMS=45,NW=48) # Function Call-3
findtotalmarks(40,"RS","Research",-10,-20,-30,-40) # Function Call-4
findtotalmarks(40,"Raj","4th",dw=40) # Function Call-5
findtotalmarks(50,"Raj","5th",5,4,3,2,1,rd=40,an=89,city="AP") # Function Call-6
findtotalmarks(50,"Raj","6th",-5,-6,-6,-8,city="AP",rd=40,an=89) # Function Call-6"""
findtotalmarks(60,"KV","Trainer")

#NOTE-1
#>>> sno,sname,*marks=10,"RS",40,50,60
#>>> print(type(sno))
#<class 'int'>
#>>> print(type(sname))----------<class 'str'>
#>>> print(type(marks))-----------<class 'list'>
#>>> print(marks)-------------------[40, 50, 60]
#>>> print(marks[0],marks[1],marks[2])--------40 50 60
#NOTE-2
#-------------
#>>> *deatils=10,"RS",40,50,60------------SyntaxError: starred assignment target must be in a list or tuple
#>>> sno,*details=10,"RS",40,50,60
#>>> print(sno)------------10
#>>> print(details)--------------['RS', 40, 50, 60]
#------------------------------
