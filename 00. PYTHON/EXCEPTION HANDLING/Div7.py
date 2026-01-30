#program for Performing Division of Two Numbers
#Div7.py
#Here On 10-07-2024----The Programmer KVR Defined this program with Two Exceptions
#After 5 years this code will go for Updations (adding some new code)---Rajeet new programmer 
try:
	print("Program Execution Started")
	s1=input("Enter First Value:")
	s2=input("Enter Second Value:")
	#Convert str type value into int type
	a=int(s1) #------------------------------- exception generated stmt--ValueError
	b=int(s2)#------------------------------- exception generated stmt--ValueError
	c=a/b  #------------------------------- exception generated stmt--ZeroDivisionError
	s="PYTHON"
	print(s[12])
except (ZeroDivisionError,ValueError,IndexError):
	print("\tDon't Enter Zero for Den....")
	print("\tDon't enter alnums,stmbols and str")
	print("\tcheck the Index")
except : # default except block
	print("Oooops Some thing went wrong!!!!")
else:
	print("-----else block------")
	print("First Value:",a)
	print("Second Value:",b)
	print("Div=",c)
finally:
	print("-----finally block------")
	print("Program Execution Ended")

