#PloyEx16.py
class C1:
	def x(self):
		print("C1-x()")
class C2(C1):
	def x(self):
		print("C2-x()")
class C3(C1):
	def x(self):
		print("C3-x()")
class C4(C2):
	def x(self):
		print("C4-x()")	
class C5(C3):
	def x(self):
		print("C5-x()")
class C6(C4,C5):
	def x(self):
		print("C6-x()")
		C2.x(self)
		C1.x(self)
		C3.x(self)
		super().x()
		C5.x(self)
#Main Program
o6=C6()
o6.x()