#Program for Reading the Data from the File
#FileReadEx1.py
try:
    with open("hyd.data") as fp:
        filedata=fp.read()
        print("-----------------------------")
        print(filedata)
        print("-----------------------------")
except FileNotFoundError:
    print("File Does not Exist")