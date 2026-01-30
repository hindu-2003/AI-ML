from stdmenu import menu
from stdpick2 import writes
from stdunpick2 import reads
def stddemo():	
	while(True):
		try:
			ch=int(input("Enter Ur Choice:"))
			match(ch):
				case 1:
					writes()
				case 2:
					reads()
				case 3:
					print("Thx for Using Program")
					break
				case _:
					print("Ur Selection of Operation is wrong--try again")
		except ValueError:
			print("Don't Enter alnums,str,symbols and floats for Choice of Operation--enter int values")