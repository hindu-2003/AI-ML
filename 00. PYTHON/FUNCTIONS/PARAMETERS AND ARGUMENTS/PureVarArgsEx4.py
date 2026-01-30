#Program for finding sum of Variable length Numerical values 
#This Program will  execute as it is 
#PureVarArgsEx4.py
def  findtotal(sno,sname,*vals,city="HYD",crs="PYTHON"):
	print("---------------------------------------------")
	print("Student Number:{}".format(sno))
	print("Student Name:{}".format(sname))
	print("Student City={}".format(city))
	print("Student Course={}".format(crs))
	s=0
	for val in vals:
		print(val,end=" ")
		s+=val
	print()
	print("Sum=",s)
	print("---------------------------------------------")

#Main Program
findtotal(100,"KV",10,20,30,40,50)
findtotal(200,"RK",100,200,300,400)
findtotal(300,"HS",1.2,2.3,4.5)
findtotal(400,"KR",10,2.3,4.5,20,5.6,7.8)
findtotal(500,"RS")
findtotal(crs="HTML",sno=600,sname="DR",city="USA")
findtotal(700,"MC",-1,-2,-3,-1.55,-3,44,5.66,city="AUS")
#findtotal(crs="Java",sno=800,sname="MC",-11,-12,-13,-1.55,-3,44)----SyntaxError: positional argument follows keyword argument
findtotal(800,"MC",-11,-12,-13,-1.55,-3,44,crs="Java",city="MUM")