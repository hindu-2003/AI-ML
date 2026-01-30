#Program for Demonstrating Obtaining File Properties
#FilePropertiesEx4.py
try:
    with open("Kvr5.data","x+") as fp:
        print("-----------------------------------")
        print("Name of the File=",fp.name)
        print("File Mode=",fp.mode)
        print("Is this File Readable?=",fp.readable())
        print("Is this File Writeable?=",fp.writable())
        print("Is This Closed?=",fp.closed)
        print("-----------------------------------")
    print("Out-off with open() as--Is This Closed?=",fp.closed) # Autoclosability
except FileExistsError:
    print("Specified File Name already exist")