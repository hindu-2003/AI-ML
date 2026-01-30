#Program for Demonstrating Obtaining File Properties
#FilePropertiesEx3.py
with open("E:\\KVR-PYTHON-6PM\\FILES\\NOTES\\Kvr3.data","w+") as fp:
    print("-----------------------------------")
    print("Name of the File=",fp.name)
    print("File Mode=",fp.mode)
    print("Is this File Readable?=",fp.readable())
    print("Is this File Writeable?=",fp.writable())
    print("Is This Closed?=",fp.closed)
    print("-----------------------------------")
print("Out-off with open() as--Is This Closed?=",fp.closed) # Autoclosability