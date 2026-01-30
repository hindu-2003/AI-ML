from rclass import DivsionByZeroError
def divop(a,b):
   if(b==0):
       raise DivsionByZeroError
   else:
       return(a/b)