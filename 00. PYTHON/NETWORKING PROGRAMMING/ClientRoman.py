#Write a Client Side Program, which will read a Numerical Integer Value from KBD , send to Server Side Program and get Its Eqv Roman Number from Server Side Program.
#ClientRoman.py
import socket
s=socket.socket()
s.connect(("localhost",8888))
print("CSP Connected to SSP")
print("---------------------------------------")
n=input("Enter any Number for getting Its Roman Eqv:")
s.send(n.encode())
rv=s.recv(1024).decode()
print("Roman({})={}".format(n,rv))