
filename = input("Enter Any File Name:")
try:
    with open(filename,"r")as p:
        filename = input("Enter Any File Name:")
        with open(filename,"a")as wp:
            for line in p:
                wp.write(line)
except FileNotFoundError:
    print("File Does Not Exist")
