#Program for Demonstrating the Need of Iterators
#ListIterEx.py
x=[10,"RS",23.45,3+4j,True,False]
print("Type of x=",type(x)) # <class, list>
print(x)
itr=iter(x)
print("Type of itr=",type(itr)) # <class 'list_iterator'>
print("---------------------------------------")
print("Content of List_Iterator")
print("---------------------------------------")
while(True):
	try:
		print(next(itr))
	except StopIteration:
		print("---------------------------------------")
		break
