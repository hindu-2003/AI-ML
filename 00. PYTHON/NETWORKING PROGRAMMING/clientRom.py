#clientRom.py
import socket
sc = socket.socket()
sc.connect( ("localhost",8888) )
print("--------------------------------------")
n = input("Enter a Number for Getting For Roman Number:")
sc.send(n.encode())
rv = sc.recv(1024).decode()
print("Roman({})={}".format(n,rv))
