#This Program demonstrates how to open the File
#FileOpenEx3.py
try:
    with open("kvr1.data") as fp:
        print("Type of fp=",fp)
        print("File Opened in read mode sucessfully")
except FileNotFoundError:
    print("File does not exist")