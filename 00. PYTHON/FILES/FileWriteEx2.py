#Program for Demonstrating How to write the Data to the File
#FileWriteEx2.py
sno=int(input("Enter Ur Roll Number:"))
sname=input("Enter Ur Name:")
marks=float(input("Enter Ur Marks:"))
with open("stud.data","a") as fp:
    fp.write(str(sno)+"\t")
    fp.write(sname+"\t")
    fp.write(str(marks)+"\n")
    print("Data Written to the File")
