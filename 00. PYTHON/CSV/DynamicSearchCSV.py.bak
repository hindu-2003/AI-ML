#Program finding details about those people who are living in TS.
#Use adhar.csv file
#DynamicSearchCSV.py
import csv
with open("E:\\KVR-PYTHON-6PM\\CSV\\NOTES\\adhar.csv","r") as fp:
    csvr=csv.reader(fp)
    hname=next(csvr)
    print("-"*50)
    for name in hname:
        print(name,end="\t")
    print()
    print("-" * 50)
    for record in csvr:
        if(record):
            for val in record:
                print(val,end="\t")
            print()
    print("-"*50)
    ano=input("Enter Ur Adhar Card Number:")
    #Reset the File Pointer
    fp.seek(0)
    csvr = csv.reader(fp)
    res=False
    for record in csvr:
        if(record):
            if(ano==record[0]):
                res=True
                break
    if(res):
        print("-------------------------------------")
        print("Ur details along adhar Card Number")
        print("Ur Adhar Card Nunber:{}".format(record[0]))
        print("Ur Name:{}".format(record[1]))
        print("Ur State:{}".format(record[2]))
        print("Ur Country:{}".format(record[3]))
        print("-------------------------------------")
    else:
        print("{} Number Does not Exist-Goto Adhar Center".format(ano))



