# demonstrate the list values are even and odd separately printed
num = [1,2,3,4,5,6,7,8,9,10,11,2,3]
even=[]
odd= []
for number in num:
    if number % 2 == 1:
        odd.append(number)
    else:
        even.append(number)

print("Even numbers are given list:",even)

print("odd numbers are given list:",odd)