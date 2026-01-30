#Program for Demmonstrating How to Access the Data Randomly from File
#FilePointerObj.tell()-->Gives Index of File Pointer
#FilePointer.seek(Index)--->Will set File Pointer to Point to the Specified Index
#RandomAccessFileEx1.py
with open("kvr1.data","r") as fp:
    print("Initially, FP Points to:",fp.tell())
    filedata=fp.read(3)
    print("File Data=",filedata)
    print("Now FP Points to:{}".format(fp.tell()))
    print("--------------------------------")
    filedata = fp.read(4)
    print("File Data=",filedata)
    print("Now FP Points to:{}".format(fp.tell()))
    print("--------------------------------")
    filedata = fp.read(3)
    print("File Data=", filedata)
    print("Now FP Points to:{}".format(fp.tell()))#10
    print("--------------------------------")
    filedata = fp.read(3)
    print("File Data=", filedata)
    print("Now FP Points to:{}".format(fp.tell()))  #
    print("--------------------------------")
    filedata = fp.read(5)
    print("File Data=", filedata)
    print("Now FP Points to:{}".format(fp.tell()))  #
    print("--------------------------------")
    #-----------------------------------------------
    #To Re-set the File Pointer, we use seek()
    fp.seek(7)
    print("Now FP Points after seek() to:{}".format(fp.tell()))  #
    filedata = fp.read(3)
    print("File Data=", filedata)
    print("Now FP Points to:{}".format(fp.tell()))  #
    print("--------------------------------")
    fp.seek(0)
    print("Now FP Points after seek() to:{}".format(fp.tell()))  #
    #read complete data from file
    filedata=fp.read()
    print("File Data=",filedata)
    print("Now FP Points after seek() to:{}".format(fp.tell()))
#-----------------------------------------------------------------------





