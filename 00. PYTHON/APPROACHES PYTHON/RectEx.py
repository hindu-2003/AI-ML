#program for Cal Area and Perimeter of Rect
#Accept the Input
length=float(input("Enter Length:"))
breadth=float(input("Enter Breadth:"))
#Cal Area of Rect and perimter
ra=length*breadth
rp=2*(length+breadth)
#displat the Result
print("="*50)
print("Length={}".format(length))
print("Breadth={}".format(breadth))
print("Area of Rect={}".format(ra))
print("Perimeter of Rect={}".format(rp))
print("*"*50)


"""
>>> "3"*4
'3333'
>>> "2+3"*2
'2+32+3'
>>> str(2+3)*4
'5555'
>>> str(2)+str(2*3)*3
'2666'
>>>
"""