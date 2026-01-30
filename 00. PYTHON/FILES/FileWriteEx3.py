#Program for Demonstrating How to write the Iterable-object Data to the File
#FileWriteEx3.py
x= {10:"Python",20:"Java",30:"C"}
with open("stud1.data","a") as kv:
    kv.writelines(str(x)+"\n")
    print("Data Written to the File")

