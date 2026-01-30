#Program for Demonstrating Generator
#GenEx2.py
def kvrange(beg,end):
	while(beg<=end):
		yield beg
		beg=beg+1

#Main Program
print("-------------------------------------------")
r=kvrange(10,20) # Function Call
print(next(r))
while(True):
	try:
		print(next(r))
	except StopIteration:
		print("-------------------------------------------")
		break
print("-------------------------------------------")	
r1=kvrange(100,110)
print(next(r1))
print(next(r1))
for val in r1:
	print(val)

#print(next(r1))--------->Gives StopIteration