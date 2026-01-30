n =[int(val) for val in input().split()]
even = list(filter(lambda x:x%2==0,n))
print(even)