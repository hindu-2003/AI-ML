#Program for Demonstrating the NEED of Inheritance
#Non_InhProgEx.py
class C1:
	def disp1(self):
		print("C1--disp1()")

class C2:
	def disp2(self):
		print("C2--disp2()")

class C3:
	def disp3(self):
		print("C3--disp3()")

#Main Program
o1=C1()
o2=C2()
o3=C3()
o1.disp1()
o2.disp2()
o3.disp3()