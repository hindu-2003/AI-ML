#Program for Demonstrating the NEED of Inheritance
#InhProgEx2.py
class C1:
	def disp1(self):
		print("C1--disp1()")

class C2:
	def disp2(self):
		print("C2--disp2()")
class C3(C1,C2):
	def disp3(self):
		print("C3--disp3()")

#Main Program
o3=C3()
o3.disp1()
o3.disp2()
o3.disp3()