"""server program which displays the server machine's date and time on the client machine."""

import socket                                         
import time
# create a socket object
serversocket = socket.socket(
         socket.AF_INET, socket.SOCK_STREAM) 

# get local machine name
tcp_ip = "127.0.0.1"
port = 4444                                            

# bind to the port
serversocket.bind((tcp_ip, port))                                  

# queue up to 5 requests
serversocket.listen(5)                                        
while True:
    # establish a connection
    clientsocket,addr = serversocket.accept()      

    print("Got a connection from %s" % str(addr))
    currentTime = time.ctime(time.time()) + "\r\n"
    clientsocket.send(currentTime.encode('ascii'))
    clientsocket.close()