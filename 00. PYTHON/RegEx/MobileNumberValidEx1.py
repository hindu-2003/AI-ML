#Program for Validating Mobile Number by using Regular Expression.
#MobileNumberValidEx1.py
import re
while(True):
	mno=input("Enter Ur Mobile Number:")
	if(len(mno)==10):
		res=re.search(r"\d{10}",mno)
		if(res!=None):
			print("\t{} is valid Mobile Number-Save".format(mno))
			break
		else:
			print("\t{} is Invalid Mobile Number-bcoz It contains non-ints-try again".format(mno))
	else:
		print("\t{} is invalid Mobile Number Due to its length--try again".format(mno))