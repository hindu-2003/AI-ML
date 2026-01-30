#Write a Python program to check a list is empty or not?
nov = int(input("Enter for number of values u want in list:"))
if nov<0:
    print("{} Invalid input try again".format(nov))
elif nov==0:
    print("Empty list ")
else:
    lst = []
    for i in range(1, nov + 1):
        val = input("Enter the {} value :".format(i))
        lst.append(val)
    print("Created Your List is :- {}".format(lst))
    print("Your list is non-empty")




