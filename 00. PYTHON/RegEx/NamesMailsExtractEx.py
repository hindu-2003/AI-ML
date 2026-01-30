#Program for Extaracting  Names and  Mails from Given File (mails.info)
#NamesMailsExtractEx.py
import re
try:
	with open("E:\\KVR-PYTHON-6PM\\REG EXPR\\NOTES\\mails.info","r") as fp:
		filedata=fp.read()
		nameslist=re.findall(r"[A-Z][a-z]+",filedata)
		mailslist=re.findall(r"\S+@\S+",filedata)
		print("="*50)
		print("\tNames\tMails")
		print("="*50)
		for names,mails in zip(nameslist,mailslist):
			print("\t{}\t{}".format(names,mails))
		print("="*50)
except FileNotFoundError:
	print("File does not Exist")

