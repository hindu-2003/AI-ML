#This Program demonstrates how to open the File
#FileOpenEx1.py
try:
    fp=open("kvr1.data","r")
    print("Type of fp=",type(fp))
    print("File Opened in Read Mode sucessfully")
except FileNotFoundError:
    print("File Does not Exist")
