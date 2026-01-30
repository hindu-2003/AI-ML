#Program for Reading the Data from CSV File by using csv module--in the for form Dictionary--DictReader()
#CSVDictReadEx3.py
import csv
with open("employee.csv","r") as fp:
	csvdr=csv.DictReader(fp)
	for record in csvdr: # here record is an object of <class,dict>
		print("-"*50)
		for k,v in record.items():
			print("\t{}--->{}".format(k,v))
		print("-"*50)
