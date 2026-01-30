#Program for Reading the Data from CSV File by using csv module--in the for form Tabular format--reader()
#CSVReadEx1.py
import csv
with open("student.csv","r") as fp:
	csvr=csv.reader(fp) # here csvr is an object of <class, _csv.reader>
	for record in csvr:
		for val in record:
			print("{}".format(val),end="\t")
		print()