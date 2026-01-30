#Program for Demonstrating Generator
#GenEx1.py
def  kvrange(Val):
	i=0
	while(i<Val):
		yield i
		i=i+1

#Main Program
r=kvrange(6) # Function call
print("type of r=",type(r)) # here 'r' is an object of <class, 'generator'>
print("content of r=",r)
#Extract the Data from generator object--Approach-1
print(next(r))
print(next(r))
print(next(r))
print(next(r))
print(next(r))
print(next(r))
#print(next(r))------generates  StopIteration
#Extract the Data from generator object--Approach-2
r1=kvrange(10)
print("type of r1=",type(r1)) # here 'r1' is an object of <class, 'generator'>
while(True):
	try:
		print(next(r1))
	except StopIteration:
		break
#Extract the Data from generator object--Approach-3
r2=kvrange(20)
print("type of r2=",type(r2)) # here 'r2' is an object of <class, 'generator'>
for val in r2:
	print(val,end="  ")
print()