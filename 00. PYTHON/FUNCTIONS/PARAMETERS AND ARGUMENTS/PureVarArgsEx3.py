#Program for finding sum of Variable length Numerical values 
#This Program will  execute as it is 
#PureVarArgsEx3.py
def  findtotal(sno,sname,*vals):
	print("---------------------------------------------")
	print("Student Number:{}".format(sno))
	print("Student Name:{}".format(sname))
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

