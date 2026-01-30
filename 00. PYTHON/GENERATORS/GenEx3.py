#Program for Demonstrating Generator
#GenEx3.py
class InputError(Exception):pass

def kvrange(start=0,stop=0,step=1):
	if((start==stop) and (stop==step)):
		raise InputError
	else:
		if(start>=stop):
			stop=start
			start=0
		while(start<=stop):
			yield start
			start=start+step

#Main Program
r=kvrange(10,20,2)
print(next(r))
print(next(r))
for val in r:
	print(val,end=" ")
print()
#print(next(r))-----------------Gives StopIteration
print("----------------------------------------------")
r2=kvrange(100,120,5)
print(next(r2))
print(next(r2))
for val in r2:
	print(val,end=" ")
print()
print("----------------------------------------------")
r3=kvrange(25,30) # Function Call
print(next(r3))
print(next(r3))
for val in r3:
	print(val,end=" ")
print()
print("----------------------------------------------")
r4=kvrange(5) # Function Call
print(next(r4))
print(next(r4))
for val in r4:
	print(val,end=" ")
print()
print("----------------------------------------------")
r4=kvrange(stop=6,step=2) # Function Call
print(next(r4))
print(next(r4))
for val in r4:
	print(val,end=" ")
print()
print("----------------------------------------------")
r4=kvrange(step=6,stop=30) # Function Call
print(next(r4))
print(next(r4))
for val in r4:
	print(val,end=" ")
print()
print("----------------------------------------------")
try:
	r5=kvrange(0,0,0) # Function Call
	print(next(r5))
except InputError:
	print("Check Start ,stop and step Values:")