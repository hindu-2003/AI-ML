#Program for Demonstrating How to write the Data to the File
#FileWriteEx1.py
sno=30
sname="KV"
marks=11.22
with open("stud.data","a") as fp:
    fp.write(str(sno)+"\t")
    fp.write(sname+"\t")
    fp.write(str(marks)+"\n")
    print("Data Written to the File")
