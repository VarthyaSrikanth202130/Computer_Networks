"""client program which displays the server machine's date and time on the client machine."""

import socket

# create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

# get local machine name
tcp_ip = "127.0.0.1"
port = 4444 

# connection to hostname on the port.
s.connect((tcp_ip, port))                               

# Receive no more than 1024 bytes
tm = s.recv(1024)                                     

s.close()

print("The time got from the server is: %s" % tm.decode('ascii'))