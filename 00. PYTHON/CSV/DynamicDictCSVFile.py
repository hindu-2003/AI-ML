#Program for Creating Dynamic CSV File
#DynamicDictCSVFile.py
import csv
noc=int(input("Enter How Many Columns in CSV File u want:"))
if(noc<=0):
    print('Invalid Number of Columns')
else:
    hnames=list() # creating an empty list
    for i in range(1,noc+1):
        colname=input('Enter {} Col Name:'.format(i))
        hnames.append(colname)
    else: # hnames=['PID', 'PNAME', 'PRICE', 'Bname']
        nor=int(input("Enter How Many Records u want to Enter:"))
        if(nor<=0):
            print("Invalid Number of Records-can't create csv file")
        else:
            records=[] # for Storing Multiple Records(Dict in list)
            for i in range(1,nor+1):
                print("Enter {} Record Data:".format(i))
                print("-"*50)
                record = {}  # empty dict for storing Single Record--(Key,Value)
                for colname in hnames:
                    val=input("Enter Value for {}:".format(colname))
                    #Add (colname,Val) to empty dict
                    record[colname]=val
                records.append(record)
                print("-" * 50)
            else:
                #Choose the CSF File and Open it into write mode
                csvfilename=input("Enter the CSV File Name with an extenson .csv:")
                if(not csvfilename.endswith(".csv")):
                    print("U Don't Know CSV Concept--Plz Open the Notes")
                else:
                    with open("D:\\My-Teaching\\PYTHON\\TEACH-PYTHON\\CSV\\"+csvfilename,"w") as fp:
                        csvwr=csv.DictWriter(fp,fieldnames=hnames)
                        csvwr.writeheader()
                        csvwr.writerows(records)
                        print("CSV File Created Dynamically--verify")

