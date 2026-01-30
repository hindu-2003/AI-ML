#Program for Reading the Data from CSV File by using csv module--in the for form Dictionary--DictReader()
#CSVReadEx3.py
import csv
with open("employee.csv","r") as fp:
    csvr=csv.reader(fp)
    print("*"*50)
    for record in csvr: # here record is an object of <class,dict>
        for val in record:
            print("{}".format(val),end="\t")
        print()
    print("*" * 50)

