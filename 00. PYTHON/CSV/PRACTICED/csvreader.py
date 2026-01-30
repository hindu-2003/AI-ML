import csv
with open("stud.csv","r")as fp:
    csr = csv.reader(fp)
    for val in csr:
        for rec in val:
            print("{}".format(rec),end="\t")
        print()