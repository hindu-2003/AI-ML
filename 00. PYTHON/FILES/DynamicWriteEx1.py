#Program for Reading the Input from KeyBoard and save it in File
#DynamicWriteEx1.py
print("Enter the Data from Key Board Press @ to stop:")
with open("hyd.data","a") as fp:
    while(True):
        kbdata=input()
        if(kbdata!="@"):
            fp.write(kbdata+"\n")
        else:
            print("Data Written to the File--verify")
            break

