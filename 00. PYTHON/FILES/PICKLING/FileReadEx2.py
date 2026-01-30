#Program for Reading the Data from the File
#FileReadEx2.py
try:
    with open("hyd.data") as fp:
        filedata=fp.readlines()
        print("-----------------------------")
        for line in filedata:
            print(line,end="")
        print("-----------------------------")
except FileNotFoundError:
    print("File Does not Exist")