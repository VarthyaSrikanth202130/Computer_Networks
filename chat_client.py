"""client program which displays the server machine's date and time on the client machine."""

import socket

def client_program():
    tcp_ip = "127.0.0.1"
    port = 4444  # socket server port number

    client_socket = socket.socket()  # instantiate
    client_socket.connect((tcp_ip, port))  # connect to the server

    message = input(" -> ")  # take input

    while message.lower().strip() != 'bye':
        client_socket.send(message.encode())  # send message
        data = client_socket.recv(1024).decode()  # receive response

        print('Received from server: ' + data)  # show in terminal

        message = input(" -> ")  # again take input

    client_socket.close()  # close the connection


if __name__ == '__main__':
    client_program()