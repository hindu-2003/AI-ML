#Program for Copying the content of One File into Another File.
#FileCopyEx.py
try:
    srcfile=input("Enter Source File:")
    with open(srcfile,"rt") as rp: # Opening the SRC File in Read Mode
        dstfile=input("Enter Destination File:")
        with open(dstfile,"at") as wp:# Opening the DEST File in write Mode
            srcdata=rp.read() # read the data from src file
            wp.write(srcdata) # Writing the src file data to dest. File
            print("File Copied--Verify")
except FileNotFoundError:
    print("Source File does not Exist")