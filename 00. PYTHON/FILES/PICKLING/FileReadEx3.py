#Program for Displaying the content of any File b y accepting the file name
#FileReadEx3.py
try:
    filename=input("Enter File Name to view Its Content:")
    fp=open(filename,"r")
except FileNotFoundError:
    print("File Does not Exist")
else:
    filedata=fp.read()
    if(len(filedata)==0):
        print("File is Empty")
    else:
        print("--------------------------------")
        print("Content of:{}".format(fp.name))
        print("--------------------------------")
        print(filedata)
        print("--------------------------------")


