#Program for Demonstrating the Need of Iterators
#SetIterEx.py
x={10,"RS",23.45,3+4j,True,False}
print("Type of x=",type(x)) # <class, set>
print(x)
itr=iter(x)
print("Type of itr=",type(itr)) # <class 'set_iterator'>
print("---------------------------------------")
print("Content of Set_Iterator")
print("---------------------------------------")
for val in itr:
	print(val)
print("---------------------------------------")

