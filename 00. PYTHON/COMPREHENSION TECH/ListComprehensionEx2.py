#Program for accepting Only +ve Values from KBD even the user enter -ve value and zeros
#ListComprehensionEx2.py
print('Enter List of Numerical values separated by space:')
pslist=[int(value) for value in input().split() if int(value)>0]
print("List of +ve Values=",pslist)
