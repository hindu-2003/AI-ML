#Program for Copying the Image
#ImageFileCopy.py
try:
    with open("D:\\SUB\\kvr.png","rb") as rp: # Opening the SRC File in Read Mode
        with open("pyt.png","wb") as wp:# Opening the DEST File in write Mode
            srcdata=rp.read() # read the data from src file
            wp.write(srcdata) # Writing the src file data to dest. File
            print("Image File Copied--Verify")
except FileNotFoundError:
    print("Source File does not Exist")