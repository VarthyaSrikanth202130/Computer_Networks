"""server program to display the server machine's date and time on the client machine."""

import socket

def server_program():
    # get the hostname
    tcp_ip = "127.0.0.1"
    port = 4444

    server_socket = socket.socket()  # get instance

    server_socket.bind((tcp_ip, port))  # bind host address and port together

    # configure how many client the server can listen simultaneously
    server_socket.listen(5)
    conn, address = server_socket.accept()  # accept new connection
    print("Connection from: " + str(address))
    while True:
        # receive data stream. it won't accept data packet greater than 1024 bytes
        data = conn.recv(1024).decode()
        if not data:
            # if data is not received break
            break
        print("Client replied: " + str(data))
        data = input(' -> ')
        conn.send(data.encode())  # send data to the client

    conn.close()  # close the connection


if __name__ == '__main__':
    server_program()