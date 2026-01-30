#Program for Demonstrating Obtaining File Properties
#FilePropertiesEx1.py
try:
    fp=open("mahi.data","a")
except FileNotFoundError:
    print("File does not exist")
else:
    print("-----------------------------------")
    print("File Opened in Read Mode Successfully")
    print("Name of the File=",fp.name)
    print("File Mode=",fp.mode)
    print("Is this File Readable?=",fp.readable())
    print("Is this File Writeable?=",fp.writable())
    print("Is This Closed?=",fp.closed)
    print("-----------------------------------")
finally:
    print("I am from finally block")
    fp.close() # Manual Closing
    print("Is This Closed?=", fp.closed)