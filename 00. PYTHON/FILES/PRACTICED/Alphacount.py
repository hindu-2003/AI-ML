
def fileword():
    try:
        filename = input("Enter Any File Name:")
        with open(filename, "rt") as p:
            with open("alpha", "a") as out:
                for line in p:
                    for l in line:
                        if l.isalpha():
                            out.write(l+" ")
    except FileNotFoundError:
        print("File Does not Exist")
# Main Program
fileword()

