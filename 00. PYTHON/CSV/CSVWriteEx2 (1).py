#Program for adding Record to the Existing CSV File though Python Lang.
#CSVWriteEx2.py
import csv
record=[700,"KVR",0.0] # Single Record
with open("emp.csv","a") as fp:
	csvwr=csv.writer(fp) # here csvwr is an object of <class, csv.writer>
	csvwr.writerow(record)
	print("record added to emp.csv file")

